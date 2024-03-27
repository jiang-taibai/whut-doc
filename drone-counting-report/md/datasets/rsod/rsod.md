# RSOD Dataset

## 1. 介绍

RSOD（Remote Sensing Object
Detection）数据集发布页：[https://github.com/RSIA-LIESMARS-WHU/RSOD-Dataset-](https://github.com/RSIA-LIESMARS-WHU/RSOD-Dataset-)

是一个用于遥感图像中物体检测的开放数据集。该数据集包括飞机、油罐、游乐场和立交桥。

![rsod-datasets-preview](https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/rsod/rsod-datasets-preview.png)

## 2. 链接

百度网盘：[https://pan.baidu.com/s/1ile12hRi32zzW1zl7vzDoQ?pwd=cvlj](https://pan.baidu.com/s/1ile12hRi32zzW1zl7vzDoQ?pwd=cvlj)

## 3. 数据集说明

### 3.1 数据集统计

该数据集包括4个文件，每个文件针对一种对象。

| 子数据集             | 对象数量            | 图片数量 |
|------------------|-----------------|------|
| aircraft dataset | 4993 aircrafts  | 446  |
| playground       | 191 playgrounds | 189  |
| overpass         | 180 overpasses  | 176  |
| oiltank          | 1586 oiltanks   | 165  |

### 3.2 目录结构

```text
RSOD-Datasets/
├─aircraft
│  ├─Annotation
│  │  ├─labels
│  │  └─xml
│  └─JPEGImages
├─oiltank
│  ├─Annotation
│  │  ├─labels
│  │  └─xml
│  └─JPEGImages
├─overpass
│  ├─Annotation
│  │  ├─labels
│  │  └─xml
│  └─JPEGImages
└─playground
    ├─Annotation
    │  ├─labels
    │  └─xml
    └─JPEGImages
```

### 3.2 标注格式

数据集采用PASCAL VOC格式标注，放置在`class_name/Annotation/xml`目录下。

同时该数据集将标注的关键信息放置在了`class_name/Annotation/labels`目录下，每个文件包含一行，格式如下：

```text
aircraft_4.jpg aircraft 937 85 1033 160
aircraft_4.jpg aircraft 741 484 813 550
aircraft_4.jpg aircraft 223 538 304 598
```

## Citation

Please cite our papers if the dataset is useful for you. Thank you!

```text
[1] Y. Long, Y. Gong, Z. Xiao and Q. Liu, "Accurate Object Localization in Remote Sensing Images Based on Convolutional Neural Networks," in IEEE Transactions on Geoscience and Remote Sensing, vol. 55, no. 5, pp. 2486-2498, May 2017. doi: 10.1109/TGRS.2016.2645610, link
[2] Z Xiao, Q Liu, G Tang, X Zhai, "Elliptic Fourier transformation-based histograms of oriented gradients for rotationally invariant object detection in remote-sensing images", International Journal of Remote Sensing, vol. 36, no. 2, 2015
```

