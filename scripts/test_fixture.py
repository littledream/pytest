import pytest

@pytest.fixture()
def login():
    print("登录成功!")
    
def test_get_addr(login):
    print("进入个人中心,查看收货地址")
    
def test_get_order(login):
    print("进入个人中心,查看订单")
    
def test_browser_goods():
    print("不需要登录,浏览商品")