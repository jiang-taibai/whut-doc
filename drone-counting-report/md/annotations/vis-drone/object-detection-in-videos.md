# Object Detection in Videos

## 1. 概述

官网：[https://github.com/VisDrone/VisDrone2018-VID-toolkit](https://github.com/VisDrone/VisDrone2018-VID-toolkit)

- 来源：视频检测 (VID) 竞赛的 VisDrone2018 竞赛开发套件的文档。
- 格式说明：基于PASCAL VOC[1]和MS-COCO[2]平台进行了修改。
- 工具包：代码在Windows 10和macOS Sierra 10.12.6系统上，Matlab 2013a/2014b/2016b/2017b平台上进行了测试。
- 数据集：对于VID竞赛，存在三组数据和标签：训练数据、验证数据和测试挑战数据。三组之间没有重叠。

## 2. 工具包介绍

evalVID.m 是评估您的探测器的主要函数:

- 修改数据集路径和结果路径
- 使用“isSeqDisplay”显示真实值和检测结果

## 3. 标注介绍

每一个标注文件对应一个图像，文件名相同。

每个标注文件`x.txt`含有若干行，每一行格式如下：

```text
<frame_index>,<target_id>,<bbox_left>,<bbox_top>,<bbox_width>,<bbox_height>,<score>,<object_category>,<truncation>,<occlusion>
# 例如
214,0,0,131,45,25,1,4,1,0
98,1,739,0,50,23,1,4,0,0
99,1,739,55,49,23,1,4,0,0
100,1,736,109,49,26,1,4,0,0
101,1,734,121,48,24,1,4,0,0
102,1,733,121,48,24,1,4,0,0
```

| Name                | Description                                                                                                                                             |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<frame_index>`     | 视频帧的帧索引                                                                                                                                                 |
| `<target_id>`       | 在检测结果文件中，目标的身份应该设置为常数-1。在GROUNDTRUTH文件中，利用目标的身份提供不同帧中边界框的时间对应关系。                                                                                        |
| `<bbox_left>`       | 预测边界框左上角的x坐标                                                                                                                                            |
| `<bbox_top>`        | 预测对象边界框左上角的y坐标                                                                                                                                          |
| `<bbox_width>`      | 预测对象边界框的像素宽度                                                                                                                                            |
| `<bbox_height>`     | 预测对象边界框的高度，单位为像素                                                                                                                                        |
| `<score>`           | 检测文件中的分数表示包含对象实例的预测边界框的置信度。GROUNDTRUTH文件中的分数设置为1或0。1表示计算时考虑边界框，0表示忽略边界框。                                                                                |
| `<object_category>` | 对象类别表示被标注对象的类型(即被忽略的区域(0)，pedestrian(1)， people(2)， bicycle(3)， car(4)， van(5)， truck(6)， tricycle(7)， awn -tricycle(8)， bus(9)， motor(10)， others(11)) |
| `<truncation>`      | 检测结果文件中的分数应该设置为常数-1。GROUNDTRUTH文件中的分数表示对象部分出现在帧外的程度(即没有截断= 0(截断率0%)，部分截断= 1(截断率1% ~ 50%))。                                                              |
| `<occlusion>`       | 检测文件中的得分应该设置为常数-1。GROUNDTRUTH文件中的分数表示对象被遮挡的比例(即无遮挡= 0(遮挡率0%)，部分遮挡= 1(遮挡率1% ~ 50%)，重度遮挡= 2(遮挡率50% ~ 100%))。                                              |

## 4. 版权信息

If you use our toolkit or dataset, please cite our paper as follows:

```text
@article{zhuvisdrone2018,
    title={Vision Meets Drones: A Challenge},
    author={Zhu, Pengfei and Wen, Longyin and Bian, Xiao and Haibin, Ling and Hu, Qinghua},
    journal={arXiv preprint:1804.07437},
    year={2018}
}
```