import pytest

@pytest.mark.xfail(condition=True,reason="")
def test_1():
    print("当条件为真时,用例执行失败")
    assert False

@pytest.mark.xfail(condition=True,reason="")
def test_2():
    print("当条件为真时,用例执行成功")
    assert True

@pytest.mark.xfail(conditon=False,reason="")
def test_3():
    print("当条件为假时,用例执行成功")
    assert True 

@pytest.mark.xfail(conditon=False,reason="")
def test_4():
    print("当条件为假时,用例执行失败")
    assert False
