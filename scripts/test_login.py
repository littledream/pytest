import pytest

@pytest.mark.run(order=3)
def test_add_cart():
    print("测试添加购物车")
    
@pytest.mark.run(order=2)
def test_order():
    print("测试下单")
    
@pytest.mark.run(order=1)
def test_close():
    print("关闭浏览器")