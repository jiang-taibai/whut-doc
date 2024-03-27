# HighD Dataset

## 1. 介绍

<video autoplay="autoplay" muted="muted" loop="loop" style="width: 100%">
    <source data-v-b11bcf84="" src="https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/high-d/high-d-dataset-intro.mp4" type="video/mp4">
</video>

官网：[https://www.highd-dataset.com/](https://www.highd-dataset.com/)

highD数据集是一个新的自然车辆轨迹数据集，记录了德国高速公路上的车辆情况。通过使用无人机，
克服了传统交通数据收集方法（如遮挡）的典型限制，提供了航空视角。

我们在六个不同的地点记录了交通情况，包括超过110500辆车辆。
每辆车的轨迹，包括车辆类型、大小和驾驶行为，都被自动提取出来。
使用最先进的计算机视觉算法，定位误差通常小于十厘米。

虽然这个数据集是为了验证高度自动化车辆的安全性而创建的，但它也适合于许多其他任务，如交通模式的分析或驾驶模型的参数化。

该团队的其他数据集如下：

- exiD: [https://www.exid-dataset.com/](https://www.exid-dataset.com/)
- inD: [https://www.ind-dataset.com/](https://www.ind-dataset.com/)
- rounD: [https://www.round-dataset.com/](https://www.round-dataset.com/)
- uniD: [https://www.unid-dataset.com/](https://www.unid-dataset.com/)

## 2. 特性

- 大规模数据集：
    - 110,500辆车
    - 44,500公里的行驶距离
    - 147小时的行驶时间
- 高质量与多样性
    - 六个不同的记录位置
    - 不同的交通状态（例如交通堵塞）
    - 典型定位误差<10厘米
- 丰富的数据
    - 周围的车辆
    - 像THW或TTC这样的指标
    - 行驶操作（例如变道）
- 为Matlab和Python提供的脚本：
    - 解析提供的文件
    - 可视化记录的轨迹

## 3. 链接

使用高校邮箱即可申请下载: [https://www.highd-dataset.com/#download](https://www.highd-dataset.com/#download)

## 4. 数据集说明

官方说明文档: [https://www.highd-dataset.com/format](https://www.highd-dataset.com/format)

```pdf
https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/high-d/the-high-d-dataset-format_files.pdf
```

## Citation

To reference the dataset, please cite this publication:

```BiBTeX
@inproceedings{highDdataset,
               title={The highD Dataset: A Drone Dataset of Naturalistic Vehicle Trajectories on German Highways for Validation of Highly Automated Driving Systems},
               author={Krajewski, Robert and Bock, Julian and Kloeker, Laurent and Eckstein, Lutz},
               booktitle={2018 21st International Conference on Intelligent Transportation Systems (ITSC)},
               pages={2118-2125},
               year={2018},
               doi={10.1109/ITSC.2018.8569552}}
```



