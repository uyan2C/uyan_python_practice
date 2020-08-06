#测试计算器代码


#外部数据源文件
from python_code.calc import Calculator
import pytest
import yaml

with open('./datas/calc.yml') as f:
  datas = yaml.safe_load(f)
  datas_add = datas['add']
  datas_div = datas['div']

# 测试类
class TestCalc:
  #setup方法，用例执行的前提条件
  def setup_class(self):
    print("开始计算")
    #实例化计算器
    #加了self.则局部变量变成实例变量，类中的其他方法也可用
    self.calc = Calculator()

  # teardown方法，cleanup action
  def teardown_class(self):
    print("结束计算")

  @pytest.mark.add
  @pytest.mark.parametrize("a, b, expect", datas_add['datas'], ids=datas_add['myid'])
  def test_add(self, a, b, expect):
    result = self.calc.add(a, b)
    # isinstance()函数用来判断一个对象是否是一个已知的类型
    if isinstance(result, float):
      result = round(result, 2)
    assert expect == result

  @pytest.mark.div
  @pytest.mark.parametrize("a, b, expect", datas_div['datas'], ids=datas_div['myid'])
  def test_div(self, a, b, expect):
    result = self.calc.div(a, b)
    # isinstance()函数用来判断一个对象是否是一个已知的类型
    if isinstance(result, float):
      result = round(result, 2)
    assert expect == result