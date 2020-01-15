import pytest

@pytest.fixture()
def operation_database():
    print("连接数据库,准备测试数据")
    yield
    print("断开连接,清空测试数据")
    
def test_register(operation_database):
    print("执行测试注册用例")