import requests
from app.core.logger import logger

class AeroHttpSender:
    def __init__(self, timeout=15):
        self.timeout = timeout

    def safe_get(self, url, params=None):
        logger.info(f"🚀 正在请求 GET: {url}")
        try:
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            logger.info(f"✅ GET 响应成功 | 状态码: {response.status_code}")
            if "application/json" in response.headers.get("Content-Type", ""):
                return response.json()
            else:
                logger.warning("⚠️ 响应内容不是 JSON 格式")
                return response.text
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP 错误: {http_err}")
            return f"HTTP 错误发生: {http_err}"
        except requests.exceptions.ConnectionError:
            logger.error("网络连接错误")
            return "网络连接错误: 请检查你的路由器或代理设置！"
        except requests.exceptions.Timeout:
            logger.error("请求超时")
            return "请求超时: 服务器响应太慢了，请稍后再试。"
        except Exception as e:
            logger.error(f"未知错误: {e}")
            return f"发生了未知错误: {e}"

    def safe_post(self, url, data=None):
        logger.info(f"🚀 正在请求 POST: {url}")
        try:
            response = requests.post(url, json=data, timeout=self.timeout)
            logger.info(f"✅ POST 响应成功 | 状态码: {response.status_code}")
            if "application/json" in response.headers.get("Content-Type", ""):
                return response.json()
            else:
                logger.warning("⚠️ 响应内容不是 JSON 格式")
                return response.text
        except Exception as e:
            logger.error(f"❌ POST 请求发生异常: {str(e)}")
            return None