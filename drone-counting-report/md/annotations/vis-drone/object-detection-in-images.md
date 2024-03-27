# Object Detection in Images

## 1. 概述

官网：[https://github.com/VisDrone/VisDrone2018-DET-toolkit](https://github.com/VisDrone/VisDrone2018-DET-toolkit)

- 来源：VisDrone2018 图像中对象检测 (DET) 竞赛开发套件挑战赛的文档。
- 格式说明：基于PASCAL VOC[1]和MS-COCO[2]平台进行了修改。
- 工具包：代码在Windows 10和macOS Sierra 10.12.6系统上，Matlab 2013a/2014b/2016b/2017b平台上进行了测试。
- 数据集：对于DET竞赛，有三组数据和标签:训练数据、验证数据和测试挑战数据。这三个集合之间没有重叠。

## 2. 工具包介绍

evalDET.m 是用于评估检测器的主要函数 - 请修改数据集路径和结果路径 - 使用“isImgDisplay”显示真实值和检测结果

评估中将不考虑被忽略区域或标记为“其他”的检测。

```text
VisDrone2018-DET-toolkit-master/
│  evalDET.m
│  README.md
│
└─utils
        calcAccuracy.m
        compOas.m
        createIntImg.m
        displayImage.m
        dropObjectsInIgr.m
        evalRes.m
        findImageList.m
        saveAnnoRes.m
        VOCap.m
```

## 3. 标注介绍

每一个标注文件对应一个图像，文件名相同。

每个标注文件`x.txt`含有若干行，每一行格式如下：

```text
<bbox_left>,<bbox_top>,<bbox_width>,<bbox_height>,<score>,<object_category>,<truncation>,<occlusion>
# 例如
345,163,37,18,1,4,0,0
384,164,26,22,1,4,0,1
43,398,18,17,1,10,0,1
324,167,14,6,1,3,0,0
362,143,30,18,1,4,1,0
```

| Name                | Description                                                                                                                                             |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<bbox_left>`       | 预测边界框左上角的x坐标                                                                                                                                            |
| `<bbox_top>`        | 预测对象边界框左上角的y坐标                                                                                                                                          |
| `<bbox_width>`      | 预测对象边界框的像素宽度                                                                                                                                            |
| `<bbox_height>`     | 预测对象边界框的高度，单位为像素                                                                                                                                        |
| `<score>`           | 检测文件中的分数表示包含对象实例的预测边界框的置信度。GROUNDTRUTH文件中的分数设置为1或0。1表示计算时考虑边界框，0表示忽略边界框。                                                                                |
| `<object_category>` | 对象类别表示被标注对象的类型(即被忽略的区域(0)，pedestrian(1)， people(2)， bicycle(3)， car(4)， van(5)， truck(6)， tricycle(7)， awn -tricycle(8)， bus(9)， motor(10)， others(11)) |
| `<truncation>`      | 检测结果文件中的分数应该设置为常数-1。GROUNDTRUTH文件中的分数表示对象部分出现在帧外的程度(即没有截断= 0(截断率0%)，部分截断= 1(截断率1% ~ 50%))。                                                              |
| `<occlusion>`       | 检测文件中的得分应该设置为常数-1。GROUNDTRUTH文件中的分数表示对象被遮挡的比例(即无遮挡= 0(遮挡率0%)，部分遮挡= 1(遮挡率1% ~ 50%)，重度遮挡= 2(遮挡率50% ~ 100%))。                                              |

## 4. 版权信息

If you use our toolkit or dataset, please cite our paper as follows:

```text
@article{zhuvisdrone2018,
    title={Vision Meets Drones: A Challenge},
    author={Zhu, Pengfei and Wen, Longyin and Bian, Xiao and Haibin, Ling and Hu, Qinghua},
    journal={arXiv preprint:1804.07437},
    year={2018}
}
@InProceedings{Zhu_2018_ECCV_Workshops, 
    author = {Zhu, Pengfei and Wen, Longyin and Du, Dawei and Bian, Xiao and Ling, Haibin and Hu, Qinghua and Nie, Qinqin and Cheng, Hao and Liu, Chenfeng and Liu, Xiaoyu and Ma, Wenya and Wu, Haotian and Wang, Lianjie and Schumann, Arne and Brown, Chase and Qian, Chen and Li, Chengzheng and Li, Dongdong and Michail, Emmanouil and Zhang, Fan and Ni, Feng and Zhu, Feng and Wang, Guanghui and Zhang, Haipeng and Deng, Han and Liu, Hao and Wang, Haoran and Qiu, Heqian and Qi, Honggang and Shi, Honghui and Li, Hongliang and Xu, Hongyu and Lin, Hu and Kompatsiaris, Ioannis and Cheng, Jian and Wang, Jianqiang and Yang, Jianxiu and Zhou, Jingkai and Zhao, Juanping and Joseph, K. J. and Duan, Kaiwen and Suresh, Karthik and Bo, Ke and Wang, Ke and Avgerinakis, Konstantinos and Sommer, Lars and Zhang, Lei and Yang, Li and Cheng, Lin and Ma, Lin and Lu, Liyu and Ding, Lu and Huang, Minyu and Kumar Vedurupaka, Naveen and Mamgain, Nehal and Bansal, Nitin and Acatay, Oliver and Giannakeris, Panagiotis and Wang, Qian and Zhao, Qijie and Huang, Qingming and Liu, Qiong and Cheng, Qishang and Sun, Qiuchen and Laganire, Robert and Jiang, Sheng and Wang, Shengjin and Wei, Shubo and Wang, Siwei and Vrochidis, Stefanos and Wang, Sujuan and Lee, Tiaojio and Sajid, Usman and Balasubramanian, Vineeth N. and Li, Wei and Zhang, Wei and Wu, Weikun and Ma, Wenchi and He, Wenrui and Yang, Wenzhe and Chen, Xiaoyu and Sun, Xin and Luo, Xinbin and Lian, Xintao and Li, Xiufang and Kuai, Yangliu and Li, Yali and Luo, Yi and Zhang, Yifan and Liu, Yiling and Li, Ying and Wang, Yong and Wang, Yongtao and Wu, Yuanwei and Fan, Yue and Wei, Yunchao and Zhang, Yuqin and Wang, Zexin and Wang, Zhangyang and Xia, Zhaoyue and Cui, Zhen and He, Zhenwei and Deng, Zhipeng and Guo, Zhiyao and Song, Zichen}, 
    title = {VisDrone-DET2018: The Vision Meets Drone Object Detection in Image Challenge Results},
    booktitle = {The European Conference on Computer Vision (ECCV) Workshops}, 
    month = {September}, 
    year = {2018}
}
```