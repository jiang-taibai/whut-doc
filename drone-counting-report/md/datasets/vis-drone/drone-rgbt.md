# VisDrone DroneRGBT

## 1. 数据集简介

> 官网：[https://github.com/VisDrone/DroneRGBT](https://github.com/VisDrone/DroneRGBT)
>
> 《来自无人机的RGB-T人群计数:基准和MMCCN网络》（RGB-T Crowd Counting from Drone: A Benchmark and MMCCN Network）
> - Published: 2020
> - PDF
    Link: [RGB-T Crowd Counting from Drone: A Benchmark and MMCCN Network](https://openaccess.thecvf.com/content/ACCV2020/papers/Peng_RGB-T_Crowd_Counting_from_Drone_A_Benchmark_and_MMCCN_Network_ACCV_2020_paper.pdf)
> - DOI: xxx

人群计数旨在识别物体的数量，在智能交通、城市管理和安防监控中发挥着重要作用。

由于尺度变化、光照变化、遮挡和成像条件差，特别是在夜间和雾霾条件下，人群计数任务具有很大的挑战性。

本文提出了一个基于无人机的rgb-热人群计数数据集DroneRGBT (drone based RGB-Thermal crowd counting dataset)，
由3600对图像组成，涵盖了不同的属性，包括高度、光照和密度。

为了利用可见光和热红外模态的互补信息，本文提出了一种多模态人群计数网络(multi-modal crowd counting network, MMCCN)，
该网络包含多尺度特征学习模块、模态对齐模块和自适应融合模块。在DroneRGBT数据集上的实验验证了该方法的有效性。

![drone-rgbt-datasets-preview](https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/vis-drone/drone-rgbt-datasets-preview.jpg)

## 2. 数据集链接

百度网盘: [https://pan.baidu.com/s/1KbrSyOD7fyD_wHZ7VhS6AQ?pwd=cvlj](https://pan.baidu.com/s/1KbrSyOD7fyD_wHZ7VhS6AQ?pwd=cvlj)

下图为相关代码的架构图
![drone-rgbt-code-structure](https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/vis-drone/drone-rgbt-code-structure.jpg)

## 3. 数据集格式

### (1) 数据集文件结构

文件结构如下：

```text
DroneRGBT
├─Test
│  ├─GT_        标注文件xml
│  ├─Infrared   红外图像
│  ├─RGB        可见光图像
│  └─shisih     10张红外示例图像和示例标注
└─Train
    ├─GT_       标注文件xml
    ├─Infrared  红外图像
    └─RGB       可见光图像
```

### (2) 数据集标注对应关系

每个标注文件均为PASCAL VOC格式的xml文件，包含了图像的宽度、高度、通道数、目标类别、目标位置等信息。

其对应的两种图像文件名序号相同，分别为可见光RGB图像和红外图像。

例如`/Test/GT_/1R.xml`对应于`/Test/RGB/1.jpg`和`/Test/Infrared/1R.jpg`。

## 4. 其他信息

### (1) 版权信息

```
@InProceedings{Peng_2020_ACCV,
    author    = {Peng, Tao and Li, Qing and Zhu, Pengfei},
    title     = {RGB-T Crowd Counting from Drone: A Benchmark and MMCCN Network},
    booktitle = {Proceedings of the Asian Conference on Computer Vision (ACCV)},
    month     = {November},
    year      = {2020}
}
```