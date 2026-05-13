import requests  # 引入请求库，这是我们的“传声筒”
import time      # 引入时间库，用于处理超时重试

class AeroHttpSender:
    """
    【气动智能体 HTTP 发送器】
    作用：安全、规范地向外部 API（如大模型接口）发送数据请求
    """
    
    def __init__(self, timeout=10):
        # timeout: 设置超时时间为10秒。
        # 如果10秒内对方没反应，就断开，防止程序死等浪费资源。
        self.timeout = timeout

    def safe_get(self, url, params=None):
        """
        发送 GET 请求（类似于向服务器“查询”信息）
        """
        try:
            # 使用 requests 发送请求
            # params 参数用于在 URL 后面拼接查询条件，例如 ?id=1
            response = requests.get(url, params=params, timeout=self.timeout)
            
            # 检查状态码。如果返回 404 或 500 等错误，直接抛出异常进入 except 分支
            response.raise_for_status()
            
            # 将返回的 JSON 格式数据转换成 Python 字典
            return response.json()
            
        except requests.exceptions.HTTPError as http_err:
            return f"HTTP 错误发生: {http_err}"  # 比如 404 找不到网页
        except requests.exceptions.ConnectionError:
            return "网络连接错误: 请检查你的路由器或代理设置！"
        except requests.exceptions.Timeout:
            return "请求超时: 服务器响应太慢了，请稍后再试。"
        except Exception as e:
            return f"发生了未知错误: {e}"

    def safe_post(self, url, data=None):
        """
        发送 POST 请求（类似于向服务器“提交”数据或下达指令）
        """
        try:
            # 发送 POST 请求，json=data 会自动把字典转成标准的 JSON 字符串发送
            response = requests.post(url, json=data, timeout=self.timeout)
            
            # 同样进行错误检查
            response.raise_for_status()
            
            return response.json()
        except Exception as e:
            return f"POST 请求失败: {e}"