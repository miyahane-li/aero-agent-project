import os  # 用于处理操作系统相关的任务，比如读取文件名
from app.core.logger import logger  # 引入昨天的黑匣子日志

class AeroFileProcessor:
    """
    【气动智能体文件处理中心】
    负责扫描数据目录，批量读取文本内容
    """
    
    def __init__(self, base_path="data/raw_docs"):
        # 设置默认的数据存放路径
        self.base_path = base_path
        # 确保路径存在，如果不存在就创建一个
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
            logger.info(f"📁 已自动创建数据目录: {self.base_path}")

    def collect_files(self, extension=".txt"):
        """
        扫描目录下所有指定后缀的文件
        :param extension: 文件后缀名，如 .txt 或 .dat
        :return: 文件路径列表
        """
        file_list = []
        # os.walk 会递归进入每一个子文件夹
        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                if file.endswith(extension):
                    # 将文件夹路径和文件名组合成完整路径
                    full_path = os.path.join(root, file)
                    file_list.append(full_path)
        
        logger.info(f"🔍 扫描完成，共找到 {len(file_list)} 个 {extension} 文件")
        return file_list

    def read_all_contents(self, file_paths):
        """
        批量读取文件内容并存入字典
        :param file_paths: 文件路径列表
        :return: 字典 {文件名: 文件内容}
        """
        data_map = {}
        for path in file_paths:
            try:
                # 使用 utf-8 编码读取，防止中文乱码
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # 提取文件名作为 Key
                    file_name = os.path.basename(path)
                    data_map[file_name] = content
                    logger.info(f"📖 成功读取: {file_name}")
            except Exception as e:
                logger.error(f"❌ 读取文件 {path} 失败: {str(e)}")
        
        return data_map