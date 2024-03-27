# -*- coding: utf-8 -*-
# @Time    : 2023-08-01 17:14
# @Author  : Jiang Liu
# @Desc    : 该脚本用于从Zotero中导出的参考文献列表（csv格式文件）解析出对象，方便后续处理

import csv
import os
import re


class Reference:
    """
    该类用于存储参考文献的信息
    """

    def __init__(self, publication_year=None, author=None, title=None, title_en=None, doi=None, url=None,
                 abstract_note=None, notes=None, file_attachments=None, automatic_tags=None):
        """
        :param publication_year:    发表年份
        :param author:              作者
        :param title:               标题
        :param title_en:            英文标题
        :param doi:                 DOI
        :param url:                 链接
        :param abstract_note:       概述
        :param notes:               笔记（来自Zotero）
        :param file_attachments:    附件（本地绝对路径）
        :param automatic_tags:      关键词
        """
        self.publication_year = publication_year
        self.author = author
        self.title = title
        self.title_en = title_en,
        self.doi = doi
        self.url = url
        self.abstract_note = abstract_note
        self.notes = notes
        self.file_attachments = file_attachments
        self.automatic_tags = automatic_tags

    def __str__(self):
        return {
            "publication_year": self.publication_year,
            "author": self.author,
            "title": self.title,
            "doi": self.doi,
            "url": self.url,
            "abstract_note": self.abstract_note,
            "notes": self.notes,
            "file_attachments": self.file_attachments,
            "automatic_tags": self.automatic_tags,
        }.__str__()


def parse_extra_zotero(extra):
    matches = re.findall(
        r'(titleTranslation|abstractTranslation|Number|_eprint|Conference Name|Place):((?:(?!titleTranslation|abstractTranslation|Number|_eprint|Conference Name|Place).)*)',
        extra)
    result = {match[0]: match[1].strip() for match in matches}
    return result


def parser(csv_file_path):
    """
    该函数用于解析csv文件，生成Reference对象数组
    :param csv_file_path: csv文件路径
    :return:              Reference对象数组
    """
    # 对象数组：用于存储解析出的Reference对象
    reference_object_list = []
    # 字典数组：用于存储纯粹的键值对，方便后续生成Reference对象（不依赖于csv文件的列顺序）
    reference_map_list = []
    # 字符串数组：用于存储csv文件的列名，其中 reference_key_list[0] 为 第一个列名，reference_key_list[1] 为 第二个列名，以此类推
    reference_key_list = []
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for index, row in enumerate(csv_reader):
            if index == 0:
                reference_key_list = row
            else:
                reference_map = {}
                for i, value in enumerate(row):
                    reference_map[reference_key_list[i]] = value
                reference_map_list.append(reference_map)

    # 将字典数组转换为对象数组
    for reference_map in reference_map_list:
        reference_object = Reference()
        reference_object.author = reference_map['Author']
        reference_object.publication_year = reference_map['Publication Year']
        reference_object.doi = reference_map['DOI']
        reference_object.file_attachments = reference_map['File Attachments']
        reference_object.automatic_tags = reference_map['Automatic Tags']
        reference_object.notes = reference_map['Notes']
        reference_object.issn = reference_map['ISSN']
        reference_object.pages = reference_map['Pages']

        # 针对标题和摘要，Zotero提供了翻译功能，如果有翻译，则使用翻译，否则使用原文
        # Zotero将翻译后的标题和摘要存储在 Extra 字段中，格式为："titleTranslation:xxx abstractTranslation:xxx"，还包含其他信息，因此需要进行分割函数
        extra = parse_extra_zotero(reference_map['Extra'])
        # 如果有翻译标题，则使用翻译标题，否则使用原标题
        reference_object.title = extra['titleTranslation'] if \
            "titleTranslation" in extra else reference_map['Title']
        reference_object.title_en = reference_map['Title']
        # 如果有翻译摘要，则使用翻译摘要，否则使用原摘要
        reference_object.abstract_note = extra['abstractTranslation'] if \
            "abstractTranslation" in extra else reference_map['Abstract Note']
        reference_object_list.append(reference_object)

        # 有时候链接并非链接，而是一串字符，需要进行处理
        # 检查url是否是http链接
        if not reference_map['Url'].startswith('http'):
            # 如果不是http链接，则检查DOI是否存在，如果存在，则使用DOI作为链接，否则使用空字符串
            if reference_map['DOI']:
                reference_object.url = f'https://doi.org/{reference_map["DOI"]}'
            else:
                reference_object.url = ""
        else:
            reference_object.url = reference_map['Url']

    # 以下为PDF提取图片时使用，如果附件有多个，使用最后一个附件
    # 拷贝PDF文件到指定文件夹
    # for reference_map in reference_map_list:
    #     file_attachment = reference_map['File Attachments']
    #     if reference_map['File Attachments'].count(';') > 0:
    #         file_attachment = reference_map['File Attachments'].split(';')[-1].strip()
    #     if not file_attachment.endswith('.pdf'):
    #         continue
    #     print(
    #         f"copy \"{file_attachment}\" " + r"D:\Users\Administrator\Desktop")
    # # 将文件夹名改名（用于PDF图片提取后文件夹更名）
    # for reference_map in reference_map_list:
    #     file_attachment = reference_map['File Attachments']
    #     if reference_map['File Attachments'].count(';') > 0:
    #         file_attachment = reference_map['File Attachments'].split(';')[-1].strip()
    #     if not file_attachment.endswith('.pdf'):
    #         continue
    #     print(
    #         f"ren \"{os.path.basename(file_attachment.split('.')[0].strip())}\" \"{reference_map['ISSN']}_{reference_map['Pages']}\"")

    # 按照年份排序
    sorted(reference_object_list, key=lambda obj: obj.publication_year)
    return reference_object_list


def main():
    # csv_file_path = r"D:\Data\Papers\韩仲志\国内期刊\导出的条目.csv"
    csv_file_path = r"D:\Data\Papers\韩仲志\国际期刊\导出的条目.csv"
    reference_object_list = parser(csv_file_path)
    # print()
    # for reference in reference_object_list:
    #     print(f'Title: {reference.title}')
    #     print(f'Abstract: {reference.abstract_note}')
    #     print(f'Publication Year: {reference.publication_year}')
    #     print()


if __name__ == '__main__':
    main()
