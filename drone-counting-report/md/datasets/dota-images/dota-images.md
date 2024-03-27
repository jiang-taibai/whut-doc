# DOTA Images Dataset

## 1. 数据集介绍

官网：[https://captain-whu.github.io/DOTA/dataset.html](https://captain-whu.github.io/DOTA/dataset.html)

该数据集由武汉大学于 2017 年 11 月 28 日在 arXiv 上发布，在 2018 年 6 月在 IEEE 计算机视觉和模式识别会议上发布，
一共 2806 幅航拍图，包含不同尺度、方向和形状的物体，每张图片的像素尺寸在 800*800 到 4000*4000 的范围内。

DOTA数据集的图像来源于Google Earth，中国资源卫星应用中心提供的GF-2和JL-1卫星，以及CycloMedia B.V. 提供的航拍图像。

DOTA包含RGB图像和灰度图像。其中，RGB图像来自Google Earth和CycloMedia，而灰度图像则来自GF-2和JL-1卫星图像的全色波段。

所有的图像都以'png'格式存储。

## 2. 数据集版本

- 在DOTA-v1.0版本中，目标类别包括：飞机、船、储罐、棒球场、网球场、篮球场、田径场、港口、桥梁、大型车辆、小型车辆、直升机、环形交叉路口、足球场和游泳池。

- 在DOTA-v1.5版本中，目标类别包括：飞机、船、储罐、棒球场、网球场、篮球场、田径场、港口、桥梁、大型车辆、小型车辆、直升机、环形交叉路口、足球场、游泳池和集装箱起重机。

- 在DOTA-v2.0版本中，目标类别包括：飞机、船、储罐、棒球场、网球场、篮球场、田径场、港口、桥梁、大型车辆、小型车辆、直升机、环形交叉路口、足球场、游泳池、集装箱起重机、机场和直升机停机坪。

## 3. 数据集下载

DOTA-v1.0~v2.0:
[https://pan.baidu.com/s/1L2V-F34p4Pmm0qcuuGF-_g?pwd=cvlj](https://pan.baidu.com/s/1L2V-F34p4Pmm0qcuuGF-_g?pwd=cvlj)

额外说明：对于DOTA-v2.0，需要下载 DOTA-v1.0 图片，然后下载 DOTA-v2.0 的额外图片和注释。请注意，DOTA-v1.0 中的图像已被重新标记。因此，要在
DOTA-v2.0 上评估您的模型，您应该仅使用 DOTA-v2.0 的注释。

## 4. 数据集格式

在这个数据集中，每一个目标都由一个定向边界框（OBB）进行标注，
该边界框可被表述为`(x1, y1, x2, y2, x3, y3, x4, y4)`，其中`(xi, yi)`代表OBB的第i个顶点。顶点按照顺时针方向进行排序。

下面是注释的可视化。黄色点代表起点，表示:(a)飞机的左上角，(b)大型交通工具的左上角，(c)棒球菱形的中心。

![dota-datasets-preview](https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/dota-dataset/dota-datasets-preview.png)

除了OBB之外，每一个实例还会被标注一个类别和一个难度等级，用以标识该实例是否难以被检测（1代表困难，0代表不困难）。
一个图像的所有标注都保存在一个与其同名的文本文件中。每一行代表一个实例。以下是一张图像的标注示例：

```text
x1, y1, x2, y2, x3, y3, x4, y4, category, difficult
x1, y1, x2, y2, x3, y3, x4, y4, category, difficult
```

图像获取日期、图像来源以及地面采样距离（GSD）的元数据都已经提供。

在第一行，提供了'acquisition dates'（获取日期）。

在第二行，提供了'imagesource'（图像来源，可能是GoogleEarth，GF-2或JL-1）。

在第三行，提供了以米为单位的地面采样距离（GSD）。如果'获取日期'和'GSD'丢失了，它们会被标记为'None'。

```text
'acquisition dates':acquisition dates
'imagesource':imagesource
'gsd':gsd
```

## 5. 数据集工具包

开发套件提供以下功能：

- 加载并可视化数据。
- 评估结果。
- 拆分和合并数据。

可以在这里下载开发套件：[https://github.com/CAPTAIN-WHU/DOTA_devkit](https://github.com/CAPTAIN-WHU/DOTA_devkit)

使用DOTA.py读取和可视化数据

## Citation

If you make use of the DOTA dataset, please cite our following paper:

```BibTeX
@ARTICLE{9560031,
    author={Ding, Jian and Xue, Nan and Xia, Gui-Song and Bai, Xiang and Yang, Wen and Yang, Michael and Belongie, Serge and Luo, Jiebo and Datcu, Mihai and Pelillo, Marcello and Zhang, Liangpei},
    journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
    title={Object Detection in Aerial Images: A Large-Scale Benchmark and Challenges},
    year={2021},
    volume={},
    number={},
    pages={1-1},
    doi={10.1109/TPAMI.2021.3117983}
}
```

```BibTeX
@InProceedings{Xia_2018_CVPR,
    author = {Xia, Gui-Song and Bai, Xiang and Ding, Jian and Zhu, Zhen and Belongie, Serge and Luo, Jiebo and Datcu, Mihai and Pelillo, Marcello and Zhang, Liangpei},
    title = {DOTA: A Large-Scale Dataset for Object Detection in Aerial Images},
    booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
    month = {June},
    year = {2018}
}
```

```BibTeX
@InProceedings{Ding_2019_CVPR,
    author = {Jian Ding, Nan Xue, Yang Long, Gui-Song Xia, Qikai Lu},
    title = {Learning RoI Transformer for Detecting Oriented Objects in Aerial Images},
    booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
    month = {June},
    year = {2019}
}
```