"""
注册的测试脚本
"""

# 注册失败的测试脚本
import pytest
from zonghe.baw import Member, Db
from zonghe.caw import DataRead, Asserts


# pytest 数据驱动的方式
# 从yaml中读取测试数据


@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_fail.yaml"))
def fail_data(request):
    return request.param


def test_register_fail(url, baserequests, fail_data):
    # 下发注册的请求
    r = Member.register(url, baserequests, fail_data['data'])
    # 断言结果
    print(r.text)
    # assert r.json()['status'] == fail_data['expect']['status']
    # assert r.json()['code'] == fail_data['expect']['code']
    # assert r.json()['msg'] == fail_data['expect']['msg']
    Asserts.check(r.json(), fail_data['expect'], "status,code,msg")


# 把注册成功的数据写到register_pass.yaml
@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_pass.yaml"))
def pass_data(request):
    return request.param


# 注册成功的脚本下发请求，断言响应的结果
def test_register_pass(url, baserequests, pass_data, db):
    mobilephone = pass_data['data']['mobilephone']
    # 初始化环境：删除注册的用户（数据库中可能有其他人测试的数据，与本用例冲突）
    Db.delete_user(db, mobilephone)
    # 下发注册请求
    r = Member.register(url, baserequests, pass_data['data'])
    print(r.text)
    # assert r.json()['status'] == pass_data['expect']['status']
    # assert r.json()['code'] == pass_data['expect']['code']
    # assert r.json()['msg'] == pass_data['expect']['msg']
    Asserts.check(r.json(), pass_data['expect'], "status,code,msg")
    # 调用查询的接口，在查询结果中能找到本次中注册的手机号码
    r = Member.list(url, baserequests)
    assert mobilephone in r.text
    # 清理环境，删除注册的用户
    Db.delete_user(db, mobilephone)


# 重复注册
@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_redo.yaml"))
def redo_data(request):
    return request.param


def test_register_redo(url, baserequests, redo_data, db):
    mobilephone = redo_data['data']['mobilephone']
    # 下发注册
    r = Member.register(url, baserequests, redo_data['data'])
    # 重复注册
    r = Member.register(url, baserequests, redo_data['data'])
    print(r.text)
    # assert r.json()['status'] == redo_data['expect']['status']
    # assert r.json()['code'] == redo_data['expect']['code']
    # assert r.json()['msg'] == redo_data['expect']['msg']
    Asserts.check(r.json(), redo_data['expect'], "status,code,msg")
    # 清理环境，删除注册的用户
    Db.delete_user(db, mobilephone)


# 20109：手机号格式不正确
@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_phone.yaml"))
def phone_data(request):
    return request.param


def test_register_phone(url, baserequests, phone_data, db):
    mobilephone = phone_data['data']['mobilephone']
    # 下发注册
    r = Member.register(url, baserequests, phone_data['data'])
    print(r.text)
    # assert r.json()['status'] == phone_data['expect']['status']
    # assert r.json()['code'] == phone_data['expect']['code']
    # assert r.json()['msg'] == phone_data['expect']['msg']
    Asserts.check(r.json(), phone_data['expect'], "status,code,msg")
    # 清理环境，删除注册的用户
    Db.delete_user(db, mobilephone)
