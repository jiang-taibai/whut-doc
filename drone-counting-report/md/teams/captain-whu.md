# CAPTAIN

## 1. 介绍

官网：[http://www.captain-whu.com/index.html](http://www.captain-whu.com/index.html)

CAPTAIN研究组（武汉大学计算视觉与摄影测量研究组）致力于计算机视觉、机器学习、航空航天摄影测量与遥感等领域中前沿问题的理论研究和算法设计，
包括纹理建模、三维重建、目标检测、语义分割、场景分类等研究课题，主要涉及图像理解、机器学习、深度学习、优化理论、空间几何等理论和方法。

CAPTAIN 汇聚了来自全国各地的优秀学子，现有博士研究生 14人，硕士研究生29 人。
研究组内不乏数学高手、编程达人、运动健将，7名同学曾获得数模竞赛一1二等奖，
10 名同学获电子设计大赛全国一等奖3名同学获大疆无人机全球挑战赛总决赛第三名,9名同学获得湖北省优秀学士学位论文奖，
多名同学在IEEE TPAMI/TIP/TGRS、RSE、PR、ISPRS、CVPR、ECCV 等国际顶级期刊和会议上发表学术研究成果。

![captain-team-intro](https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/teams/captain/captain-team-intro.jpg)

## 2. 研究方向

<div style="display: flex; flex-wrap: wrap;gap: 8px">
<div>

- 计算机视觉
    - 图像处理
    - 图像结构分析
    - 图匹配
    - 纹理建模与分析
    - 目标识别
    - 医学图像处理
    - 点云语义分割

</div>
<div>

- 遥感影像理解
    - 影像数据集
    - 目标检测
    - 变化检测
    - 图像检索
    - 场景分类
    - 图像分割
    - 视频处理与分析
    - 无人机遥感
    - SAR 图像处理

</div>
<div>

- 应用平台
    - 广域遥感图像分析平台
    - 遥感影像智能解译系统

</div>
</div>

## 3. 设备与技术

> [!TIP]
> 来自论文: [DOTA: A Large-Scale Dataset for Object Detection in Aerial Images](https://ieeexplore.ieee.org/document/8578516)
> 
> 该论文为 DOTA 数据集的发表论文，该数据集由该团队负责。

### 3.1 数据获取

- 技巧：该团队会记录每张图片的确切地理坐标和拍摄时间，以确保不存在重复的图片。
- 方式：
    - 遥感卫星
    - 众包平台
    - 谷歌地球

### 3.2 数据标注

该团队提出了一种新的标注方式，即面向对象的标注方式 OBB（Oriented Bounding Box）

OBB 可以更好地将对象和区分互相拥挤的对象。

## 4. 相关数据集

1. DOTA Images收录至：[DOTA Images Dataset](md/datasets/dota-images/dota-images.md)