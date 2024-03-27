# Single Object Tracking

## 1. 概述

官网：[https://github.com/VisDrone/VisDrone2018-SOT-toolkit](https://github.com/VisDrone/VisDrone2018-SOT-toolkit)

- 来源：单目标跟踪 (SOT) 竞赛的 VisDrone2018 竞赛开发套件的文档
- 格式说明：基于Wu等人的视觉基准平台修改的。
- 工具包：该代码在 Windows 10 和 macOS Sierra 10.12.6 系统以及 Matlab 2013a/2014b/2016b/2017b 平台上进行了测试。
- 数据集：对于VID竞赛，存在三组数据和标签：训练数据、验证数据和测试挑战数据。三组之间没有重叠。

## 2. 工具包说明

- 跟踪结果将存储在文件夹“.\results”中。
- 文件夹“.\trackers”包含跟踪器的所有源代码（例如 Staple）
- 文件夹“.\util”包含主要功能中使用的一些脚本。
- 主要功能
    - main_running.m 是运行跟踪器的主要函数
        - 根据 Staple tracker 的源码将源码放入./trackers/
        - 修改./main_running.m 中的数据集路径
        - 输入./util/configTrackers.m 中命名的方法
        - mat 格式的结果保存在./results/results_OPE/
    - perfPlot.m 是根据 mat 或 txt 格式的结果评估跟踪器的主要函数。
        - 修改./perfPlot.m 中的数据集路径（通过设置标志 “reEvalFlag = 1” 重新评估结果）
        - 选择在./util/configTrackers.m 中命名的跟踪器
        - 选择排名类型，例如 AUC 和阈值
        - 检查./results/results_OPE/ 中的跟踪结果
        - 数字保存在./figs/overall/
    - drawResultBB.m 是用于显示结果的主要函数
        - 修改./drawResultBB.m 中的数据集路径
        - 选择在./util/configTrackers.m 中命名的跟踪器
        - 检查./results/results_OPE/ 中的跟踪结果
        - 视觉结果保存在./tmp/OPE/ 中

## 3. 格式说明

txt格式：包括每个预测对象一行的 TXT 文件，每行包含以下信息：

```text
<bbox_left>,<bbox_top>,<bbox_width>,<bbox_height>
```

| Name            | Description    |
|-----------------|----------------|
| `<bbox_left>`   | 预测对象边界框左上角的x坐标 |
| `<bbox_top>`    | 预测对象边界框左上角的y坐标 |
| `<bbox_width>`  | 预测对象边界框的像素宽度   |
| `<bbox_height>` | 预测对象边界框的像素高度   |

mat格式

```matlab
< results: {type = 'rect', res, fps, len, annoBegin = 1, startFrame = 1} >
```

| Name           | Description                                                         |
|----------------|---------------------------------------------------------------------|
| `<type>`       | 预测边界框表示的表示类型。应设为'rect'。                                             |
| `<res>`        | 视频剪辑中的跟踪结果。<br/>值得注意的是，每行包括帧索引，预测边界框左上角的x和y坐标，<br/>以及预测边界框的像素宽度和高度。 |
| `<fps>`        | 评估跟踪器的运行速度，即每秒帧数。                                                   |
| `<len>`        | 评估序列的长度。                                                            |
| `<annoBegin>`  | 跟踪的开始帧索引。默认值为1。                                                     |
| `<startFrame>` | 视频的开始帧索引。默认值为1。                                                     |

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