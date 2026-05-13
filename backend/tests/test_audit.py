import os
from app.utils.http_util import AeroHttpSender


def test_http_audit_logging():
    """验证发送请求时，日志文件是否产生了记录"""
    sender = AeroHttpSender()
    # 故意请求一个不存在的地址来触发错误日志
    sender.safe_post("https://invalid-api-test.com", data={"test": "data"})

    # 检查 logs 文件夹和 app.log 是否生成
    assert os.path.exists("logs/app.log")

    # 读取日志最后一行，检查是否包含我们定义的错误关键词
    with open("logs/app.log", "r", encoding="utf-8") as f:
        content = f.read()
        assert "请求发生异常" in content
