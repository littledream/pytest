import pytest
import random
num = random.randint(1,10)

@pytest.mark.skipif(condition=num%2==0,reason="女性跳过")
def test_browser_electronic():
    print("电子产品")

@pytest.mark.skipif(condition=num%2==1,reason="男性跳过")
def test_browser_maquillage():
    print("浏览化妆品")
