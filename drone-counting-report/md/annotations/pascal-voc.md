# PASCAL VOC 标注格式

PASCAL Visual Object Classes (VOC)是一个用于目标检测的基准数据集，包括20个物体类别。这个数据集以其XML标注格式而闻名，通常被用于物体识别和图像分割等任务。下面我们详细地介绍一下PASCAL
VOC的标注格式。

## 1. 格式说明

PASCAL VOC标注的格式是XML，其中包含了图像的相关信息以及图像中物体的标注信息。一个典型的PASCAL VOC XML标注文件的结构如下：

```xml
<annotation>
    <folder>图片所在文件夹</folder>
    <filename>图片名称</filename>
    <source>
        <database>来源数据库</database>
        <annotation>标注来源</annotation>
        <image>图像来源</image>
    </source>
    <size>
        <width>图像宽度</width>
        <height>图像高度</height>
        <depth>图像深度</depth>
    </size>
    <segmented>是否用于分割</segmented>
    <object>
        <name>物体名称</name>
        <pose>物体姿态</pose>
        <truncated>物体是否被截断</truncated>
        <difficult>物体是否难以识别</difficult>
        <bndbox>
            <xmin>物体包围框左上角的x坐标</xmin>
            <ymin>物体包围框左上角的y坐标</ymin>
            <xmax>物体包围框右下角的x坐标</xmax>
            <ymax>物体包围框右下角的y坐标</ymax>
        </bndbox>
    </object>
    <object>
        ...
    </object>
</annotation>
```

## 2. 标注工具

创建并导出PASCAL VOC格式的标注数据可以通过多种标注工具来完成，这些工具通常提供了一个图形用户界面，使得用户能够在图像上直观地绘制包围框，并为其分配类别。以下是一些常见的标注工具：

1. **LabelImg**：这是一个用Python和Qt构建的图形图像标注工具，它支持PASCAL
   VOC和YOLO两种格式的标注数据。LabelImg提供了基础的标注功能，如创建和删除包围框，改变包围框的大小，复制和粘贴包围框，以及撤销和重做操作。

2. **VGG Image Annotator (VIA)**
   ：这是一个由牛津大学视觉几何组（VGG）开发的项目，支持标注图片、音频和视频文件。VIA提供了多种形状的标注，包括矩形、圆形、多边形和线段，可以满足各种标注需求。然而，你需要自行转换VIA的标注数据到PASCAL
   VOC格式。

3. **Labelbox**：这是一个强大的标注平台，可以在线协作标注数据，支持多种类型的数据，如图像、视频和文本。Labelbox提供了一些高级特性，如自动标注和标注质量控制。导出的标注数据可以自定义格式，包括PASCAL
   VOC格式。

4. **RectLabel**：这是一个专为Mac用户设计的标注工具，支持创建矩形和多边形的标注。RectLabel还可以集成苹果的Create
   ML，实现标注和模型训练的无缝对接。导出的标注数据支持PASCAL VOC和YOLO两种格式。
