# -*- coding: utf-8 -*-
# @Time    : 2023-08-01 17:46
# @Author  : Jiang Liu
# @Desc    : 该脚本用于将参考文献对象列表转换为markdown格式

import re
import os

import parse_the_reference_list_from_zotero_csv as parser_csv


def to_pdf_link(file_attachments):
    basename_link_pair = {
        r"C:\Users\Administrator\Zotero\storage\842S9GP6\Wu 等 - 2023 - Identification of Soybean Mutant Lines Based on Du.pdf": "https://cdn.taibai.cloud/docsify/han-zhong-zhi/paper/foreign/Wu%20%E7%AD%89%20-%202023%20-%20Identification%20of%20Soybean%20Mutant%20Lines%20Based%20on%20Du.pdf",
        r"C:\Users\Administrator\Zotero\storage\7VJ48JTX\Yang 等 - 2021 - A novel method for peanut variety identification a.pdf": "https://cdn.taibai.cloud/docsify/han-zhong-zhi/paper/foreign/Xu%20%E7%AD%89%20-%202020%20-%20Analysis%20of%20Behavior%20Trajectory%20Based%20on%20Deep%20Lear.pdf",
        r"C:\Users\Administrator\Zotero\storage\FDCEWLDD\Xu 等 - 2020 - Analysis of Behavior Trajectory Based on Deep Lear.pdf": "https://cdn.taibai.cloud/docsify/han-zhong-zhi/paper/foreign/Xu%20%E7%AD%89%20-%202020%20-%20Analysis%20of%20Behavior%20Trajectory%20Based%20on%20Deep%20Lear.pdf",
        r"C:\Users\Administrator\Zotero\storage\GTQ4MM8V\9296756.html; C:\Users\Administrator\Zotero\storage\QBSN9YQA\Ni 等 - 2020 - Monitoring the Change Process of Banana Freshness .pdf": "https://cdn.taibai.cloud/docsify/han-zhong-zhi/paper/foreign/Ni%20%E7%AD%89%20-%202020%20-%20Monitoring%20the%20Change%20Process%20of%20Banana%20Freshness%20.pdf",
        r"C:\Users\Administrator\Zotero\storage\Y92W75H2\8945222.html; C:\Users\Administrator\Zotero\storage\LQEA2YZ9\Li 等 - 2020 - Detection and Analysis of Behavior Trajectory for .pdf": "https://cdn.taibai.cloud/docsify/han-zhong-zhi/paper/foreign/Li%20%E7%AD%89%20-%202020%20-%20Detection%20and%20Analysis%20of%20Behavior%20Trajectory%20for%20.pdf",

        r"C:\Users\Administrator\Zotero\storage\S2E7JDE8\杨 等 - 2021 - 基于深度学习声谱图分类的“听声识风”.pdf": "https://cdn.taibai.cloud/docsify/han-zhong-zhi/paper/%E5%9F%BA%E4%BA%8E%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E5%A3%B0%E8%B0%B1%E5%9B%BE%E5%88%86%E7%B1%BB%E7%9A%84%E2%80%9C%E5%90%AC%E5%A3%B0%E8%AF%86%E9%A3%8E%E2%80%9D.pdf",
        r"C:\Users\Administrator\Zotero\storage\3ABGGUZX\倪 等 - 2021 - 基于改进型AlexNet的花生荚果品种识别.pdf": "https://cdn.taibai.cloud/docsify/han-zhong-zhi/paper/%E5%9F%BA%E4%BA%8E%E6%94%B9%E8%BF%9B%E5%9E%8BAlexNet%E7%9A%84%E8%8A%B1%E7%94%9F%E8%8D%9A%E6%9E%9C%E5%93%81%E7%A7%8D%E8%AF%86%E5%88%AB.pdf",
        r"C:\Users\Administrator\Zotero\storage\6RSTYGUF\高 等 - 2021 - 基于数据平衡和深度学习的开心果品质视觉检测方法.pdf": "https://cdn.taibai.cloud/docsify/han-zhong-zhi/paper/%E5%9F%BA%E4%BA%8E%E6%95%B0%E6%8D%AE%E5%B9%B3%E8%A1%A1%E5%92%8C%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E7%9A%84%E5%BC%80%E5%BF%83%E6%9E%9C%E5%93%81%E8%B4%A8%E8%A7%86%E8%A7%89%E6%A3%80%E6%B5%8B%E6%96%B9%E6%B3%95.pdf",
        r"C:\Users\Administrator\Zotero\storage\6U74XI29\卜 等 - 2020 - 基于Zernike矩与SIFT特征的商标检索算法.pdf": "https://cdn.taibai.cloud/docsify/han-zhong-zhi/paper/%E5%9F%BA%E4%BA%8EZernike%E7%9F%A9%E4%B8%8ESIFT%E7%89%B9%E5%BE%81%E7%9A%84%E5%95%86%E6%A0%87%E6%A3%80%E7%B4%A2%E7%AE%97%E6%B3%95.pdf",
        r"C:\Users\Administrator\Zotero\storage\28Z23FDG\王 等 - 2020 - 基于数据平衡深度学习的不同成熟度冬枣识别.pdf": "https://cdn.taibai.cloud/docsify/han-zhong-zhi/paper/%E5%9F%BA%E4%BA%8E%E6%95%B0%E6%8D%AE%E5%B9%B3%E8%A1%A1%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E7%9A%84%E4%B8%8D%E5%90%8C%E6%88%90%E7%86%9F%E5%BA%A6%E5%86%AC%E6%9E%A3%E8%AF%86%E5%88%AB.pdf",
        r"C:\Users\Administrator\Zotero\storage\G8ICZPBP\倪 等 - 2020 - 基于知识蒸馏的胡萝卜外观品质等级智能检测.pdf": "https://cdn.taibai.cloud/docsify/han-zhong-zhi/paper/%E5%9F%BA%E4%BA%8E%E7%9F%A5%E8%AF%86%E8%92%B8%E9%A6%8F%E7%9A%84%E8%83%A1%E8%90%9D%E5%8D%9C%E5%A4%96%E8%A7%82%E5%93%81%E8%B4%A8%E7%AD%89%E7%BA%A7%E6%99%BA%E8%83%BD%E6%A3%80%E6%B5%8B.pdf",
        r"C:\Users\Administrator\Zotero\storage\MHHT4N3B\韩 和 刘 - 2020 - 高光谱亚像元分解预测花生中的黄曲霉毒素B_1.pdf": "https://cdn.taibai.cloud/docsify/han-zhong-zhi/paper/%E9%AB%98%E5%85%89%E8%B0%B1%E4%BA%9A%E5%83%8F%E5%85%83%E5%88%86%E8%A7%A3%E9%A2%84%E6%B5%8B%E8%8A%B1%E7%94%9F%E4%B8%AD%E7%9A%84%E9%BB%84%E6%9B%B2%E9%9C%89%E6%AF%92%E7%B4%A0B1.pdf",
        r"C:\Users\Administrator\Zotero\storage\NBQPXXQG\王 等 - 2019 - 大沽河流域土壤养分、重金属与pH高光谱探测.pdf": "https://cdn.taibai.cloud/docsify/han-zhong-zhi/paper/%E5%A4%A7%E6%B2%BD%E6%B2%B3%E6%B5%81%E5%9F%9F%E5%9C%9F%E5%A3%A4%E5%85%BB%E5%88%86%E3%80%81%E9%87%8D%E9%87%91%E5%B1%9E%E4%B8%8EpH%E9%AB%98%E5%85%89%E8%B0%B1%E6%8E%A2%E6%B5%8B.pdf",
        r"C:\Users\Administrator\Zotero\storage\A8VYUINL\韩 等 - 2019 - 高光谱遥感分区混合端元提取计算海洋溢油覆盖度.pdf": "https://cdn.taibai.cloud/docsify/han-zhong-zhi/paper/%E9%AB%98%E5%85%89%E8%B0%B1%E9%81%A5%E6%84%9F%E5%88%86%E5%8C%BA%E6%B7%B7%E5%90%88%E7%AB%AF%E5%85%83%E6%8F%90%E5%8F%96%E8%AE%A1%E7%AE%97%E6%B5%B7%E6%B4%8B%E6%BA%A2%E6%B2%B9%E8%A6%86%E7%9B%96%E5%BA%A6.pdf",
        r"C:\Users\Administrator\Zotero\storage\L4M4S4HX\郭 等 - 2019 - 物联网中的无线传感器网络技术综述.pdf": "https://cdn.taibai.cloud/docsify/han-zhong-zhi/paper/%E7%89%A9%E8%81%94%E7%BD%91%E4%B8%AD%E7%9A%84%E6%97%A0%E7%BA%BF%E4%BC%A0%E6%84%9F%E5%99%A8%E7%BD%91%E7%BB%9C%E6%8A%80%E6%9C%AF%E7%BB%BC%E8%BF%B0.pdf",
        r"C:\Users\Administrator\Zotero\storage\E5ZJDHCW\王 等 - 2018 - 混合式随机森林的土壤钾含量高光谱反演.pdf": "https://cdn.taibai.cloud/docsify/han-zhong-zhi/paper/%E6%B7%B7%E5%90%88%E5%BC%8F%E9%9A%8F%E6%9C%BA%E6%A3%AE%E6%9E%97%E7%9A%84%E5%9C%9F%E5%A3%A4%E9%92%BE%E5%90%AB%E9%87%8F%E9%AB%98%E5%85%89%E8%B0%B1%E5%8F%8D%E6%BC%94.pdf",
        r"C:\Users\Administrator\Zotero\storage\RUVV7NTF\韩 等 - 2017 - 利用高光谱图像的独立成分分析进行丰度量化以计算油污覆盖范围.pdf": "https://cdn.taibai.cloud/docsify/han-zhong-zhi/paper/Abundance%20qua...e%20calculation.pdf",
    }
    if len(file_attachments) > 0 and file_attachments in basename_link_pair:
        pdf_basename = os.path.basename(file_attachments)
        return f"[{pdf_basename}]({basename_link_pair[file_attachments]})"
    return "无"


def reference_to_md(reference, image_file_folder, title_serial_number, index):
    # 如果有图片附件，则添加图片
    images = []
    image_file_folder = os.path.join(image_file_folder, f"{reference.issn}_{reference.pages}")
    if os.path.exists(image_file_folder):
        for file in os.listdir(image_file_folder):
            if file.endswith('.jpg') or file.endswith('.png'):
                images.append(os.path.join(image_file_folder, file))
    images_md = ""
    for image in images:
        image_basename = os.path.basename(image)
        folder = f"{reference.issn}_{reference.pages}"
        # https://cdn.taibai.cloud/docsify/han-zhong-zhi/src/paper-img/{folder}/{image_basename}
        image_link = f"https://cdn.taibai.cloud/docsify/han-zhong-zhi/src/paper-img/{folder}/{image_basename}"
        images_md += f'<img src="{image_link}" alt="image_basename" />\n'
    images_md = '<div class="custom-paper-image-group">\n' + images_md + '</div>\n'

    # if reference.file_attachments.endswith('.pdf'):
    #     print(reference.file_attachments)
    md = f"""
### {title_serial_number}.{index} {reference.title}

> - 发表年份: {reference.publication_year}
> - 论文链接: [{reference.title_en}]({reference.url})
> - 论文PDF: {to_pdf_link(reference.file_attachments) if reference.file_attachments else "无"}
> - 作者: {reference.author}
> - DOI: {reference.doi if reference.doi else "无"}
 
摘要:

{reference.abstract_note}

关键词: {reference.automatic_tags}

{"笔记:" if reference.notes else ""}

{reference.notes}

{images_md if len(images) > 0 else ""}

"""
    # 去除多余的换行符
    md = re.sub('\n{2,}', '\n\n', md)
    return md


def reference_list_to_md(reference_list, image_file_folder, title, title_serial_number):
    md = f"## {title_serial_number}. {title}\n"
    for index, reference in enumerate(reference_list):
        md += reference_to_md(reference, image_file_folder, title_serial_number, index + 1)
    return md


def main():
    csv_file_path_foreign = r"D:\Data\Papers\韩仲志\外网获取\导出的条目.csv"
    image_file_folder = r"D:\Data\Papers\韩仲志\图片汇总"
    reference_object_list = parser_csv.parser(csv_file_path_foreign)
    md = reference_list_to_md(reference_object_list, image_file_folder, "近5年国际期刊发表（按年份排序）",
                              title_serial_number=3)
    print(md)

    print()

    csv_file_path_local = r'D:\Data\Papers\韩仲志\知网\导出的条目.csv'
    reference_object_list = parser_csv.parser(csv_file_path_local)
    md = reference_list_to_md(reference_object_list, image_file_folder, "近5年国内期刊发表（按年份排序）",
                              title_serial_number=4)
    print(md)


if __name__ == '__main__':
    main()
