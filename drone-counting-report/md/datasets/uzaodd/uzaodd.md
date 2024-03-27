# UZAODDataset

## 1. 简介

Link: [https://www.kaggle.com/datasets/sganderla/urban-zone-aerial-object-detection-dataset](https://www.kaggle.com/datasets/sganderla/urban-zone-aerial-object-detection-dataset)

UZAODDataset(Urban Zone Aerial Object Detection Dataset)作为创建对象检测模型的基础，该数据集专注于城市地区的航空图像。

它包含 4 个对象类的 187,138 个图像和超过 4,112,482 个带注释的对象，因为对象注释位于 YOLOv5 类型上。

该数据集是其他 3 个数据集的组合，即Stanford Drone Dataset、Vision Meets Drones 和 Umanned Unmanned Aerial Vehicles
Benchmark Object Inspection and Tracking。

该数据集包含以下目标对象：人、小型车辆、中型车辆和大型车辆。

![uzaodd-datasets-preview](https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/uzaodd/uzaodd-datasets-preview.png)

## 2. 链接

HTTP下载：[https://www.kaggle.com/datasets/sganderla/urban-zone-aerial-object-detection-dataset/download?datasetVersionNumber=1](https://www.kaggle.com/datasets/sganderla/urban-zone-aerial-object-detection-dataset/download?datasetVersionNumber=1)

## 3. 数据集说明

### 3.1 标注格式

下面是`Stanford_bookstore_video0_0.txt`的示例注释文件：

```
4 0.984 0.531 0.027 0.045
0 0.532 0.844 0.031 0.040
4 0.420 0.937 0.021 0.034
0 0.630 0.168 0.027 0.042
0 0.287 0.931 0.014 0.029
```

该标注格式与 YOLOv5 标注格式相同，详细介绍请参见：[YOLO 标注格式](md/annotations/yolo.md)