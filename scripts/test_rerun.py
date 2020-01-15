import random

class TestCart:
    def test_add_cart(self):
        print("测试添加购物车")
        assert True

    def test_cart_list(self):
        print("测试查看购物车清单")
        num = random.randint(0,1)
        if num == 0:
            assert True
        else:
            assert False

    def test_update_cart(self):
        print("测试更新购物车")
        assert True

    def test_delete_cart(self):
        print("测试删除购物车")
        assert True
