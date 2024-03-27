# DroneVehicle Annotation to LabelMe

## 1. Introduction

DroneVehicle的数据集标注格式改自PASCAL VOC标注格式，但对象框使用的是旋转后的矩形框，因此一般的标注工具无法直接使用。

- 该数据集的标注格式：`(x1, y1, x2, y2, x3, y3, x4, y4)`
- PASCAL VOC标注格式为：`(xmin, ymin, xmax, ymin)`

该代码主要用于将该数据集标注的数据转换为LabelMe标注格式的Json数据，以便使用LabelMe直接进行浏览和标注。

## 2. Code

```python
# -*- coding: utf-8 -*-
# @Time    : 2023-07-27 17:10
# @Author  : Jiang Liu
# @Desc    : DroneVehicle的数据集标注格式改自PASCAL VOC标注格式，但对象框使用的是旋转后的矩形框，因此一般的标注工具无法直接使用。
#            该代码主要用于将该数据集标注的数据转换为LabelMe标注格式的Json数据，以便使用LabelMe直接进行浏览和标注。

import os
import json
import xml.etree.ElementTree as ET
import sys
import base64


def update_progress_bar(done, total):
    if total == 0:
        return
    # 计算进度条的百分比
    percent = done / total * 100
    # 使用 \r 来清空当前行，然后输出新的内容
    sys.stdout.write('\r[%-50s] %d%%' % ('=' * int(percent / 2), percent))
    sys.stdout.flush()


def et_safe_find(root, name, default=None):
    """
    安全的查找 xml 元素
    :param root: xml 元素
    :param name: 元素名称
    :param default: 默认值
    :return: 元素的值
    """
    if root is None:
        return default
    element = root.find(name)
    if element is None:
        return default
    return element.text


def convert_file(img_file_path, xml_file_path):
    """
    将一个 xml 文件转换为 json 数据
    但特别的是，xml中object对象是多边形（使用x1y1, x2y2, ...），
    因此并非是标准的LabelImg标注格式（使用xmin, ymin, xmax, ymin标记矩形），需要特殊处理
    :param img_file_path: img 文件的路径，用于获取图片的base64格式的imageData
    :param xml_file_path: xml 文件的路径
    :return: json 数据
    """
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # 创建 json 数据结构
    json_dict = {"shapes": []}

    # 读取每一个标注框的信息
    for member in root.findall('object'):
        label = member.find('name').text
        pose = et_safe_find(member, 'pose', 'Unspecified')
        truncated = int(et_safe_find(member, 'truncated', 0))
        difficult = int(et_safe_find(member, 'difficult', 0))
        polygon = member.find('polygon')
        # 如果没有数据，就直接跳过
        if polygon is None:
            continue
        points = []
        index = 1
        while True:
            x = polygon.find('x' + str(index))
            y = polygon.find('y' + str(index))
            if x is None or y is None:
                break
            points.append([int(x.text), int(y.text)])
            index += 1

        # labelme 中的 points 是一个由坐标组成的列表，每个坐标由 [x, y] 表示
        # 我们假设 bounding box 是一个矩形，所以我们只需要四个点
        shape = {
            "label": label,
            "points": points,
            "group_id": None,
            "description": "",
            "shape_type": "polygon",
            "flags": {},
        }
        json_dict["shapes"].append(shape)

    # 读取图片的宽和高
    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)
    json_dict["imageWidth"] = width
    json_dict["imageHeight"] = height

    # 打开图片文件
    with open(img_file_path, "rb") as image_file:
        # 读取图片数据
        image_data = image_file.read()
        # 将图片数据转换为 base64 编码的字符串
        encoded_string = base64.b64encode(image_data).decode()
        json_dict["imageData"] = encoded_string

    # 获取图片文件名
    img_file_name = os.path.basename(img_file_path)
    json_dict["imagePath"] = img_file_name

    return json_dict


def convert_directory(img_folder_path, xml_folder_path, json_folder_path=None, img_suffix='jpg', debug=False):
    """
    将一个文件夹下的所有 xml 文件转换为 json 文件，每个 xml 文件对应一个 json 文件，调用 convert_file 函数实现
    :param img_folder_path: img 文件夹的路径，用于获取图片的base64格式的imageData
    :param xml_folder_path: xml 文件夹的路径
    :param json_folder_path: json 文件夹的路径，如果为 None，则默认为 xml_folder_path
    :param img_suffix: 图片文件的后缀，默认为 jpg
    :param debug: 是否打印调试信息
    :return: None
    """
    # 如果 json_folder_path 为 None，则默认为 xml_folder_path
    if json_folder_path is None:
        json_folder_path = xml_folder_path
    # 如果输出文件夹不存在，则创建
    if not os.path.exists(json_folder_path):
        os.makedirs(json_folder_path)
    total = len(os.listdir(xml_folder_path))
    if debug:
        print("xml输入文件夹:", xml_folder_path)
        print("json输出文件夹：", json_folder_path)
        print("共发现 %d 个文件" % total)
        print("开始转换...")
    # 转换失败的文件列表，以及转换失败的原因
    failed_files = []
    # 遍历 xml 文件夹下的所有 xml 文件
    index = 1
    for filename in os.listdir(xml_folder_path):
        if filename.endswith('.xml'):
            xml_file_path = os.path.join(xml_folder_path, filename)
            # 获取文件名，不包含后缀和“.”
            file_name = filename[:-4]
            img_file_path = os.path.join(img_folder_path, file_name + '.' + img_suffix)
            # 检查图片文件是否存在
            if not os.path.exists(img_file_path):
                failed_files.append({
                    "img_file_path": img_file_path,
                    "xml_file_path": xml_file_path,
                    "msg": "图片文件不存在"
                })
                continue
            json_dict = convert_file(img_file_path, xml_file_path)
            # 将文件后缀改为 .json
            json_file_name = file_name + '.json'
            # 输出文件的完整路径
            json_file_path = os.path.join(json_folder_path, json_file_name)

            with open(json_file_path, 'w') as f:
                json.dump(json_dict, f, indent=2)
        else:
            failed_files.append({
                "img_file_path": None,
                "xml_file_path": os.path.join(xml_folder_path, filename),
                "msg": "文件后缀不是 .xml"
            })
        if debug:
            update_progress_bar(index, total)
            index += 1
    if debug:
        print("\n转换完成！")
        print("成功转换 %d 个文件" % (total - len(failed_files)))
        print("失败 %d 个文件" % len(failed_files))
        print()
        if len(failed_files) > 0:
            print("====================失败文件列表以及原因====================")
            for failed_file_id, failed_file in enumerate(failed_files):
                print("第 %d 个失败文件：" % (failed_file_id + 1))
                if failed_file["img_file_path"] is not None:
                    print("图片文件路径：%s" % failed_file["img_file_path"])
                print("xml文件路径：%s" % failed_file["xml_file_path"])
                print("失败原因：%s" % failed_file["msg"])
                print("=========================================================")
                print()


def main():
    img_folder_path = r"D:\Environments\Library\Datasets\VisDrone\DroneVehicle\train\trainimg"
    xml_folder_path = r"D:\Environments\Library\Datasets\VisDrone\DroneVehicle\train\trainlabel"
    json_folder_path = r"D:\Environments\Library\Datasets\VisDrone\DroneVehicle\train\trainlabel-json"
    convert_directory(img_folder_path, xml_folder_path, json_folder_path, debug=True, img_suffix='jpg')


if __name__ == '__main__':
    main()
```