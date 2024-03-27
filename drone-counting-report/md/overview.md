# 概述

<!-- tabs:start -->

## **v1.1**

- Update Time: 2024年03月07日 23:40:12
- Change Log:
    - 域名调整，切换 CDN 服务商

## **v1.0**

|      Type      | Style | Version | Link                                                                                                                         |    Note     |
|:--------------:|:-----:|:-------:|------------------------------------------------------------------------------------------------------------------------------|:-----------:|
|      HTML      | Dark  |  v1.0   | [uav-counting-report_dark.html](https://doc.coderjiang.com/whut/uav-counting-report/export/v1/uav-counting-report_dark.html) |  Recommend  |
|      HTML      |   -   |  v1.0   | [uav-counting-report.html](https://doc.coderjiang.com/whut/uav-counting-report/export/v1/uav-counting-report.html)           |             |
|      PDF       |   -   |  v1.0   | [uav-counting-report.pdf](https://doc.coderjiang.com/whut/uav-counting-report/export/v1/uav-counting-report.pdf)             |             |
|      Docx      |   -   |  v1.0   | [uav-counting-report.docx](https://doc.coderjiang.com/whut/uav-counting-report/export/v1/uav-counting-report.docx)           |             |
|    Markdown    |   -   |  v1.0   | [uav-counting-report.md](https://doc.coderjiang.com/whut/uav-counting-report/export/v1/uav-counting-report.md)               | Source File |
| Docsify&Python |   -   |  v1.0   | [uav-counting-report.zip](https://doc.coderjiang.com/whut/uav-counting-report/export/v1/uav-counting-report.zip)             |    项目源文件    |


<!-- tabs:end -->


## 1. 任务描述

<img src="https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/datasets/vis-drone/drone-animal-introduction.jpg" alt="drone-animal-introduction"/>

无人机计数是计算机视觉领域的一个应用，主要是利用无人机（也称为无人飞行器或者是无人驾驶飞行器）进行高空拍摄，
然后通过计算机视觉技术对拍摄的图像进行分析，以实现对特定目标（如人群、车辆、动物、树木等）的自动计数。

这种技术的应用场景非常广泛，例如

- 在农业领域，可以用来统计农田中的作物数量；
- 在环保领域，可以用来监测和统计野生动物的数量；
- 在城市管理领域，可以用来统计车辆和人群的数量等等。

实现无人机计数的关键技术主要包括目标检测、目标跟踪和目标识别等。

- 目标检测：识别图像中的特定目标；
- 目标跟踪：在连续的图像序列中跟踪特定目标的运动轨迹；
- 目标识别：确定检测到的目标的类别。

这些技术通常需要利用深度学习等机器学习方法来实现。

另外的，[**IVUL团队**](md/teams/ivul.md) 在 [**UAV123 Dataset**](md/datasets/uav123/uav123.md)
的相关论文中还提到了利用虚拟引擎技术预设无人机的轨迹移动

## 2. 任务目标

无人机计数的任务目标主要包括以下几个方面：

1. **目标检测**：这是无人机计数的首要任务，需要在无人机拍摄的图像中识别并定位出感兴趣的目标，例如人、车辆、动物、树木等。这通常涉及到复杂的图像处理和机器学习算法，如卷积神经网络（CNN）和深度学习。

2. **目标跟踪**：在连续的图像序列中，跟踪已经被检测出来的目标的运动轨迹。这对于动态的计数任务（例如，计算过马路的人数或者车辆数）非常重要。

3. **目标分类**：对检测出来的目标进行分类，例如区分人和车辆，或者区分不同种类的动物。这对于多目标计数任务非常重要。

4. **计数**：基于上述步骤，最后进行目标的计数。这可能涉及到处理重叠目标的问题，因为在高密度的场景中，目标可能会相互遮挡，导致计数困难。

5. **实时性**：对于某些应用（例如交通监控或者人群管理），无人机计数需要能够实时进行，这就需要算法具有高效的计算性能。

6. **鲁棒性**：无人机计数需要能够处理各种复杂的环境条件，例如光照变化、天气变化、目标的大小和形状变化等。

7. **自动化**：最终的目标是实现无人机计数的全自动化，即无人机可以自动进行飞行路径规划、目标检测和跟踪、计数等任务，无需人工干预。

## 3. 技术路线

无人机计数的技术路线通常包括以下几个步骤：

1. **数据收集**：首先，需要使用无人机在目标区域进行飞行，收集图像或视频数据。这可能涉及到飞行路径规划，以确保覆盖所有的目标区域。

2. **预处理**：收集到的数据可能需要进行一些预处理，例如图像增强（以改善图像质量或对比度），图像裁剪（以减少计算量），或者图像配准（如果从多个视角收集了数据）。

3. **密度图**：密度图是一种将图像的空间信息和目标的数量或概率信息结合起来的有效方法。
    - 在人群计数任务中，密度图可以用来表示图像中每个像素的人头计数。
    - 在目标检测任务中，密度图可以用来表示目标的存在概率。
    - 在目标跟踪任务中，密度图可以用来表示目标在下一帧中的可能位置。
    - 在语义分割任务中，密度图可以用来表示每个像素属于某个类别的概率。

4. **目标检测**：然后，使用目标检测算法在图像中识别和定位目标。这通常涉及到深度学习模型，例如卷积神经网络（CNN）。这些模型需要在标注的训练数据上进行训练，以学习如何识别目标。

5. **目标跟踪**：如果是处理视频数据，那么可能需要进行目标跟踪，以在连续的帧中跟踪目标的运动。

6. **计数**：最后，根据检测到的目标进行计数。这可能涉及到处理重叠目标的问题，因为在高密度的场景中，目标可能会相互遮挡。

7. **后处理和分析**：计数结果可能需要进行后处理和分析，例如统计分析，或者将结果可视化在地图上。

8. **系统优化**：为了实现实时或近实时的计数，可能需要对系统进行优化，例如使用更快的算法，或者使用硬件加速。

## 4. 技术难点

以下是一些关于无人机计数技术难点的论文：

> 《无人机监视中目标检测的研究进展》（A review on object detection in unmanned aerial vehicle surveillance）
>
> - Published: June 2021
> - Link: https://www.sciencedirect.com/science/article/pii/S2666307421000267
> - DOI: 10.1016/j.ijcce.2021.11.005

这篇论文回顾了在无人机监视中进行目标检测的各种方法
作者指出，无人机监视中的目标检测比标准图像中的目标检测更具挑战性，因为无人机图像具有以下特点：

1. 运动物体的动态过渡
2. 宽高比和图像比例的变化
3. 摄像机突然运动
4. 严重的透视失真
5. 运动模糊
6. 物体的高密度
7. 复杂的背景

> 《低空航空数据中目标分类模型的性能评价》（On the performance evaluation of object classification models in low altitude
> aerial data）
> - Published: 05 April 2022
> - Link: https://link.springer.com/article/10.1007/s11227-022-04469-5
> - DOI: 10.1007/s11227-022-04469-5

这篇论文比较了在低空无人机数据中进行目标分类的各种模型的性能，包括机器学习模型和深度学习模型。
作者指出，低空无人机图像的特性与标准图像不同，因此在这种情况下遇到的挑战更加复杂，具体包括：

1. 空中物体的大小变化很大
2. 小物体密集分布
3. 低空航拍图像中物体的朝向可能为任意方向
4. 高照度会使高分辨率图像的暗区曝光不足

> 《检测与追踪遇见无人机挑战》（Detection and Tracking Meet Drones Challenge）
> - Published: 16 Jan 2020
> - Link: https://arxiv.org/abs/2001.06303
> - DOI: 10.1109/TPAMI.2021.3119563

这篇论文介绍了一个新的大规模数据集VisDrone，旨在促进无人机图像上的目标检测和跟踪研究。

数据集包含来自中国14个城市的无人机拍摄的图像，涵盖了城市和农村地区、行人、车辆和自行车等10个常见目标类别，共标注了超过250万个边界框。

值得注意的是，与计算机视觉领域现有的数据集相比，无人机捕捉的视频序列带来了几个新的挑战，如下所述。

- 视角变化：与具有固定视角的监控摄像头相比，装备无人机的摄像头可以从任意视角监控物体。
- 尺度变化：装备无人机的摄像头在不同的高度上监控物体，导致物体尺度的大变化。
- 运动模糊：视频通常在无人机装备的摄像头移动过程中记录，带来了记录视频的大量运动模糊。

> 《DOTA:面向航空图像目标检测的大规模数据集》（DOTA: A Large-scale Dataset for Object Detection in Aerial Images）
> - Published: 18-23 June 2018
> - Link: https://ieeexplore.ieee.org/document/8578516
> - DOI: 10.1109/CVPR.2018.00418

该论文的相关数据集是DOTA Dataset，并指出在航拍图像中进行目标检测与传统目标检测任务之间的主要区别，这些区别主要包括以下几点：

- 航拍图像中物体实例的尺度变化巨大：这不仅因为传感器的空间分辨率，还因为同一物体类别内部的大小变化。
- 航拍图像中常常有许多小的物体实例：例如，港口中的船只和停车场里的汽车。
  此外，航拍图像中实例的频率是不均衡的，例如，一些小尺寸（例如1k ×
  1k）的图像可能包含1900个实例，而一些大尺寸的图像（例如4k × 4k）可能只包含少数几个小实例。
- 航拍图像中的物体通常以任意方向出现：有些实例的长宽比可能极大，如桥梁。

## 5. 全文目录

本报告在左侧导航栏也可查看目录（移动端浏览器可以在左上角点击目录按钮查看目录）

右侧为当前页面的目录，点击可以快速跳转到指定标题。（移动端自动收起到右上角，点击展开）

另外目录栏拥有全文搜索功能，可以快速搜索到相关内容。

<div style="border: #d7d8d9 dashed 1px; border-radius: 8px; padding: 8px;display: flex;flex-wrap: wrap; gap: 8px">

<div>

- [概述]()
- [数据集概述](md/datasets.md)
- [国内外数据集](md/directories/countrywide-datasets.md)
    - [国内外数据集总览](md/datasets/index.md)
    - [VisDrone Dataset](md/directories/vis-drone-datasets.md)
        - [VisDrone 2019](md/datasets/vis-drone/vis-drone-2019.md)
        - [VisDrone DroneAnimal](md/datasets/vis-drone/drone-animal.md)
        - [VisDrone DroneCrowd](md/datasets/vis-drone/drone-crowd.md)
        - [VisDrone DroneRGBT](md/datasets/vis-drone/drone-rgbt.md)
        - [VisDrone DroneVehicle](md/datasets/vis-drone/drone-vehicle.md)
    - [AU-AIR Dataset](md/datasets/au-air/au-air.md)
    - [British Antarctic Survey](md/directories/british-antarctic-survey.md)
        - [Wildlife Colonies Dataset](md/datasets/british-antarctic-survey/01483.md)
    - [COWC Dataset](md/datasets/cowc/cowc.md)
    - [DOTA Images Dataset](md/datasets/dota-images/dota-images.md)
    - [DTB70 Dataset](md/datasets/dtb70/dtb70.md)
    - [HighD Dataset](md/datasets/high-d/high-d.md)
    - [RSD46 Dataset](md/datasets/rsd-46/rsd-46.md)
    - [RSOD Dataset](md/datasets/rsod/rsod.md)
    - [SDD Dataset](md/datasets/stanford-drone-dataset/stanford-drone-dataset.md)
    - [UAV123 Dataset](md/datasets/uav123/uav123.md)
    - [UCAS-AOD Dataset](md/datasets/ucas-aod/ucas-aod.md)
    - [UZAODDataset](md/datasets/uzaodd/uzaodd.md)

</div>

<div>

- [国内外研究团队](md/directories/countrywide-research-team.md)
    - [AISKYEYE](md/teams/aiskyeye.md)
    - [British Antarctic Survey](md/teams/british-antarctic-survey.md)
    - [CAPTAIN](md/teams/captain-whu.md)
    - [IVUL](md/teams/ivul.md)
    - [RSPiP](md/teams/rspip.md)
- [相关工具](md/directories/toolkits.md)
    - [CVAT](md/tools/cvat.md)
    - [DotDotGoose](md/tools/dot-dot-goose.md)
    - [LabelMe](md/tools/labelme.md)
    - [LabelIm](md/tools/labelimg.md)
    - [VIA](md/tools/via.md)
- [相关代码](md/directories/codes.md)
    - [DroneVehicle Annotation to LabelMe](md/codes/drone-vehicle-annotation2labelme.md)
- [标注格式说明](md/directories/annotation-introduction.md)
    - [COCO 标注格式](md/annotations/coco.md)
    - [PASCAL VOC 标注格式](md/annotations/pascal-voc.md)
    - [VisDrone 自有格式](md/directories/annotation-visdrone-format.md)
        - [Multiple Object Tracking](md/annotations/vis-drone/multiple-object-tracking.md)
        - [Object Detection in Images](md/annotations/vis-drone/object-detection-in-images.md)
        - [Object Detection in Videos](md/annotations/vis-drone/object-detection-in-videos.md)
        - [Single Object Tracking](md/annotations/vis-drone/single-object-tracking.md)
    - [YOLO 标注格式](md/annotations/yolo.md)

</div>

</div>

## 6. 参考文献

```
[1] J. C. Hodgson et al., “Drones count wildlife more accurately and precisely than humans,” Methods in Ecology and Evolution, vol. 9, no. 5, pp. 1160–1167, 2018, doi: 10.1111/2041-210X.12974.
[2] Y. Long, Y. Gong, Z. Xiao, and Q. Liu, “Accurate Object Localization in Remote Sensing Images Based on Convolutional Neural Networks,” IEEE Transactions on Geoscience and Remote Sensing, vol. 55, no. 5, pp. 2486–2498, May 2017, doi: 10.1109/TGRS.2016.2645610.
[3] Y. Long, Y. Gong, Z. Xiao, and Q. Liu, “Accurate Object Localization in Remote Sensing Images Based on Convolutional Neural Networks,” IEEE Transactions on Geoscience and Remote Sensing, vol. 55, no. 5, pp. 2486–2498, May 2017, doi: 10.1109/TGRS.2016.2645610.
[4] D. Marchowski, “Drones, automatic counting tools, and artificial neural networks in wildlife population censusing,” Ecology and Evolution, vol. 11, no. 22, pp. 16214–16227, 2021, doi: 10.1002/ece3.8302.
[5] P. Mittal, A. Sharma, R. Singh, and A. K. Sangaiah, “On the performance evaluation of object classification models in low altitude aerial data,” J Supercomput, vol. 78, no. 12, pp. 14548–14570, Aug. 2022, doi: 10.1007/s11227-022-04469-5.
[6] M. Mueller, N. Smith, and B. Ghanem, “A Benchmark and Simulator for UAV Tracking,” in Computer Vision – ECCV 2016, B. Leibe, J. Matas, N. Sebe, and M. Welling, Eds., in Lecture Notes in Computer Science. Cham: Springer International Publishing, 2016, pp. 445–461. doi: 10.1007/978-3-319-46448-0_27.
[7] A. Ramachandran and A. K. Sangaiah, “A review on object detection in unmanned aerial vehicle surveillance,” International Journal of Cognitive Computing in Engineering, vol. 2, pp. 215–228, Jun. 2021, doi: 10.1016/j.ijcce.2021.11.005.
[8] L. Wen et al., “Detection, Tracking, and Counting Meets Drones in Crowds: A Benchmark,” in 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Nashville, TN, USA: IEEE, Jun. 2021, pp. 7808–7817. doi: 10.1109/CVPR46437.2021.00772.
[9] G.-S. Xia et al., “DOTA: A Large-Scale Dataset for Object Detection in Aerial Images,” in 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition, Jun. 2018, pp. 3974–3983. doi: 10.1109/CVPR.2018.00418.
[10] Z. Xiao, Q. Liu, G. Tang, and X. Zhai, “Elliptic Fourier transformation-based histograms of oriented gradients for rotationally invariant object detection in remote-sensing images,” International Journal of Remote Sensing, vol. 36, no. 2, pp. 618–644, Jan. 2015, doi: 10.1080/01431161.2014.999881.
[11] Z. Xiao, Y. Long, D. Li, C. Wei, G. Tang, and J. Liu, “High-Resolution Remote Sensing Image Retrieval Based on CNNs from a Dimensional Perspective,” Remote Sensing, vol. 9, no. 7, Art. no. 7, Jul. 2017, doi: 10.3390/rs9070725.
[12] H. Zhu, X. Chen, W. Dai, K. Fu, Q. Ye, and J. Jiao, “Orientation robust object detection in aerial images using deep convolutional neural network,” in 2015 IEEE International Conference on Image Processing (ICIP), Sep. 2015, pp. 3735–3739. doi: 10.1109/ICIP.2015.7351502.
[13] P. Zhu et al., “Detection and Tracking Meet Drones Challenge.” arXiv, Oct. 03, 2021. doi: 10.48550/arXiv.2001.06303.
[14] “Drones Offer Ability to Find, ID and Count Marine Megafauna,” NC State News. https://news.ncsu.edu/2018/11/drones-marine-megafauna/ (accessed Jul. 28, 2023).
```







