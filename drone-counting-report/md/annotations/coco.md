# COCO 标注格式

COCO（Common Objects in Context）是一个大型的、丰富的物体检测，分割和字幕数据集。该数据集鼓励算法的研究和开发，提升人们对场景理解的深度。COCO数据集的标注格式较为复杂，下面我们将详细介绍。

## 1. COCO标注概览

COCO数据集的标注信息存储在一个JSON文件中。JSON文件的最外层是一个字典，包含五个主要的键值对：'images', 'annotations', '
categories', 'licenses' 和 'info'。

### (1) `images`

这部分包含了数据集中所有图像的相关信息。每一张图像又是一个字典，包含以下字段：

- `id`： 图像的唯一ID
- `width`： 图像的宽度（像素）
- `height`： 图像的高度（像素）
- `file_name`： 图像的文件名
- `license`： 图像的版权许可信息的ID
- `date_captured`： 图像的捕获日期

### (2) `annotations`

这部分包含了数据集中所有的标注信息。每一个标注也是一个字典，包含以下字段：

- `id`： 标注的唯一ID
- `image_id`： 对应图像的ID
- `category_id`： 对应类别的ID
- `segmentation`： 物体的分割信息，可以是一个二维的mask（RLE编码后的结果）或者是一组代表边缘的点（边缘多边形）
- `area`： 物体的面积（像素）
- `bbox`： 物体的边界框，格式为 `[x,y,width,height]`，其中`(x,y)`是左上角的坐标
- `iscrowd`： 表示该物体是否是一组无法单独标注的物体的聚集体

### (3) `categories`

这部分包含了所有的类别信息。每一个类别也是一个字典，包含以下字段：

- `id`： 类别的唯一ID
- `name`： 类别的名称
- `supercategory`： 类别的上级类别

### (4) `licenses`

这部分包含了所有的版权许可信息。每一个许可也是一个字典，包含以下字段：

- `id`： 版权许可的唯一ID
- `name`： 版权许可的名称
- `url`： 版权许可的URL

### (5) `info`

这部分包含了数据集的一些基本信息，例如数据集的版本、网址、发布日期等。

## 2. 示例

下面是COCO数据集的一个标注示例：

```json
{
  "info": {},
  "images": [
    {
      "file_name": "000000391895.jpg",
      "height": 360,
      "width": 640,
      "id": 391895
    }
  ],
  "annotations": [
    {
      "segmentation": [
        [
          510.66,
          423.01,
          511.72,
          420.03,
          510.45,
          423.01
        ]
      ],
      "area": 702.1057499999998,
      "iscrowd": 0,
      "image_id": 289343,
      "bbox": [
        473.07,
        395.93,
        38.65,
        28.67
      ],
      "category_id": 18,
      "id": 1768
    }
  ],
  "categories": [
    {
      "supercategory": "person",
      "id": 1,
      "name": "person"
    },
    {
      "supercategory": "vehicle",
      "id": 2,
      "name": "bicycle"
    }
  ]
}
```