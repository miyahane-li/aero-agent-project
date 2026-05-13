import json  # 引入处理 JSON 格式的工具包
import os  # 引入处理电脑路径的工具包


class AeroDataProcessor:
    """
    【气动数据处理器】
    作用：把乱糟糟的文本文件，转换成规整的 JSON 格式
    """

    def __init__(self, file_path):
        # file_path: 你想要处理的文件路径
        self.file_path = file_path

    def read_txt(self):
        """读取文本文件内容"""
        try:
            # 'r' 代表只读模式，encoding='utf-8' 确保中文不乱码
            with open(self.file_path, "r", encoding="utf-8") as f:
                content = f.read()
                return content
        except FileNotFoundError:
            # 如果文件找不着，返回一个友好的提示
            return "Error: 文件没有找到，请检查路径！"

    def save_as_json(self, data, output_name):
        """将数据保存为标准 JSON 格式"""
        # data: 要保存的字典数据；output_name: 保存后的文件名
        with open(output_name, "w", encoding="utf-8") as f:
            # indent=4 让 JSON 看起来有漂亮的缩进
            # ensure_ascii=False 确保中文能正常显示
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"数据已成功存档至: {output_name}")
