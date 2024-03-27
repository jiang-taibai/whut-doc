# 数据集概述

## 1. 制作流程与工具

1. 数据采集:
    - 大疆无人机：AISKYEYE团队、英国南极调查局、IVUL团队
    - Phantom高速摄像机：AISKYEYE团队
    - 珞珈三号 01 星：RSPiP团队
    - Google Earth
    - 天地图：
    - 总包平台：CAPTAIN团队
2. 无人机镜头：
    - Panasonic GH4：IVUL团队
    - Olympus M. Zuiko 12毫米f2.0镜头：IVUL团队
3. 无人机飞行软件:
    - DJI GO4 app：英国南极调查局
4. 数据管理:
    - Adobe Lightroom CC 10.0：英国南极调查局
5. 视频转图片帧序列：
    - ffmpeg
    - 直接代码处理
6. 图像处理:
    - Agisoft Metashape：英国南极调查局
7. 图像标注:
    - DotDotGoose：英国南极调查局
    - CVAT
    - LabelImg
    - LabelMe
    - VIA-VGG Image Annotator
    - Vatic
    - scalabel
    - DarkLabel
    - Vidat

## 2. 数据集格式

### 2.1 数据形式

数据集的展现形式有两种，一种是图片格式，另一种是视频格式。

但一般视频格式的数据集将按照帧数进行编号，每一帧都是一张图片。

### 2.2 数据来源

- 自行拍摄：
    - 小型无人机Drone
    - 大型无人机UAV
    - 遥感卫星
- 网络获取：
    - Google Earth: [https://earth.google.com/web/](https://earth.google.com/web/)
    - 天地图: [https://www.tianditu.gov.cn/](https://www.tianditu.gov.cn/)
    - 其他团队的公开或商业级数据集

### 2.3 数据标注格式

一些研究团队会自己制作数据集，例如AISKYEYE团队的VisDrone的数据集，这些数据集的标注格式一般是自定义的，
因此需要编写代码来将其转换为常用的标注格式，如COCO、VOC、YOLO等。

另外一些公开的数据集，其标注格式已经是常用的格式，例如YOLO、VOC等，因此可以直接使用。




