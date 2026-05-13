import os
from app.core.logger import logger
import pytest
from app.utils.file_util import AeroFileProcessor

def test_batch_file_reading():
    """测试批量读取功能是否正常"""
    # 1. 准备测试环境：在 data/raw_docs 下临时建两个测试文件
    test_dir = "data/raw_docs"
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    
    file1_path = os.path.join(test_dir, "test1.txt")
    file2_path = os.path.join(test_dir, "test2.txt")
    
    with open(file1_path, "w", encoding="utf-8") as f:
        f.write("气动数据 A")
    with open(file2_path, "w", encoding="utf-8") as f:
        f.write("气动数据 B")

    # 2. 运行我们的工具类
    processor = AeroFileProcessor(base_path=test_dir)
    files = processor.collect_files(extension=".txt")
    results = processor.read_all_contents(files)

    # 3. 断言验证：检查是否读到了 2 个文件，且内容正确
    assert len(files) >= 2
    assert "气动数据 A" in results["test1.txt"]
    assert "气动数据 B" in results["test2.txt"]
    
    logger.info("🎯 批量文件读取测试全部通过！")