# British Antarctic Survey

## 1. 团队介绍

官网：[https://www.bas.ac.uk/](https://www.bas.ac.uk/)

英国南极调查局(British Antarctic Survey, 简称BAS)是一家在南极实施科研的机构，它对南极的研究涵盖了地质、大气科学、生物学以及许多其他领域。
该机构于1945年由英国政府建立，并自此为全球提供关于南极大陆与南极洋的重要信息。近年来，BAS也在无人机计数领域取得了显著的成果。

BAS的主要研究方向包括环境科学、气候变化、海洋生态学及地球科学等多个领域。
这些研究对于理解我们的地球以及其快速变化的环境尤其重要。
例如，他们的气候科学研究有助于我们理解全球气候变化的程度及其潜在影响，而他们的海洋生态学研究则揭示了南极洋生物的多样性以及生态系统的复杂性。

## 2. 无人机计数领域的研究

在无人机计数领域，BAS也有引人注目的成果。
他们开发并使用了高级无人机系统，以实现对南极地区动植物群落的精确计数。
这些无人机装备有高分辨率的摄像头和先进的影像识别技术，能在空中对动物进行详细的观察并进行精确计数。

例如，BAS的科学家们曾利用这种无人机技术对南极的企鹅种群进行了全面的计数。
他们发现，传统的人工计数方法存在一定的误差，而使用无人机进行计数可以显著提高计数的准确性。此外，这种方法还可以最小化人为干扰，保护这些珍贵生物的生存环境。

来源：[https://www.bas.ac.uk/media-post/drones-effective-method-for-counting-seabirds/](https://www.bas.ac.uk/media-post/drones-effective-method-for-counting-seabirds/)

<div class="custom-img-group">
    <img src="https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/teams/british-antarctic-survey/uav-at-signy.jpg" alt="uav-at-signy.jpg"/>
    <img src="https://cdn.coderjiang.com/doc/whut/uav-counting-investigation-report/teams/british-antarctic-survey/signy-uav-ops2017-gourlay-at-6.jpg" alt="signy-uav-ops2017-gourlay-at-6.jpg">
</div>

## 3. 设备与技术

> 此处引用[Wildlife Colonies 数据集](md/datasets/british-antarctic-survey/01483.md)中的设备与技术

- 数据采集: 大疆无人机 2 Pro
- 无人机飞行软件: DJI GO4 app
- 图像管理: Adobe Lightroom CC 10.0
- 图像处理: Agisoft Metashape
- 图像标注: DotDotGoose

- DotDotGoose 标注工具：
  [https://biodiversityinformatics.amnh.org/open_source/dotdotgoose](https://biodiversityinformatics.amnh.org/open_source/dotdotgoose)
- Agisoft 图像处理软件：
  [https://www.agisoft.com](https://www.agisoft.com)

## 3. 相关数据集

### (1) 2019-2020 年南乔治亚岛和南桑威奇群岛野生动物栖息地的无人机图像

已收录至：[Wildlife Colonies 数据集](md/datasets/british-antarctic-survey/01483.md)

### (2) 2016-2018年，南奥克尼群岛西格尼岛的巴布亚企鹅和chinstrap企鹅和南乔治亚群岛的shag殖民地的处理过的无人机(UAV)图像

Link: [https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01604](https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01604)

通过使用多旋翼无人驾驶飞行器（UAVs）进行低空航拍，收集了南奥克尼群岛Signy岛上的鸟类群落的图片。

本研究中包括了三种物种：

- 南极企鹅（Pygoscelis antarctica）
- 颏带企鹅（Pygoscelis papua）
- 南乔治亚鸬鹚(Leucocarbo atriceps georgianus)

数据是在2016/17和2017/18的野外季节中收集的。通过将单张图片拼接在一起，为调查中的多帧群体创建了马赛克图像。

### (3) 2019年到2020年12月至2月期间，使用运动结构生成的影像，收集了南三文治群岛上的阿德利企鹅、颏带企鹅、巴布亚企鹅和马可罗尼企鹅的巢穴位置坐标和数量。

Link: [https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01556](https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01556)

这个数据集包含了2019年12月至2020年2月期间在南三文治群岛通过无人驾驶飞行器（UAV）收集的企鹅调查数据和影像。
它包括调查地点的正射影像图（orthotiffs）和数字高程模型（DEMS）、企鹅群落的地理轮廓、个别物种的巢穴坐标、混合物种的子群落和群组（在这些地方无法进行物种级别的识别）。
最后，它还包括了每个地点不同类别的总计数，以及由于正射影像图的某些部分产生失真而未能计数的巢穴的估计。

这些正射影像图和数字高程模型是通过使用结构光从运动（SfM）——一种三维（3D）渲染技术产生的，然后被加载到QGIS中，以手动提取颏带企鹅、阿德利企鹅、巴布亚企鹅和马可罗尼企鹅的巢穴坐标。
在无法计数巢穴的地方，采用在现场进行过计数的区域来计算可能存在的巢穴的估计值。

这个数据集是由牛津大学极地生态和保护小组的研究人员收集的，目标是通过对这些地点进行调查并更新南三文治群岛上的当前种群评估，从而帮助保护政策，并推动监测技术和能力的提升。

南三文治群岛的考察活动得到了南乔治亚和南三文治群岛政府的支持，并由约翰·埃勒曼基金会以及Quark Expeditions船上乘客的捐款资助。

### (4) 2016-2018年南奥克尼群岛Signy岛上由无人驾驶飞行器（UAV）收集的巴布亚企鹅、颏带企鹅以及南乔治亚鸬鹚群体的数量统计

通过使用多旋翼无人驾驶飞行器（UAV）进行的低空航空摄影收集的图像，手动计算了筑巢鸟类的数量。

这项研究包括了三个物种:

- 巴布亚企鹅（Pygoscelispapua）
- 颏带企鹅（Pygoscelis antarctica）
- 南乔治亚鸬鹚（Leucocarbo atriceps georgianus）

数据是在2016/17和2017/18的野外季节中收集的。

### (5) 更多

可在官网数据集搜索平台进行搜索：[https://data.bas.ac.uk/search.php](https://data.bas.ac.uk/search.php)
