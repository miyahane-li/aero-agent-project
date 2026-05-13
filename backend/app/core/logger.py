import logging  # 引入 Python 内置的日志工具
import os  # 用于处理文件夹路径


def setup_logger():
    """
    【气动智能体全链路审计配置】
    作用：初始化日志系统，将程序的运行记录同时打印到屏幕并保存到文件
    """
    # 确保日志文件夹存在
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # 创建一个日志记录器 (Logger)
    logger = logging.getLogger("AeroAgent")
    logger.setLevel(logging.INFO)  # 设置级别为 INFO，记录重要信息

    # 定义日志的显示格式：时间 - 名字 - 级别 - 内容
    # 这种格式符合 SCI 论文数据记录的严谨性要求
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # 1. 创建控制台处理器：让日志显示在黑窗口里
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # 2. 创建文件处理器：将日志保存到 logs/app.log 文件中，方便后续追责或调试
    file_handler = logging.FileHandler("logs/app.log", encoding="utf-8")
    file_handler.setFormatter(formatter)

    # 将两个处理器都添加到记录器中
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# 实例化，方便其他文件直接调用
logger = setup_logger()
