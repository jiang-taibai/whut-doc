# VisDrone 2019

## 1. 数据集简介

> 官网：[https://github.com/VisDrone/VisDrone-Dataset](https://github.com/VisDrone/VisDrone-Dataset)
>
> 《探测和跟踪是无人机面临的挑战》（Detection and Tracking Meet Drones Challenge）
> - Link: [https://ieeexplore.ieee.org/document/9573394](https://ieeexplore.ieee.org/document/9573394)
> - Published: 01 November 2022
> - DOI: 10.1109/TPAMI.2021.3119563

VisDrone2019数据集由天津大学机器学习和数据挖掘实验室的AISKYEYE团队收集。

基准数据集由各种无人机相机拍摄的261908帧和10209幅静态图像组成的288段视频片段组成，
涵盖了位置(取自中国相隔数千公里的14个不同城市)、环境(城市和农村)、目标(行人、车辆、自行车等)和密度(稀疏和拥挤的场景)等广泛方面。

注意，该数据集是使用各种无人机平台(即不同模型的无人机)在不同场景以及不同天气和光照条件下收集的。

这些框架使用260多万个频繁兴趣目标的边界框进行人工标注，如行人、汽车、自行车和三轮车。

此外，还提供了一些重要的属性，包括场景可见性、目标类别和遮挡，以更好地利用数据。

<div class="custom-img-group">
  <img src="https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/vis-drone/vis-drone-preview-01.jpg" alt="vis-drone-preview-01.jpg"/>
  <img src="https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/vis-drone/vis-drone-preview-02.jpg" alt="vis-drone-preview-02.jpg"/>
  <img src="https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/vis-drone/vis-drone-preview-03.jpg" alt="vis-drone-preview-03.jpg"/>
  <img src="https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/vis-drone/vis-drone-preview-04.jpg" alt="vis-drone-preview-04.jpg"/>
  <img src="https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/vis-drone/vis-drone-preview-05.jpg" alt="vis-drone-preview-05.jpg"/>
  <img src="https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/vis-drone/vis-drone-preview-06.jpg" alt="vis-drone-preview-06.jpg"/>
</div>

## 2. 数据集任务

1. 图像目标检测：该任务旨在从无人机拍摄的单个图像中检测预定义类别的目标(例如，汽车和行人)。
2. 视频目标检测：该任务与任务1类似，不同的是需要从视频中检测物体。
3. 单目标跟踪：该任务旨在估计目标的状态，在第一个帧中表示，在后续的视频帧中。
4. 多目标跟踪：该任务旨在恢复每个视频帧中物体的轨迹。
5. 人群计数：该任务的目的是对每个视频帧中的人数进行统计。

## 3. 团队相关数据集

> [!TIP|label:VisDrone 数据集系列]
> 打钩表示已在本报告中收录，点击名称可跳转到相应的报告。

- [x] [**VisDrone**](md/datasets/vis-drone/vis-drone-2019.md)：无人机目标检测和追踪基准数据集。（Detection and Tracking
  Meet Drones Challenge, IEEE Transactions on
  Pattern
  Analysis and Machine Intelligence, 2021）
- [x] [**DroneVehicle**](md/datasets/vis-drone/drone-vehicle.md)：基于无人机的 RGB-T 车辆检测数据集。（Drone-Based
  RGB-Infrared
  Cross-Modality
  Vehicle
  Detection via
  Uncertainty-Aware Learning, IEEE Transactions on Circuits and Systems for Video Technology, 2022）
- [x] [**DroneCrowd**](md/datasets/vis-drone/drone-crowd.md)：基于无人机的人群密度图估计，计数和跟踪的人群分析数据集。（Detection,
  Tracking, and
  Counting Meets Drones in
  Crowds: A Benchmark, Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2021）
- [x] [**AnimalDrone**](md/datasets/vis-drone/drone-animal.md)：基于无人机的视频动物计数数据集。（Graph Regularized Flow
  Attention Network for
  Video
  Animal Counting From
  Drones, IEEE Transactions on Image Processing, 2021）
- [x] [**DroneRGBT**](/md/datasets/vis-drone/drone-rgbt.md)：基于无人机的 RGB-T 人群计数数据集。（RGB-T Crowd Counting from
  Drone: A Benchmark and
  MMCCN
  Network,
  Proceedings of the Asian Conference on Computer Vision, 2020）
- [ ] MultiDrone：多无人机单目标跟踪数据集。（Multi-Drone-Based Single Object Tracking With Agent Sharing Network, IEEE
  Transactions on Circuits and Systems for Video Technology, 2020）
- [ ] MDMT: 多无人机多目标跟踪数据集。（Robust Multi-Drone Multi-Target Tracking to Resolve Target Occlusion: A
  Benchmark，2022）

## 4. 数据集列表

### 4.1 图像中的目标检测

- 百度网盘：
  [https://pan.baidu.com/s/1I7hCb0UYcUH7XK1AG9xFGw?pwd=cvlj](https://pan.baidu.com/s/1I7hCb0UYcUH7XK1AG9xFGw?pwd=cvlj)
- 标注格式说明文档：[VisDrone - Object Detection in Images](md/annotations/vis-drone/object-detection-in-images.md)

```text
Object Detection in Images/
├─VisDrone2019-DET-test-challenge
│  └─images
├─VisDrone2019-DET-test-dev
│  ├─annotations
│  └─images
├─VisDrone2019-DET-train
│  ├─annotations
│  └─images
└─VisDrone2019-DET-val
    ├─annotations
    └─images
```

### 4.2 视频中的目标检测

- 百度网盘：
  [https://pan.baidu.com/s/1hutdGyyk4CKBYM3DXxXrsg?pwd=cvlj](https://pan.baidu.com/s/1hutdGyyk4CKBYM3DXxXrsg?pwd=cvlj)
- 标注格式说明文档：[VisDrone - Object Detection in Videos](md/annotations/vis-drone/object-detection-in-videos.md)

```text
Object Detection in Videos/
├─VisDrone2019-VID-test-challenge
│  └─sequences
│      ├─uav0000006_06900_v
│      ├─...
│      └─uav0000369_00001_v
├─VisDrone2019-VID-test-dev
│  ├─annotations
│  └─sequences
│      ├─uav0000009_03358_v
│      ├─...
│      └─uav0000370_00001_v
├─VisDrone2019-VID-train
│  ├─annotations
│  └─sequences
│      ├─uav0000013_00000_v
│      ├─...
│      └─uav0000366_00001_v
└─VisDrone2019-VID-val
    ├─annotations
    └─sequences
        ├─uav0000086_00000_v
        ├─...
        └─uav0000339_00001_v
```

### 4.3 单目标跟踪

- 百度网盘：
  [https://pan.baidu.com/s/18cJVjJI2X1QqyKcARQY6ew?pwd=cvlj](https://pan.baidu.com/s/18cJVjJI2X1QqyKcARQY6ew?pwd=cvlj)
- 标注格式说明文档：[VisDrone - Single Object Tracking](md/annotations/vis-drone/single-object-tracking.md)

```text
Single Object Tracking/
├─VisDrone2019-SOT-test-challenge_initialization.zip
├─VisDrone2019-SOT-test-challenge_part1.zip
├─VisDrone2019-SOT-test-challenge_part2.zip
├─VisDrone2019-SOT-test-dev.zip
├─VisDrone2019-SOT-train_part1.zip
├─VisDrone2019-SOT-train_part2.zip
└─VisDrone2019-SOT-val.zip
```

### 4.4 多目标跟踪

- 百度网盘：
  [https://pan.baidu.com/s/1fMeM9NGipGrlYsF40TVlaQ?pwd=cvlj](https://pan.baidu.com/s/1fMeM9NGipGrlYsF40TVlaQ?pwd=cvlj)
- 标注格式说明文档：[VisDrone - Multiple Object Tracking](md/annotations/vis-drone/multiple-object-tracking.md)

```text
Multiple Object Tracking/
├─VisDrone2019-MOT-test-challenge.zip
├─VisDrone2019-MOT-test-dev.zip
├─VisDrone2019-MOT-train.zip
└─VisDrone2019-MOT-val.zip
```

### 4.5 人群计数

该数据集已被收录到调研报告 [VisDrone DroneCrowd](md/datasets/vis-drone/drone-crowd.md) 中。

可在该章节中详细查看数据集相关信息。

## 5. 相关文章

- [《深度学习目标检测数据 VisDrone2019（to yolo /voc/coco）---MMDetection 数据篇》](https://blog.csdn.net/qq_41627642/article/details/124662888)
