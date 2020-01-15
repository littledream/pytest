from selenium import webdriver
import pytest

@ pytest.fixture()
def open_browser(request):
    driver = webdriver.Chrome()  # 打开浏览器

    def end():
        driver.quit()  # 关闭浏览器

    request.addfinalizer(end)  # 终结函数
    return driver

def test_baidu(open_browser):
    open_browser.get("http://www.baidu.com")

def test_sina(open_browser):
    open_browser.get("http://www.sina.com")