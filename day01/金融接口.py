import requests

# 注册
"""
# 验证用户使用合法的手机号、密码，昵称为空，注册成功
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "15106008111", "pwd": "123456"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "注册成功"
# 验证用户使用合法的手机号、密码、昵称，注册成功
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "18006118018", "pwd": "123456789012345678", "regname": "haha"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "注册成功"
# 验证用户使用合法的手机号、密码，昵称含中文，注册成功
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "13006118018", "pwd": "aa12345689", "regname": "发发发发发发发发发发发发发发发发发发发发发发发发发发发"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "注册成功"

# 验证用户使用合法的手机号、密码，昵称含数字，注册成功
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "13066118018", "pwd": "aa1234569", "regname": "发1a发发"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "注册成功"
# 验证用户使用合法的手机号、密码，昵称含特殊字符，注册成功
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "13666118018", "pwd": "aa123569", "regname": "c%@1a发发"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "注册成功"
"""

# 验证用户使用合法的手机号码，昵称、密码为空，注册失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "13006007016", "pwd": "", "regname": " "}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "密码不能为空"
# 验证用户手机号码、昵称为空，密码合法，注册失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "", "pwd": "12345678", "regname": " "}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "手机号不能为空"
# 验证用户手机号码、密码、昵称为空，注册失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "", "pwd": "", "regname": ""}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "手机号不能为空"
# 验证用户使用合法的手机号码、昵称，密码为空，注册失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "13016567022", "pwd": "", "regname": "呵护"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['code'] == "20103"
# 验证用户手机号码为空，密码、昵称合法，注册失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "", "pwd": "abc89585", "regname": "呵护"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "手机号不能为空"

# 验证用户使用合法的手机号码，密码输入5位，注册失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "18006008188", "pwd": "abc95"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['code'] == '20108'
# 验证用户使用合法的手机号码，密码输入3位，注册失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "18036008188", "pwd": "abc"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['code'] == "20108"
# 验证用户使用合法的手机号码，密码输入19位，注册失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "18036008188", "pwd": "1234567890123456789"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "密码长度必须为6~18"
# 验证用户使用长度为1的手机号码，注册失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "1", "pwd": "1651d36"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "手机号码格式不正确"
# 验证用户使用长度为6的手机号码，注册失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "180600", "pwd": "1651d36"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "手机号码格式不正确"
# 验证用户使用长度为10的手机号码，注册失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "1800600701", "pwd": "1651d36"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "手机号码格式不正确"
# 验证用户使用长度为12的手机号码，注册失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "180060070189", "pwd": "1651d36"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "手机号码格式不正确"
# 验证用户使用长度为11的不合法手机号码，注册失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "11111111111", "pwd": "1651d36"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "手机号码格式不正确"

# # 验证用户使用已注册的手机号码，注册失败
# url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
# cs = {"mobilephone": "13066118018", "pwd": "12345678", "regname": "haha"}
# print(r.text)
# assert r.json()['code'] == "20110"

# 登录
# 验证用户输入合法的手机号码、密码，登录成功
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone": "15106008111", "pwd": "123456"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "登录成功"
# 验证用户输入合法的手机号码，密码为空，登录失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone": "15106008111", "pwd": ""}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "密码不能为空"
# 验证用户输入合法的密码，手机号码为空，登录失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone": "", "pwd": "1234567"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "手机号不能为空"
# 验证手机号、密码为空，登录失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone": "", "pwd": ""}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "手机号不能为空"
# 验证输入未注册的手机号，登录失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone": "18006009001", "pwd": "1345665"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "用户名或密码错误"
# 验证输入长度不合法的手机号，登录失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone": "180060001", "pwd": "1345665"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "用户名或密码错误"
# 验证输入合法的手机号码，密码不合法，登录失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone": "18006009001", "pwd": "13665"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "用户名或密码错误"
# 验证输入已注册的手机号码，密码错误，登录失败
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
cs = {"mobilephone": "18006118018", "pwd": "15601111"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "用户名或密码错误"

# 验证用户使用合法的手机号、密码，昵称含中文，注册成功
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone": "13005216018", "pwd": "aa12345689", "regname": "发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发发"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == "注册成功"
