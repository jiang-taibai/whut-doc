import pyautogui
import pyperclip
from pynput import keyboard
import logging
import requests

# 配置日志格式和级别
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class AutoLectureProgram:
    local_version = "v1.0.0"
    current_keys = set()
    key_mapping = {
        keyboard.KeyCode.from_char('q'): "Q",
        keyboard.KeyCode.from_char('`'): "`",
    }

    def __init__(self, form_datas, hot_key_to_run=None, hot_key_to_exit=None, options=None):
        # 表单信息：分别为姓名、班级、学号
        self.form_datas = form_datas
        # 快捷键：可以自行修改，但如果是控制字符，就比较复杂了，我只用了很简单的两个字符来控制程序启动和停止
        self.hot_key_to_run = hot_key_to_run or {keyboard.KeyCode.from_char('`')}
        self.hot_key_to_exit = hot_key_to_exit or {keyboard.KeyCode.from_char('q')}
        default_options = {
            "reset_before_fill": False,
        }
        default_options.update(options)
        self.options = default_options
        self.interested_keys = self.hot_key_to_run | self.hot_key_to_exit

    def detect_update(self):
        """
        检测更新
        """
        url = "https://doc.coderjiang.com/whut/auto-lecture/src/json/version.json"
        try:
            # 1. 使用 requests 库获取 JSON 文本
            response = requests.get(url)
            data = response.json()

            # 2. 从 JSON 文本中提取最新版本
            latest_version = data["latest"]

            # 3. 比较本地版本和最新版本
            if self.local_version < latest_version:
                logging.info(f"本地版本 {self.local_version} 低于最新版本 {latest_version}")
            else:
                logging.info(f"本地版本 {self.local_version} 是最新版本")

        except Exception as e:
            logging.error("检测更新失败，原因如下：")
            logging.error(e)
            logging.error(f"当前版本为 {self.local_version}，请打开链接手动检查更新：{url}")

    def on_press(self, key):
        """
        按下键盘时触发的事件
        :param key: 按下的键位
        """
        # 将按下的键位添加到 current_keys 中
        if key in self.interested_keys:
            logging.debug("按下了: %s" % key)
            self.current_keys.add(key)

        # 检测是否按下了快捷键
        if self.is_quick_key_pressed(self.hot_key_to_run):
            logging.info("检测到按下了快捷键: %s" % self.descript_quick_key(self.hot_key_to_run))
            self.current_keys.clear()
            self.auto_complete_form()
        elif self.is_quick_key_pressed(self.hot_key_to_exit):
            logging.info("检测到按下了快捷键: %s" % self.descript_quick_key(self.hot_key_to_exit))
            self.current_keys.clear()
            logging.info("程序退出")
            exit(0)

    def is_quick_key_pressed(self, quick_key):
        """
        检测是否按下了快捷键，当且仅当所有快捷键都按下，且没有其他键按下时，返回 True
        :return: 是否按下了快捷键
        """
        return self.current_keys == quick_key

    def on_release(self, key):
        """
        释放键盘时触发的事件
        :param key: 释放的键位
        """
        try:
            # 将释放的键位从 current_keys 中移除
            self.current_keys.remove(key)
            logging.debug("释放了: %s" % key)
        except KeyError:
            # Key 不在集合中，就忽略它
            pass

    def auto_complete_form(self):
        """
        执行自动化操作
        """
        logging.info("开始自动化操作")
        for i in range(len(self.form_datas)):
            pyautogui.press('tab')
            self.fill_textarea(self.form_datas[i])
        logging.info("自动化操作完成")

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

    def descript_quick_key(self, quick_key):
        """
        将快捷键转换为字符串
        :return: 快捷键的字符串描述
        """
        return ' + '.join([self.key_mapping[k] for k in quick_key if k in self.key_mapping])


class AuxiliaryProgram:

    @staticmethod
    def hello_world(quick_key_to_run_text, quick_key_to_exit_text):
        brief = f"""
        欢迎使用 I ♥ Lecture，这是一个自动化填写表单的小工具。
        使用方法：
            1. 守着 院群 里的通知，等待院科协发布讲座在线报名的收集表。你可以狂点聊天框的空白处，以便第一时间打开。
            2. 当表单加载完成后，【请点击一下表单空白处，以获得表单的聚焦状态】
            3. 按下启动快捷键 "{quick_key_to_run_text}"，即可自动填写表单。
            4. 自行完成选择年级的下拉框，目前还未实现自动化。
            5. 提交表单。
            6. 按下退出快捷键 "{quick_key_to_exit_text}"，即可退出程序。
        希望你能喜欢这个极其简陋的小工具，如果有任何问题，欢迎联系我。
        
        测试表单：https://docs.qq.com/form/page/DVkxxT09DcHlCbkhi
        
        """
        print(AuxiliaryProgram.add_full_border(brief))
        print()

    @staticmethod
    def add_full_border(text):
        lines = text.split('\n')
        max_length = max(AuxiliaryProgram.count_chinese_chars(line) for line in lines)

        # 定义边框字符
        horizontal = '─'
        vertical = '│'
        top_left = '┌'
        top_right = '┐'
        bottom_left = '└'
        bottom_right = '┘'

        # 创建边框
        top_border = top_left + horizontal * (max_length + 2)
        bottom_border = bottom_left + horizontal * (max_length + 2)
        bordered_lines = [vertical + '  ' + line.ljust(max_length) + '  ' for line in lines]

        return '\n'.join([top_border] + bordered_lines + [bottom_border])

    @staticmethod
    def count_chinese_chars(s):
        count = 0
        for char in s:
            # 使用 Unicode 范围来判断字符是否为中文
            if '\u4e00' <= char <= '\u9fff':
                count += 2
            else:
                count += 1
        return count


def main():
    form_datas = ["刘江", "专硕236班", "2023305193"]
    # 快捷键，可以自行修改，但如果是控制字符，就比较复杂了，需要改代码，我只用了很简单的两个字符来控制程序启动和停止
    hot_key_to_run = {keyboard.KeyCode.from_char('`')}
    hot_key_to_exit = {keyboard.KeyCode.from_char('q')}
    options = {
        "reset_before_fill": False,
    }

    program = AutoLectureProgram(form_datas, hot_key_to_run, hot_key_to_exit, options)

    AuxiliaryProgram.hello_world(program.descript_quick_key(hot_key_to_run),
                                 program.descript_quick_key(hot_key_to_exit))

    program.detect_update()

    with keyboard.Listener(on_press=program.on_press, on_release=program.on_release) as listener:
        logging.info("程序已启动，正在监听快捷键...")
        logging.info(f"按下 {program.descript_quick_key(hot_key_to_run)} 启动自动化")
        logging.info(f"按下 {program.descript_quick_key(hot_key_to_exit)} 退出程序")
        listener.join()


if __name__ == '__main__':
    main()
