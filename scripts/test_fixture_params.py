import pytest

@pytest.fixture(params=[1,2,3])
def new_data(request):
    return request.param
def test_data(new_data):
    print("测试步骤")
    assert new_data == 3
    
# @pytest.fixture(params=[["Tom","123"],["Jerry","321"],["mary","456"]])
# def login(request):
#     print("用户名%s密码%s"%(request.param[0],request.param[1]))
#
# def test_add_cart(login):
#     print("添加购物车")