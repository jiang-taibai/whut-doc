# VisDrone DroneAnimal

## 1. 数据集简介

> 官网：[https://github.com/VisDrone/AnimalDrone](https://github.com/VisDrone/AnimalDrone)
>
> 《基于图正则化流注意力网络的无人机动物视频计数》（Graph Regularized Flow Attention Network for Video Animal Counting From
> Drones）
> - Published: 28 May 2021
> - Link: [https://ieeexplore.ieee.org/document/9444151](https://ieeexplore.ieee.org/document/9444151)
> - DOI: 10.1109/TIP.2021.3082297

![drone-animal-introduction](https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/vis-drone/drone-animal-introduction.jpg)

本文提出一个由无人机收集的大规模动物计数视频数据集(AnimalDrone)，用于农业和野生动物保护。

该数据集由两个子集组成，即由我们自己的无人机现场捕获的AnimalDrone-PartA和从互联网收集的AnimalDrone-PartB。
总共有53644帧，400多万物体标注和密度、高度和视角等属性。

开发了一种图正则化流注意力网络(GFAN)，用于在任意人群密度、视角和飞行高度的无人机捕获的密集视频片段中执行密度图估计。

具体而言，GFAN方法利用光流对连续帧中的多尺度特征图进行扭曲以保证时间一致性，然后结合增强特征来预测密度图。

此外，对多个邻域框架的密度图进行图正则化，进一步增强时序关系。

提出了一种新的多粒度损失函数，包括像素级密度损失和区域级计数损失，以强制网络专注于不同密度的不同场景中不同尺度目标的可区分特征。

进行了详细的定量研究，并与最新的计数算法进行了比较，验证了所提方法的有效性。

![drone-animal-datasets-preview](https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/vis-drone/drone-animal-datasets-preview.jpg)

## 2. 数据集链接

百度网盘: [https://pan.baidu.com/s/1v5pL0URmgHx_Z67-oWrhuA?pwd=cvlj](https://pan.baidu.com/s/1v5pL0URmgHx_Z67-oWrhuA?pwd=cvlj)

文件结构如下：

```text
.
├── AnimalDrone-PartA
│   ├── jpg-test.zip
│   ├── jpg-train.zip
│   ├── mat-test.zip
│   └── mat-train.zip
└── AnimalDrone-PartB
    ├── annotation.zip
    ├── jpg.zip
    ├── jpg2.zip
    ├── jpg3.zip
    └── jpg4.zip
```

备注：AnimalDrone-PartA由作者的无人机现场捕获，AnimalDrone-PartB来自互联网收集

## 3. 数据集格式

### 3.1 PartA

该数据集标注均为.mat格式，包含location和number两个字段，分别表示目标的位置和数量。

```matlab
>> disp(mat.result{1, 1})
    location: [43×2 double]
      number: 43
```

### 3.2 PartB

(1) 数据集介绍

该数据集来源于互联网，每个视频段含有帧数个jpg图像和xml标注文件。

每个标注文件为标准的PASCAL VOC格式（详见[PASCAL VOC 标注格式](/md/annotations/pascal-voc.md)）

(2) 数据集文件结构

每个标注文件集合对应一个视频段，名称为{场景序号}-cut{视频段序号}，例如023-cut7表示第23个场景的第7个视频段。

每个标注文件集合包含多个标注文件，每个标注文件对应一个jpg图像，文件名相同。

```text
├─annotation
│  ├─003-cut01
│  │  └─Annotations
│  ├─{场景序号}-cut{视频段序号}
│  │  └─Annotations
│  └─023-cut7
│      └─Annotations
└─jpg
    ├─003
    │  ├─cut1
    │  ├─...
    │  └─cut27
    ├─...
    └─023
        ├─cut1
        ├─...
        └─cut7
```

(3) 数据集标注规范

为标准的PASCAL VOC格式（详见[PASCAL VOC 标注格式](/md/annotations/pascal-voc.md)）


## 4. 其他信息

### (1) 版权信息

```
@article{zhu2021graph,
  title={Graph Regularized Flow Attention Network for Video Animal Counting from Drones},
  author={Zhu, Pengfei and Peng, Tao and Du, Dawei and Yu, Hongtao and Zhang, Libo and Hu, Qinghua},
  journal={IEEE Transactions on Image Processing},
  year={2021},
  publisher={IEEE}
}
```