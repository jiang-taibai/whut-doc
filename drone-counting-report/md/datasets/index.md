# 国内外数据集总览

## 1. 来源高校

| 高校      |                  团队                   |                                            数据集                                             | 备注                                  |
|---------|:-------------------------------------:|:------------------------------------------------------------------------------------------:|-------------------------------------|
| 天津大学    |   [AISKYEYE](md/teams/aiskyeye.md)    |                [**VisDrone 2019**](md/datasets/vis-drone/vis-drone-2019.md)                | 无人机目标检测和追踪基准数据集                     |
| 天津大学    |   [AISKYEYE](md/teams/aiskyeye.md)    |                 [**DroneVehicle**](md/datasets/vis-drone/drone-vehicle.md)                 | 基于无人机的 RGB-T 车辆检测数据集                |
| 天津大学    |   [AISKYEYE](md/teams/aiskyeye.md)    |                   [**DroneCrowd**](md/datasets/vis-drone/drone-crowd.md)                   | 基于无人机的人群密度图估计，计数和跟踪的人群分析数据集         |
| 天津大学    |   [AISKYEYE](md/teams/aiskyeye.md)    |                  [**AnimalDrone**](md/datasets/vis-drone/drone-animal.md)                  | 基于无人机的视频动物计数数据集                     |
| 天津大学    |   [AISKYEYE](md/teams/aiskyeye.md)    |                   [**DroneRGBT**](/md/datasets/vis-drone/drone-rgbt.md)                    | 基于无人机的 RGB-T 人群计数数据集                |
| 天津大学    |   [AISKYEYE](md/teams/aiskyeye.md)    |                                             -                                              | 多无人机单目标跟踪数据集                        |
| 天津大学    |   [AISKYEYE](md/teams/aiskyeye.md)    |                                             -                                              | 多无人机多目标跟踪数据集                        |
| 斯坦福大学   |                   -                   | [**Stanford Drone Dataset**](md/datasets/stanford-drone-dataset/stanford-drone-dataset.md) | -                                   |
| 武汉大学    |  [CAPTAIN](md/teams/captain-whu.md)   |                 [**DOTA-Images**](md/datasets/dota-images/dota-images.md)                  | -                                   |
| 武汉大学    |      [RSPiP](md/teams/rspip.md)       |                        [**RSOD Dataset**](md/datasets/rsod/rsod.md)                        | -                                   |
| 武汉大学    |      [RSPiP](md/teams/rspip.md)       |                     [**RSD46 Dataset**](md/datasets/rsd-46/rsd-46.md)                      | -                                   |
| 中国科学院大学 |          模式识别与<br/>智能系统开发实验室          |                      [**UCAS-AOD**](md/datasets/ucas-aod/ucas-aod.md)                      | -                                   |
| KAUST   |       [IVUL](md/teams/ivul.md)        |                         [**UAV123**](md/datasets/uav123/uav123.md)                         | -                                   |
| 奥胡斯大学   |            AU Engineering             |                         [**AU-AIR**](md/datasets/au-air/au-air.md)                         | 用于目标检测的多模态无人机数据集，集合了无人机上不同传感器的多模态数据 |
| 香港科技大学  | 计算机科学与工程系<br/>Siyi Li & Dit-Yan Yeung |                          [**DTB70**](md/datasets/dtb70/dtb70.md)                           | -                                   |

## 2. 来源论文收集

### 2.1 A review on object detection in unmanned aerial vehicle surveillance

> [!TIP]
> 下表数据来源论文：
> [A review on object detection in unmanned aerial vehicle surveillance](https://doi.org/10.1016/j.ijcce.2021.11.005)

| No | Dataset                 | Year | Link                                                     | Objects                                                                |   Number   |       Resolution       |
|----|:------------------------|------|----------------------------------------------------------|------------------------------------------------------------------------|:----------:|:----------------------:|
| 1  | UAVid                   | 2020 | https://uavid.nl/                                        | Car, Building, Low,Vegetation, Human,Tree, Background clutter,and Road |    300     | 4096×2160 or 3840×2160 |
| 2  | Stanford Drone Dataset  | 2016 | https://cvgl.stanford.edu/projects/uav_data/             | Skateboard, cart, Pedestrian, Bicyclist, bus, and car                  |   929.5k   |       1400×1904        |
| 3  | Okutama-Action Dataset  | 2017 | http://okutama-action.org/                               | Human actions                                                          |   77.4k    |       3840×2160        |
| 4  | Mini-drone              | 2015 | https://www.epfl.ch/labs/mmspg/downloads/mini-drone/     | Human actions in the parking area                                      |   23.3k    |       1920×1080        |
| 5  | Drone-Action Dataset    | 2019 | https://asankagp.github.io/droneaction/                  | Human actions                                                          |   66.9k    |       1920×1080        |
| 6  | VisDrone                | 2020 | http://aiskyeye.com/                                     | Vehicles                                                               |   10209    |       2000×1500        |
| 7  | UAVDT                   | 2020 | https://sites.google.com/site/daviddo0323/projects/uavdt | Vehicles                                                               |    80k     |        1080×540        |
| 8  | UAV20L, UAV123          | 2016 | https://cemse.kaust.edu.sa/ivul/uav123                   | Person, car, and building                                              | 58.7k 110k |        1280×720        |
| 9  | CARPK, PUCPR+           | 2017 | https://lafi.github.io/LPN/                              | Car                                                                    |    1448    |        1280×720        |
| 10 | The UAV-Gesture Dataset | 2018 | https://asankagp.github.io/uavgesture/                   | Human action                                                           |   37.2k    |       1920×1080        |
| 11 | VEDAI512                | 2016 | https://downloads.greyc.fr/vedai/                        | Vehicles                                                               |    1.2k    |       1024×1024        |
| 12 | Drone face              | 2017 | https://hjhsu.github.io/DroneFace/                       | Human face                                                             |    620     |       3680×2760        |
| 13 | Drone surf              | 2019 | http://www.iab-rubric.org/resources/dronesurf.html       | Human face                                                             |  411.5 k   |        1280×720        |
| 14 | Deepweeds               | 2019 | https://github.com/AlexOlsen/DeepWeeds                   | Weeds                                                                  |   17.5 k   |       1920×1200        |
| 15 | Agriculture-Vision      | 2020 | https://www.agriculture-vision.com/dataset               | Agriculture patterns                                                   |   94.9 k   |        512×512         |

## 3. 来源社会各界

| 部            | 组             | 数据集     | 已收录至                                                                   | 备注                                                |
|--------------|---------------|---------|------------------------------------------------------------------------|---------------------------------------------------|
| 英国南极调查局      |               | 野生动物栖息地 | [Wildlife Colonies 数据集](md/datasets/british-antarctic-survey/01483.md) | 2019-2020 年南乔治亚岛和南桑威奇群岛野生动物栖息地的无人机图像              |
| 英国南极调查局      |               | 其他      | [British Antarctic Survey](md/teams/british-antarctic-survey.md)       | 其他数据集在英国南极调查局中详细列举                                |
| 劳伦斯利弗莫尔国家实验室 | 计算工程部门的计算机视觉组 | COWC    | [COWC](md/datasets/cowc/cowc.md)                                       | 包含大量从高空视角注释的汽车的数据集，适用于训练像深度神经网络这样的设备来学习检测和/或计数汽车。 |

## 4. 来源互联网搜索

| 数据集名称  |                                                 数据集来源                                                 |                  收录至                   |
|:------:|:-----------------------------------------------------------------------------------------------------:|:--------------------------------------:|
| UZAODD | [KAGGLE-UZAODD](https://www.kaggle.com/datasets/sganderla/urban-zone-aerial-object-detection-dataset) | [UZAODD](md/datasets/uzaodd/uzaodd.md) |

