import requests
from app.core.logger import logger  # 引入我们刚才写的黑匣子


class AeroHttpSender:
    def __init__(self, timeout=15):
        self.timeout = timeout

    def safe_post(self, url, data=None):
        """
        发送 POST 请求并进行全链路审计
        """
        logger.info(f"🚀 正在请求 API: {url}")  # 在日志中记录请求开始
        try:
            # 发送请求
            response = requests.post(url, json=data, timeout=self.timeout)

            # 记录返回的状态码
            logger.info(f"✅ 响应成功 | 状态码: {response.status_code}")

            # 检查响应头是否为 JSON 格式
            if "application/json" in response.headers.get("Content-Type", ""):
                return response.json()
            else:
                logger.warning("⚠️ 响应内容不是 JSON 格式")
                return response.text

        except Exception as e:
            # 如果出错了，用 error 级别记录下具体的错误原因
            logger.error(f"❌ 请求发生异常: {str(e)}")
            return None
