from app.utils.http_util import AeroHttpSender

def test_get_request_success():
    """测试 GET 请求是否能成功拿到数据"""
    sender = AeroHttpSender()
    # 使用一个公开的测试 API：JSONPlaceholder
    test_url = "https://jsonplaceholder.typicode.com/posts/1"
    
    result = sender.safe_get(test_url)
    
    # 验证返回的结果里是否包含 'userId' 这个键
    # 如果包含，说明网络请求和解析都成功了
    assert "userId" in result
    assert result["id"] == 1

def test_invalid_url():
    """测试当 URL 错误时，程序是否能优雅地捕获异常而不崩溃"""
    sender = AeroHttpSender()
    bad_url = "https://this-is-a-wrong-url-12345.com" 
    
    result = sender.safe_get(bad_url)
    
    # 验证返回的结果是否包含我们定义的错误提示
    assert "网络连接错误" in result