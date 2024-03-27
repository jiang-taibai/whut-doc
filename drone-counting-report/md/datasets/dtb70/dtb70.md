# DTB70 Dataset

## 1. 介绍

官方发布页：[https://github.com/flyers/drone-tracking](https://github.com/flyers/drone-tracking)

DTB70 Dataset 是一个高多样性基准视频数据集，其被用于解决视觉跟踪领域中运动模型的研究，该数据集由 70 多个无人机拍摄的视频组成。

DTB70 数据集由香港科技大学・计算机科学与工程系的 Siyi Li 和 Dit-Yan Yeung 发布，相关论文有《Visual Object Tracking for
Unmanned Aerial Vehicles: A Benchmark and New Motion Models》。

<div class="custom-img-group">
  <img src="https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/dtb70/dtb70-dataset-preview-1.jpg" alt="DTB70 Dataset Preview 1">
  <img src="https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/dtb70/dtb70-dataset-preview-2.jpg" alt="DTB70 Dataset Preview 2">
  <img src="https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/dtb70/dtb70-dataset-preview-3.jpg" alt="DTB70 Dataset Preview 3">
  <img src="https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/dtb70/dtb70-dataset-preview-5.jpg" alt="DTB70 Dataset Preview 5">
  <img src="https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/dtb70/dtb70-dataset-preview-6.jpg" alt="DTB70 Dataset Preview 6">
  <img src="https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/dtb70/dtb70-dataset-preview-7.jpg" alt="DTB70 Dataset Preview 7">
</div>

## 2. 链接

- 百度网盘：
  [https://pan.baidu.com/s/1YmV0VlstBE0QKk_GO7QLoQ?pwd=cvlj](https://pan.baidu.com/s/1YmV0VlstBE0QKk_GO7QLoQ?pwd=cvlj)

- 工具集：[https://github.com/flyers/drone-tracking](https://github.com/flyers/drone-tracking)

## 3. 数据集格式

### 3.1 目录结构

```text
├─Animal1
│  ├─img
│  └─groundtruth_rect.txt
├─Basketball
│  ├─img
│  └─groundtruth_rect.txt
├─...
│  ├─img
│  └─groundtruth_rect.txt
├─BMX2
│  ├─img
│  └─groundtruth_rect.txt
└─Zebra
   ├─img
   └─groundtruth_rect.txt
```

### 3.2 标注格式

每个`groundtruth_rect.txt`对应同级下的img文件夹，img文件夹中存放了该视频的所有帧图片。

`groundtruth_rect.txt`中每一行对应一帧图片的标注，每一行的格式为`x,y,w,h`，分别表示目标框的左上角坐标和宽高。

数据集格式遵循[OTB50](http://cvlab.hanyang.ac.kr/tracker_benchmark/index.html)

在OTB50数据集中，每个视频序列都配有一个标注文件，文件名通常为"groundtruth_rect.txt"。这个文件包含了视频中每一帧的目标位置信息。

OTB50的标注格式如下：

```text
x,y,w,h
x,y,w,h
```

每一行对应一帧视频中的目标位置，其中：

- `x`和`y`是目标边界框左上角的坐标。
- `w`和`h`是目标边界框的宽度和高度。

所有的坐标和尺寸都是以像素为单位的。

例如，如果一个视频有N帧，那么`groundtruth_rect.txt`文件就会有N行，每一行都是一个 x,y,w,h的四元组，表示对应帧中目标的位置和尺寸。

```text
1004,517,65,68
1005.4,515.04,63,66
1007,513,60,72
1006.2,510.87,65,68
1005.4,508.55,67,70
```

## Citation

If you are using this code in a publication, please cite our paper.

```BibTex
@inproceedings{drone-tracking,
    title={Visual object tracking for unmanned aerial vehicles: A benchmark and new motion models},
    author={Li, Siyi and Yeung, Dit-Yan},
    booktitle = {AAAI},
    year={2017}
}
```

