"""
pytest脚本
1. 文件以test_开头
2. 测试类以test开头
3. 测试函数或者方法以test_开头
"""
import requests

url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"

#
def test_regsiter_001():
    cs = {"mobilephone": "13082136818", "pwd": "aa12345689"}
    r = requests.post(url, data=cs)
    print(r.text)
    assert r.json()['code'] == "10001"
    assert r.json()['msg'] == "注册成功"

def test_regsiter_002():
    cs = {"mobilephone": "18036008188", "pwd": "1234567890123456789"}
    r = requests.post(url, data=cs)
    print(r.text)
    assert r.json()['msg'] == "密码长度必须为6~18"

def test_regsiter_003():
    cs = {"mobilephone": "15106008111", "pwd": ""}
    r = requests.post(url, data=cs)
    assert r.json()['msg'] == "密码不能为空"
