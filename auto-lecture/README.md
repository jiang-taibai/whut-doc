# 1. 前面的言 🤗

试过多种办法，在 Web Console 中似乎不怎么方便操作 DOM 节点（腾讯做了手脚，我没找到方法），因此只能退居二线，尝试在操作系统层面上模拟键鼠操作。

本文阐述了一种基于 PyAutoGUI 的自动化脚本，可以实现自动聚焦三个输入框（分别是姓名、班级和学号）再自动填写相应的内容。

**目前还没有实现选中下拉框的功能**，如果有大佬有更牛的方法，希望能够指点一二。

这篇文章就算是抛砖引玉了，希望能够帮助到大家。

---

> **免责声明 🤯**
> 
> 本脚本基于前几次的讲座报名收集表定制，为三个输入框、一个下拉框的组合。文末有一个测试表，你可以熟悉一下。  
> 如果以后某次的收集表不是这种模板，那么本脚本需要相对于的修改。在使用前请务必清楚收集表的模板是不是 `[姓名、班级、学号]` 为输入框的组合。  
> 如果有新版收集表，本文档也会及时更新。

# 2. 演示视频 🎥

下述视频展示了从激活环境、运行脚本、启动报名表单到自动填写的过程。

建议全屏观看。

<video width="100%" controls>
  <source src="https://cdn.coderjiang.com/doc/whut/i-love-lecture/video/presentation.mp4" type="video/mp4">
</video>

有些名称和下文不一致，但是应该不会影响理解的。

# 3. 项目下载 🛒

| 版本     | 链接                                                                                                                 | 备注                      |
|--------|--------------------------------------------------------------------------------------------------------------------|-------------------------|
| v1.0.0 | [i-love-lecture-v1.0.0.zip](https://cdn.coderjiang.com/doc/whut/i-love-lecture/releases/i-love-lecture-v1.0.0.zip) | 适用于 [姓名、班级、学号] 为输入框的收集表 |

# 4. 环境安装 🛠

## 4.1 虚拟环境

首先，我们需要创建一个虚拟环境，以免污染全局环境。

```bash
conda create -n i_love_lecture python=3.8
conda activate i_love_lecture
```

## 4.2 安装依赖

接着，我们需要安装依赖。`requirements.txt` 在压缩包内。

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

这里毛遂自荐一下我的 [Development Booster](https://github.com/jiang-taibai/development-booster) 项目，可以帮助你快速切换国内源。😇😇

GitHub 打不开可以使用 Gitee 地址：[https://gitee.com/jiang-taibai/development-booster](https://gitee.com/jiang-taibai/development-booster)

# 5. 快速开始 🚀

## 5.1 修改信息

拿到脚本后，你需要修改脚本中的姓名、班级和学号

```python
# Other code......

def main():
    # 你需要修改为你的名字、班级和学号
    form_datas = ["张三", "专硕236班", "2023305000"]
    
    # Other code......
```

## 5.2 运行脚本

在虚拟环境中运行脚本

```bash
conda activate i_love_lecture
python i_love_lecture.py
```

如果运行正常，你将会看到如下输出

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│                                                                                                                   
│    欢迎使用 I ♥ Lecture，这是一个自动化填写表单的小工具。                                                                        
│    使用方法：                                                                                                    
│        1. 守着 院群 里的通知，等待院科协发布讲座在线报名的收集表。你可以狂点聊天框的空白处，以便第一时间打开。                                               
│        2. 当表单加载完成后，【请点击一下表单空白处，以获得表单的聚焦状态】                                                                  
│        3. 按下启动快捷键 "`"，即可自动填写表单。                                                                             
│        4. 自行完成选择年级的下拉框，目前还未实现自动化。                                                                           
│        5. 提交表单。                                                                                             
│        6. 按下退出快捷键 "Q"，即可退出程序。                                                                               
│    希望你能喜欢这个极其简陋的小工具，如果有任何问题，欢迎联系我。                                                                          
│                                                                                                                   
│    测试表单：https://docs.qq.com/form/page/DVkxxT09DcHlCbkhi                                                     
│                                                                                                                   
│                                                                                                                   
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
2023-10-20 16:52:21 - INFO - 本地版本 v1.0.0 是最新版本
2023-10-20 16:52:21 - INFO - 程序已启动，正在监听快捷键......
2023-10-20 16:52:21 - INFO - 按下 ` 启动自动化
2023-10-20 16:52:21 - INFO - 按下 Q 退出程序
```

## 5.3 启动表单

在院群等待发报名表，你只需要在空白处疯狂点击，以便第一时间打开表单。

![](https://cdn.coderjiang.com/doc/whut/i-love-lecture/img/main_01.png)

## 5.4 启动自动化

当表单加载完成后，**你需要点击一下表单空白处，以获得表单的聚焦状态。**

然后再按下启动快捷键 "`"，即可自动填写表单。

接着你需要手动完成选择年级的下拉框，目前还未实现自动化。

最后提交表单。

---

多插一嘴，请勿嫌烦😂。为了文档的完整性，说明一下 "`" 的位置在哪：

![](https://cdn.coderjiang.com/doc/whut/i-love-lecture/img/main_03.png "\"`\"快捷键位置")

## 5.5 退出程序

按下退出快捷键 "Q"，即可退出程

# 6. 自行测试 🧐

我做了一个类似的报名表，你可以在这里测试。

https://docs.qq.com/form/page/DVkxxT09DcHlCbkhi

并且已经开放了修改、删除、匿名提交，你可以随意测试。

![](https://cdn.coderjiang.com/doc/whut/i-love-lecture/img/main_02.png)

# 7. 进阶使用 🛸

## 7.1 输入前重置

> 其实一般情况下，你不需要这个功能。该功能会在填写前，先清空输入框，再填写，严重影响填写速度。
> 
> 而新表单要填写时，输入框是空白的无需清空。

代码如下，你可以修改 `reset_before_fill` 的值为 `True`，以在填写前重置输入框。

```python
def main():
    # Other code......
    
    options = {
        "reset_before_fill": False,
    }
    
    # Other code......
```

原理即模拟按下 `Ctrl+A` 后按 `Delete`，代码如下：

```python
def fill_textarea(self, text):
    """
    使用 pyautogui 模拟键盘输入。如果直接输入的话，会有问题，所以先复制到剪贴板，再粘贴
    :param text: 输入的文本
    """
    if self.options["reset_before_fill"]:
        logging.info("正在清空输入框")
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')
    logging.info("正在输入: %s" % text)
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
```

## 7.2 自定义快捷键

你可以修改 `hot_key_to_run` 和 `hot_key_to_exit` 的值，以自定义快捷键。

`hot_key_to_run` 和 `hot_key_to_exit` 的类型都是 `set`

```python
def main():
    # Other code......
    
    # 快捷键，可以自行修改，但如果是控制字符，就比较复杂了，需要改代码，我只用了很简单的两个字符来控制程序启动和停止
    hot_key_to_run = {keyboard.KeyCode.from_char('`')}
    hot_key_to_exit = {keyboard.KeyCode.from_char('q')}
    
    # Other code......
```

但需要注意的是，如果你想弄组合式快捷键，例如 `Ctrl+Shift+Q` 来退出程序，那你需要修改代码，因为 `Ctrl+Q` 不能监听到 `Q` 了，而会监听到 `Ctrl+Q` 的特殊字符。

具体的代码我尚未实现，因为这不是本脚本的重点。

第二步，你需要为你的快捷键添加映射，以便能够在代码中提示快捷键信息（不影响监听）

```python
class AutoLectureProgram:
    
    # Other code......

    key_mapping = {
        keyboard.KeyCode.from_char('q'): "Q",
        keyboard.KeyCode.from_char('`'): "`",
    }

    # Other code......
    
```

# 8. 常见问题 😵

## 8.1 第一个填的为什么是表单标题？

该脚本的原理是通过使用 Table 键切换输入框来实现文本的键入。

**你需要点击一下表单空白处，以获得表单的聚焦状态。**

如果不点击，那么就会聚焦到浏览器上，会发生不确定的事情，不同的浏览器第一个聚焦的位置都不一样。

![](https://cdn.coderjiang.com/doc/whut/i-love-lecture/img/ques_01.png "BUG示例图-聚焦到标题")

# 9. ChangeLog

## 2023-10-20 doc_1.0.0

完成第一版文档，发布 v1.0.0 版本。


