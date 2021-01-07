import pytest
import requests


# 注册功能测试数据
# 写法一
@pytest.fixture(params=[{"mobilephone": 15106008122, "pwd": 123456, "code": "10001"},
                        {"mobilephone": 18006118068, "pwd": "123456789012345678", "regname": "haha", 'code': "10001"},
                        {"mobilephone": 13006118888, "pwd": "aa12345689", "regname": "发发发发发发发发发发发发发发发发发发发发发发发发发发发",
                         'code': "10001","msg":"手机号码已注册"},
                        {"mobilephone": 18006118888, "pwd": "aa1234569", "regname": "发1a发发", 'code': "10001"},
                        {"mobilephone": 15666118018, "pwd": "aa123569", "regname": "c%@1a发发", 'code': "10001"}])
def add1_data(request):
    return request.param

def test_add(add_data):
    url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
    print(f"注册数据为：{add_data}")
    r = requests.post(url, data=add_data)
    assert r.json()['code'] == add_data['code']

# 写法二
# 注册功能测试数据
@pytest.fixture(params=[{"data": {"mobilephone": 15106008122, "pwd": 123456},
                         "expect": {'code': "10001","msg":"手机号码已注册","data":None}},
                         {"data": {"mobilephone": 18006118068, "pwd": "123456789012345678"},
                          "expect": {'code': "10001","msg":"手机号码已注册","data":None}}])
def add1_data(request):
    return request.param

def test_add1(add1_data):
    url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
    print(f"注册数据为：{add1_data['data']}")
    r = requests.post(url, data=add1_data['data'])
    print(r.text)
    assert r.json()['code'] == add1_data['code']
    assert r.json()['msg'] == add1_data['msg']
