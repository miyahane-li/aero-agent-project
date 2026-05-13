from app.utils.file_util import AeroDataProcessor
import os

def test_json_save():
    """测试 JSON 保存功能是否正常"""
    # 1. 准备假数据
    mock_data = {"project": "AeroAgent", "version": "v0.1"}
    test_file = "test_output.json"
    
    # 2. 运行我们的工具
    processor = AeroDataProcessor("none.txt")
    processor.save_as_json(mock_data, test_file)
    
    # 3. 验证文件是否生成
    assert os.path.exists(test_file) == True
    
    # 4. 清理垃圾文件
    os.remove(test_file)