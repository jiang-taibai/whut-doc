# -*- coding: utf-8 -*-
# @Time    : 2023-08-02 00:11
# @Author  : Jiang Liu
# @Desc    : 该脚本用于从PDF中提取图片，并进行数据清洗（过滤掉小图像、某颜色占比超过50%的图像等）

import io
import os
from os import path
from PIL import Image
import glob

import fitz  # PyMuPDF库


def image_validator(image_bytes):
    try:
        image = Image.open(io.BytesIO(image_bytes))
        # 过滤小图像
        if image.size[0] * image.size[1] < 10000:
            return False
        # 尝试获取颜色信息，增加maxcolors的值
        colors = image.convert('RGB').getcolors(maxcolors=10000)
        if colors is not None:
            # 查找出现次数最多的颜色及其计数
            max_count = 0
            sum_count = 0
            for count, color in colors:
                if count > max_count:
                    max_count = count
                    sum_count += count
            if max_count > (sum_count * 0.5):
                return False
        colors = image.convert('L').getcolors(maxcolors=256)
        if colors is None or len(colors) < 220:
            return False

        return True
    except Exception as e:
        print(e)
        return False


def extract_image_from_pdf(pdf_file_path, image_file_path):
    file_path = pdf_file_path
    doc = fitz.open(file_path)

    # 如果没有文件夹则创建
    os.makedirs(image_file_path, exist_ok=True)
    os.makedirs(path.join(image_file_path, "filtered"), exist_ok=True)

    if not path.exists(image_file_path):
        print(f"Creating directory {image_file_path}")

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)
        for img_index in range(len(image_list)):
            xref = image_list[img_index][0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            output_image_folder = ""
            if image_validator(image_bytes):
                output_image_folder = path.join(image_file_path)
            else:
                output_image_folder = path.join(image_file_path, "filtered")
            # 保存图像到文件
            image_path = f'image{page_num}_{img_index}.png'
            image_path = path.join(output_image_folder, image_path)
            with open(image_path, 'wb') as image_file:
                image_file.write(image_bytes)
            print(f"Image {img_index} from page {page_num} saved as {image_path}")
    doc.close()


def extract_image_from_pdf_folder(pdf_file_folder):
    pdf_files = glob.glob(os.path.join(pdf_file_folder, '*.pdf'))
    for pdf_file in pdf_files:
        pdf_absolute_path = os.path.abspath(pdf_file)
        pdf_filename = os.path.basename(pdf_file)
        print("Extracting images from pdf file: ", pdf_filename)
        img_output_folder = os.path.join(pdf_file_folder, pdf_filename.split('.')[0].strip())
        extract_image_from_pdf(pdf_absolute_path, img_output_folder)
        print("Extracted images from pdf file: ", pdf_filename)
        print("==========================================")


def main():
    # pdf_file_folder = r'D:\Data\Papers\韩仲志\国内期刊'
    pdf_file_folder = r'D:\Data\Papers\韩仲志\国际期刊'
    extract_image_from_pdf_folder(pdf_file_folder)


if __name__ == '__main__':
    main()
