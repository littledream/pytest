import pytest
from common.operation_data import OperationFlie

# 传一个参数
# @pytest.mark.parametrize("phone_num",["13245666788","13256778900"])
# def test_verifycode(phone_num):
#     print("输入的手机号为:",phone_num)

# 传多个参数
data = OperationFlie("test_data.csv").get_data_to_list()
print(data)

@pytest.mark.parametrize("phone,code",data)
def test_login(phone,code):
    print("手机号%s,验证码%s"%(phone,code))