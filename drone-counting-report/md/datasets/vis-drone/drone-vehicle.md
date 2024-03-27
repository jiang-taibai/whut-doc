# VisDrone DroneVehicle

## 1. 数据集简介

> 官网：[https://github.com/VisDrone/DroneVehicle](https://github.com/VisDrone/DroneVehicle)
>
> 《基于不确定性学习的无人机RGB-红外跨模态车辆检测》（Drone-Based RGB-Infrared Cross-Modality Vehicle Detection Via
> Uncertainty-Aware Learning）
> - Published: 18 April 2022
> - Link: [https://ieeexplore.ieee.org/document/9759286](https://ieeexplore.ieee.org/document/9759286)
> - DOI: 10.1109/TPAMI.2021.3119563

基于无人机的车辆检测旨在发现航拍图像中车辆的位置和类别。它为智慧城市交通管理和灾难救援赋能。

研究人员在这一领域做出了大量努力，并取得了相当大的进展。然而，在物体难以分辨的情况下，特别是在弱光条件下，这仍然是一个挑战。

为了解决这个问题，构建了一个大规模的基于无人机的rgb -红外车辆检测数据集DroneVehicle。

无人机收集了28,439对rgb -红外图像，从白天到晚上覆盖了城市道路、居民区、停车场和其他场景。

由于RGB图像与红外图像之间存在较大差距，跨模态图像在提供有效信息的同时也提供了冗余信息。
为解决这一难题，本文进一步提出一种不确定性感知的跨模态车辆检测(UA-CMDet)框架，从跨模态图像中提取互补信息，可以显著提高低光照条件下的检测性能。
设计一个不确定性感知模块(UAM)，通过跨模态交并比(IoU)和RGB光照值来量化每个模态的不确定性权重。

此外，设计了一种光照感知的跨模态非极大值抑制算法，以在推理阶段更好地融合模态特定信息。
在无人机数据集上的大量实验验证了所提方法在跨模态车辆检测方面的灵活性和有效性。

![drone-vehicle-datasets-preview](https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/vis-drone/drone-vehicle-datasets-preview.png)

无人机数据集由无人机收集的共56878张图像组成，其中一半为RGB图像，其余为红外图像。

我们为这五个类别用定向边界框做了丰富的注释，包括汽车、卡车、公共汽车、面包车和货车。

|     类别      | RGB图像标注 | 红外图像标注  |
|:-----------:|:-------:|:-------:|
|     car     | 389779条 | 428086条 |
|    truck    | 22123条  | 25960条  |
|     bus     | 15333条  | 16590条  |
|     van     | 11935条  | 12708条  |
| freight car | 13400条  | 17173条  |

在“无人机”中，为了标注图像边界上的对象，我们在每个图像的上、下、左、右设置一个宽度为100像素的白色边框，这样下载的图像比例为`840x712`。

在训练我们的检测网络时，我们可以进行预处理以删除周围的白色边框并将图像尺度更改为`640x512`。

## 2. 数据集链接

百度网盘: [https://pan.baidu.com/s/1i2uMywj-UV3DgQ8XjmXohg?pwd=cvlj](https://pan.baidu.com/s/1i2uMywj-UV3DgQ8XjmXohg?pwd=cvlj)

包含以下文件：

- Train: train.zip
- Validation: val.zip
- Test: test.zip

## 3. 数据集格式

### 3.1 数据集目录结构

分为训练集、验证集和测试集，每个集合中包含RGB图、红外图、RGB图的标注信息、红外图的标注信息。

```
D:.
│  
├─test
│  ├─testimg
│  │      00001.jpg
│  │      ...
│  │      08980.jpg
│  │      
│  ├─testimgr
│  │      00001.jpg
│  │      ...
│  │      08980.jpg
│  │      
│  ├─testlabel
│  │      00001.xml
│  │      ...
│  │      08980.xml
│  │      
│  └─testlabelr
│          00001.xml
│          ...
│          08980.xml
│          
├─train
│  ├─trainimg
│  │      00001.jpg
│  │      ...
│  │      17990.jpg
│  │      
│  ├─trainimgr
│  │      00001.jpg
│  │      ...
│  │      17990.jpg
│  │      
│  ├─trainlabel
│  │      00001.xml
│  │      ...
│  │      17990.xml
│  │      
│  └─trainlabelr
│          00001.xml
│          ...
│          17990.xml
│          
└─val
    ├─valimg
    │      00001.jpg
    │      ...
    │      01469.jpg
    │      
    ├─valimgr
    │      00001.jpg
    │      ...
    │      01469.jpg
    │      
    ├─vallabel
    │      00001.xml
    │      ...
    │      01469.xml
    │      
    └─vallabelr
            00001.xml
            ...
            01469.xml
```

### 3.2 数据集标注格式

每一个xml文件对应一张图片，这里用数据集中"/test/testlabel/00001.xml"举例，格式如下：

```xml

<annotation>
    <folder>5-11</folder>
    <filename>DJI_0458</filename>
    <path>E:\program\ProcessedData-20190617.part\5-11\DJI_0458.jpg</path>
    <source>
        <database>Unknown</database>
    </source>
    <size>
        <width>840</width>
        <height>712</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
    <object>
        <name>car</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <polygon>
            <x1>574</x1>
            <y1>395</y1>
            <x2>604</x2>
            <y2>393</y2>
            <x3>606</x3>
            <y3>469</y3>
            <x4>578</x4>
            <y4>466</y4>
        </polygon>
    </object>
</annotation>
```

不同的是，这里的标注使用的是多边形标注，而不是矩形标注。

### 3.3 数据集的使用

(1) 第一步：将xml文件转换为json文件

> [!NOTE]
> 该XML中的Object对象使用的是多边形标注，但调研后得知大部分支持多边形标注的直接导出的一般为json或其他格式。

具体代码实现：[DroneVehicle Annotation to LabelMe](md/codes/drone-vehicle-annotation2labelme.md)

(2) 第二步：可将json数据放入模型中训练

## 4. 其他信息

### (1) 相关代码

- [UA-CMDet](https://github.com/SunYM2020/UA-CMDet)

### (2) 版权信息

```
@ARTICLE{sun2020drone,
  title={Drone-based RGB-Infrared Cross-Modality Vehicle Detection via Uncertainty-Aware Learning}, 
  author={Sun, Yiming and Cao, Bing and Zhu, Pengfei and Hu, Qinghua},
  journal={IEEE Transactions on Circuits and Systems for Video Technology}, 
  year={2022},
  volume={},
  number={},
  pages={1-1},
  doi={10.1109/TCSVT.2022.3168279}
}
```