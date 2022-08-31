#导包
import unittest
from tools.HTMLTestRunner_PY3 import HTMLTestRunner
from scripts.i1_login import ihrm_login
from scripts.i2_add_employee import ihrm_add_employee

#封装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(ihrm_login))
suite.addTest(unittest.makeSuite(ihrm_add_employee))

#指定报告存放位置
report = "./report/report.html"

#打开文件流
with open(report, "wb") as e:
    #创建运行器
    runner = HTMLTestRunner(e, title="ihrm测试报告")
    #运行
    runner.run(suite)
