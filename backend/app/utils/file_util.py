import json
import os

class AeroDataProcessor:
    """
    【气动数据处理器】
    作用：把乱糟糟的文本文件，转换成规整的 JSON 格式
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def read_txt(self):
        """读取文本文件内容"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                return content
        except FileNotFoundError:
            return "Error: 文件没有找到，请检查路径！"

    def save_as_json(self, data, output_name):
        """将数据保存为标准 JSON 格式"""
        with open(output_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"数据已成功存档至: {output_name}")
