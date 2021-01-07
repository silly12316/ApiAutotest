"""
mark标记
1. skip 跳过用例不执行
2. 自定义标记：接口自动化，功能自动化，界面自动化，冒烟测试
    通过自定义标记，标记用例属于哪一类。
    比如版本转测试，需要进行冒烟测试，只执行带有冒烟测试的用例

    pytest.ini 配置文件
    -m=smoke 执行带smoke的用例
    -m=func
    -m="smoke and func" 执行带smoke标记和func标记的用例
    -m="smoke or func" 执行带smoke标记或func标记的用例
    -m="not func" 执行不带func标记的用例
"""
import pytest

version = 'V1R2'

@pytest.mark.smoke
def test_case01():
    print("用例1")


@pytest.mark.skip("跳过原因：缺陷，改动比较大，作为一行版本的需求来实现")
def test_case02():
    print("用例2")


@pytest.mark.skipif(version == 'V1R1', reason='V1R1版本不支持，如果是V1R1版本跳过')
def test_case03():
    print("用例3")


@pytest.mark.func
def test_case04():
    print("用例4")


def test_case05():
    print("用例5")


# 对类厦门的所有用例生效
@pytest.mark.func
class TestClass:
    @pytest.mark.smoke  # 自定义标记：冒烟测试
    def test_case06(self):
        print("用例6")

    @pytest.mark.smoke
    def test_case07(self):
        print("用例7")

    def test_case08(self):
        print("用例8")

    def test_case09(self):
        print("用例9")

    def test_case010(self):
        print("用例10")
