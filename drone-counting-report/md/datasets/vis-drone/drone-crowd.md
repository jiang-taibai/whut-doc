# VisDrone DroneCrowd

## 1. 数据集简介

> 官网：[https://github.com/VisDrone/DroneCrowd](https://github.com/VisDrone/DroneCrowd)
>
> 《检测、跟踪和计数遇到人群中的无人机:一个基准》（Detection, Tracking, and Counting Meets Drones in Crowds: A Benchmark）
> - Published: 18 April 2022
> -
Link: [Detection, Tracking, and Counting Meets Drones in Crowds: A Benchmark.pdf](https://openaccess.thecvf.com/content/CVPR2021/papers/Wen_Detection_Tracking_and_Counting_Meets_Drones_in_Crowds_A_Benchmark_CVPR_2021_paper.pdf)
> - DOI: xxx

![drone-crowd-datasets-preview](https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/vis-drone/drone-crowd-datasets-preview.png)

本文提出一种时空多尺度注意力网络(STANet)来解决任意人群密度、视角和飞行高度的无人机捕获的密集人群视频片段的密度图估计、定位和跟踪问题。

STANet方法在连续帧中聚合多尺度特征图以利用时间一致性，然后预测密度图，定位目标并同时关联它们。
设计了一个由粗到细的过程，逐步将注意力模块应用于聚合的多尺度特征图，以强制网络利用具有判别力的时空特征以获得更好的性能。

整个网络采用端到端的多任务损失进行训练，多任务损失由密度图损失、定位损失和关联损失3项组成。 采用非极大值抑制和最小代价流框架生成场景中目标的轨迹。

由于现有的人群计数数据集只关注静态摄像机中的人群计数，而不是密度图估计、计数和跟踪无人机上的人群，
本文收集了一个新的基于无人机的大规模数据集droneccrowd，由70个不同场景中捕获的112个视频片段组成，具有33,600个高分辨率帧(
即1920x1080)。

经过大量的努力，该数据集提供了20,800人的轨迹，具有480万个头部注释和序列中的几个视频级属性。
在Shanghaitech、UCF-QNRF和droneccrowd这两个具有挑战性的公开数据集上进行了大量实验，结果表明STANet取得了较好的性能。

## 2. 数据集链接

- ECCV2020挑战

VisDrone 2020人群计数挑战要求参与算法对每帧中的人数进行计数。
该挑战将提供112个具有挑战性的序列，包括82个用于训练的视频序列(总共2420帧)和30个用于测试的序列(总共900帧)，这些可在下载页面上获得。
我们用每个视频帧中的点手动标注人物。

- DroneCrowd(完整版本)

这个完整的版本由112个视频片段组成，具有33,600个高分辨率帧(即1920x1080)，在70个不同的场景中捕获。
经过大量的努力，该数据集提供了20,800人的轨迹，具有480万个头部注释和序列中的几个视频级属性。

百度网盘: [https://pan.baidu.com/s/1emeAej8ShBFIYLI8LGQZuw?pwd=cvlj](https://pan.baidu.com/s/1emeAej8ShBFIYLI8LGQZuw?pwd=cvlj)

- ECCV2020挑战：VisDrone2020-CC.zip
- DroneCrowd(完整版本)：DroneCrowd-FullVersion/

## 3. 数据集格式

### 3.1 数据集描述

1. 该数据集由训练集(82个序列)和测试集(30个序列)组成。`train.txt`和`test.txt`中的每一行都是序列的索引。

2. 将序列转换为训练集、val集和测试集中连续的帧，记为`img{seqID:%03d}{frID:%03d}.jpg`图像。例如，`img001001.jpg`表示第`001`
   序列中的第`001`帧。注意，val集是从测试集采样的。

3. 原始的标注信息保存在`.xml`格式中。为了方便，我们可以通过`xml2mat.m`函数生成对应的.mat格式的真值标注。
   在每一行中，点的顺序是`frame, id, xmin, ymin, xmax, ymax`。
   此外，位于`ground-truth`文件夹中的`GT_img*.mat`标注与Shanghaitech数据集一致。
   点的顺序是`x, y, id`，这是通过`saveGT.m`函数生成的。

4. 真值密度图和定位图分别由`make_data_density.py`和`make_data_localization.py`生成，用于网络训练。

### 3.2 数据集文件格式

每一个xml文件对应一个视频序列，例如在本例中`00001.xml`对应`img001001.jpg~img001300.jpg`。

每个xml文件中的`<track>`标签对应一个目标，例如在本例中`<track id="0" label="human">`对应`img001001.jpg`中的一个目标。

每个`<track>`标签中的`<box>`
标签对应一个目标在某一帧中的位置，例如在本例中`<box frame="0" xtl="737" ytl="582" xbr="757" ybr="602" outside="0" occluded="0"></box>`
对应`img001001.jpg`中的一个目标的位置。

```xml
<annotations count="145">
    <track id="0" label="human">
        <box frame="0" xtl="737" ytl="582" xbr="757" ybr="602" outside="0" occluded="0"/>
        ...
        <box frame="299" xtl="666" ytl="680" xbr="687" ybr="701" outside="0" occluded="0"/>
    </track>
    ...
    <track id="144" label="human">
        <box frame="0" xtl="696" ytl="617" xbr="716" ybr="637" outside="0" occluded="0"/>
        ...
        <box frame="299" xtl="450" ytl="665" xbr="471" ybr="686" outside="0" occluded="0"/>
    </track>
</annotations>
```

### 3.3 数据集的制作

1. 从原始的数据集中提取出每个视频序列的帧，保存在`images`文件夹中。
2. 使用工具进行数据标注，导出保存在`annotations`文件夹中。

对于视频的多目标标注，有一些工具可以帮助我们完成这项任务：

1. **CVAT (Computer Vision Annotation Tool)**
   ：CVAT是一个开源的在线视频和图像标注工具，由Intel开发。它支持多种标注类型，包括边界框、多边形、折线和点。CVAT也支持自动标注和跨帧插值，这对于视频标注非常有用。

2. **VATIC (Video Annotation Tool from Irvine, California)**
   ：VATIC是一个在线的视频标注工具，由加利福尼亚大学欧文分校开发。它支持跨帧插值和自动标注，可以用于多目标跟踪和行为识别任务。

3. **Labelbox**：Labelbox是一个商业的在线标注平台，支持视频和图像标注。它提供了一个直观的用户界面和丰富的标注类型，包括边界框、多边形、折线和点。

4. **Anvil**：Anvil是一个开源的视频标注工具，支持多种标注类型，包括边界框、多边形、折线和点。Anvil也支持自动标注和跨帧插值。

5. **VGG Image Annotator VIA**：VIA是由牛津大学视觉几何组开发的一个在线标注工具，支持图像和视频标注。VIA提供了丰富的标注类型，包括边界框、多边形、折线和点。

## 4. 其他信息

### (1) 相关代码

- Space-Time Neighbor-Aware Network (
  STNNet-pytorch): [https://github.com/VisDrone/DroneCrowd/tree/master/STNNet](https://github.com/VisDrone/DroneCrowd/tree/master/STNNet)
- Space-Time Multi-Scale Attention Network (
  STANet-pytorch): [https://github.com/VisDrone/DroneCrowd/tree/master/STANet](https://github.com/VisDrone/DroneCrowd/tree/master/STANet)

### (2) 版权信息

```
@inproceedings{dronecrowd_cvpr2021,
  author    = {Longyin Wen and
               Dawei Du and
               Pengfei Zhu and
               Qinghua Hu and
               Qilong Wang and
               Liefeng Bo and
               Siwei Lyu},
  title     = {Detection, Tracking, and Counting Meets Drones in Crowds: A Benchmark},
  booktitle = {CVPR},
  year      = {2021}
}
```

```
@article{zhu2021graph,
  title={Graph Regularized Flow Attention Network for Video Animal Counting from Drones},
  author={Zhu, Pengfei and Peng, Tao and Du, Dawei and Yu, Hongtao and Zhang, Libo and Hu, Qinghua},
  journal={IEEE Transactions on Image Processing},
  year={2021},
  publisher={IEEE}
}
```