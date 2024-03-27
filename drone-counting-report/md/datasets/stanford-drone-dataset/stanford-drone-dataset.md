# SDD Dataset

## 1. SDD(Stanford Drone Dataset) 数据集介绍

数据集官网：[https://cvgl.stanford.edu/projects/uav_data/](https://cvgl.stanford.edu/projects/uav_data/)

当人们在拥挤的空间，如大学校园或繁忙街道的人行道上行走时，他们会遵循基于社交礼仪的常识规则。
为了能够设计出可以充分利用这些规则以更好地解决如目标跟踪或轨迹预测等任务的新算法，我们需要获得更好的数据。
为此，我们提供了（据我们所知）第一个大规模数据集，
收集了在真实世界的室外环境（如大学校园）中行驶的各种类型的代理（不仅有行人，还有自行车骑行者，滑板运动员，汽车，公交车和高尔夫球车）的图像和视频。

在下面的图片中，行人用粉红色标注，自行车骑行者用红色标注，滑板运动员用橙色标注，汽车用绿色标注。

![stanford-drone-dataset-preview](https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/stanford-drone-dataset/stanford-drone-dataset-preview.jpg)

## 2. 数据集链接

直接下载链接：[Stanford Campus Dataset ~ 69 G](http://vatic2.stanford.edu/stanford_campus_dataset.zip)

OpenDataLab 平台提供了完整的数据集信息、直观的数据分布统计、流畅的下载速度、便捷的可视化脚本：[OpenDataLab-StanfordDrone](https://opendatalab.org.cn/Stanford_Drone)

## 3. 数据集统计

|   Scenes    | Videos | Bicyclist | Pedestrian | Skateboarder | Cart | Car   | Bus  |
|:-----------:|--------|-----------|------------|--------------|------|-------|------|
|    gates    | 9      | 51.94     | 43.36      | 2.55         | 0.29 | 1.08  | 0.78 |
|   little    | 4      | 56.04     | 42.46      | 0.67         | 0    | 0.17  | 0.67 |
|    nexus    | 12     | 4.22      | 64.02      | 0.60         | 0.40 | 29.51 | 1.25 |
|    coupa    | 4      | 18.89     | 80.61      | 0.17         | 0.17 | 0.17  | 0    |
|  bookstore  | 7      | 32.89     | 63.94      | 1.63         | 0.34 | 0.83  | 0.37 |
| deathCircle | 5      | 56.30     | 33.13      | 2.33         | 3.10 | 4.71  | 0.42 |
|    quad     | 4      | 12.50     | 87.50      | 0            | 0    | 0     | 0    |
|    hyang    | 15     | 27.68     | 70.01      | 1.29         | 0.43 | 0.50  | 0.09 |

## 4. 数据集格式

### (1) 文件目录结构

```text
Stanford Drone dataset
├── README
├── annotations                     # annotations: 标注，标注文件与数据集的目录结构一一对应
│   ├── bookstore                   # bookstore: 以不同场景区分视频
│   │   ├── video0
│   │   │   ├── annotations.txt
│   │   │   └── reference.jpg       # reference.jpg: 视频样例图片
│   │   ├── video1
│   │   │   ├── annotations.txt
│   │   │   └── reference.jpg
│   │   └── ...
│   ├── coupa
│   │   ├── video0
│   │   │   ├── annotations.txt
│   │   │   └── reference.jpg
│   │   ├── video1
│   │   │   ├── annotations.txt
│   │   │   └── reference.jpg
│   │   └── ...
│   └── ...
└── videos                          # videos: 数据集
    ├── bookstore
    │   ├── video0
    │   │   └── video.mov
    │   ├── video1
    │   │   └── video.mov
    │   └── ...
    ├── coupa
    │   ├── video0
    │   │   └── video.mov
    │   ├── video1
    │   │   └── video.mov
    │   └── ...
    └── ...
```

### (2) 标注文件格式

```text
0 211 1038 239 1072 10005 1 0 1 "Biker"
0 211 1038 239 1072 10006 1 0 1 "Biker"
0 211 1038 239 1072 10007 1 0 1 "Biker"
11 314 566 356 621 10336 1 0 1 "Pedestrian"
11 314 566 356 621 10337 1 0 1 "Pedestrian"
11 314 566 356 621 10338 1 0 1 "Pedestrian"
72 530 510 581 568 10000 0 0 0 "Cart"
72 528 510 579 568 10001 0 0 1 "Cart"
72 528 510 579 568 10002 0 0 1 "Cart"
72 528 510 579 568 10003 0 0 1 "Cart"
```

```text
标注文件内容从左到右的字段对应以下由上到下的字段：

Track ID: 目标 ID ，同一跟踪目标有唯一的目标 ID
xmin: 标注框左上的 x 坐标
ymin: 标注框左上的 y 坐标
xmax: 标注框右下的 x 坐标
ymax: 标注框右下的 y 坐标
frame: 该标注对应的帧号
lost: 是否丢失，如果为1则目标在视野范围外
occluded: 是否有遮挡，如果为1则目标有遮挡
generated: 是否生成的标注，如果为1则该标注是通过自动插值生成的
label: 该目标对应的类别
```


## Citation

If you find this dataset useful, please cite this paper (and refer the data as Stanford Drone Dataset or SDD):

```
A. Robicquet, A. Sadeghian, A. Alahi, S. Savarese, Learning Social Etiquette: Human Trajectory Prediction In Crowded Scenes in European Conference on Computer Vision (ECCV), 2016.
```