# Single Object Tracking

## 1. 概述

官网：[https://github.com/VisDrone/VisDrone2018-MOT-toolkit](https://github.com/VisDrone/VisDrone2018-MOT-toolkit)

- 来源：用于多目标跟踪 (MOT) 挑战的 VisDrone2018 竞赛开发套件的文档。
- 格式说明：基于MOTChallenge和PASCAL VOC中的工具包修改的。
- 工具包：该代码在 Windows 10 和 macOS Sierra 10.12.6 系统以及 Matlab 2013a/2014b/2016b/2017b 平台上进行了测试。
- 数据集：对于 MOT 竞赛，存在三组数据和标签：训练数据、验证数据和测试挑战数据。三组之间没有重叠。

## 2. 工具包介绍

- 主要功能
    - evalMOT.m 是评估您的跟踪器的主要函数
        - 源码放在./trackers/中（请参考GOG tracker源码）
        - 修改数据集路径和结果路径
        - 使用“isSeqDisplay”显示真实情况和检测结果
        - 选择评估的任务，即没有检测结果的任务4A，有检测结果的任务4B
    - evaluateTrackA.m 是使用任务 4A 中的措施评估跟踪器的主要函数，无需检测结果。
    - valuateTrackB.m 是使用任务 4B 中的措施和 Faster RCNN 检测结果来评估跟踪器的主要函数。

## 3. 数据集格式

标注由 TXT 文件组成，每个预测对象一行

```text
<frame_index>,<target_id>,<bbox_left>,<bbox_top>,<bbox_width>,<bbox_height>,<score>,<object_category>,<truncation>,<occlusion>
```

| 名称                  | 描述                                                                                                               |
|---------------------|------------------------------------------------------------------------------------------------------------------|
| `<frame_index>`     | 视频帧的帧索引                                                                                                          |
| `<target_id>`       | 在DETECTION结果文件中，目标的身份应设为常数-1。在GROUNDTRUTH文件中，目标的身份用于提供不同帧中边界框的时间对应关系。                                            |
| `<bbox_left>`       | 预测边界框左上角的x坐标                                                                                                     |
| `<bbox_top>`        | 预测对象边界框左上角的y坐标                                                                                                   |
| `<bbox_width>`      | 预测对象边界框的像素宽度                                                                                                     |
| `<bbox_height>`     | 预测对象边界框的像素高度                                                                                                     |
| `<score>`           | 在DETECTION文件中，分数表示预测边界框包围对象实例的置信度。在GROUNDTRUTH文件中，分数设为1或0。1表示在评估中考虑边界框，而0表示将忽略边界框。                               |
| `<object_category>` | 对象类别表示注释对象的类型，即，忽略区域(0)，行人(1)，人(2)，自行车(3)，汽车(4)，货车(5)，卡车(6)，三轮车(7)，遮阳三轮车(8)，公交车(9)，电机(10)，其他(11)                 |
| `<truncation>`      | 在DETECTION文件中，分数应设为常数-1。在GROUNDTRUTH文件中，分数表示对象部分出现在帧外的程度（即，无截断=0（截断比例0%），部分截断=1（截断比例1%~50%））。                    |
| `<occlusion>`       | 在DETECTION文件中，分数应设为常数-1。在GROUNDTRUTH文件中，分数表示对象被遮挡的部分（即，无遮挡=0（遮挡比例0%），部分遮挡=1（遮挡比例1%\~50%），重度遮挡=2（遮挡比例50%\~100%））。 |

## 4. 版权信息

If you use our toolkit or dataset, please cite our paper as follows:

```text
@article{zhuvisdrone2018,
    title={Vision Meets Drones: A Challenge},
    author={Zhu, Pengfei and Wen, Longyin and Bian, Xiao and Haibin, Ling and Hu, Qinghua},
    journal={arXiv preprint:1804.07437},
    year={2018}
}
```