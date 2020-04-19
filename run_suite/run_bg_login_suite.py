
# 导包
import time
import unittest
from config import BASE_DIR
# 实例化测试套件对象
from tools.HTMLTestRunner import HTMLTestRunner
suite = unittest.defaultTestLoader.discover(BASE_DIR + "./case/",pattern="test_*.py")
# 调用方法组装测试用例
# suite.addTest(unittest.makeSuite(TestPCLogin))
# 调用实例化执行对象
# runner = unittest.TextTestRunner()
file_name = BASE_DIR + "./report/report{}_bg_login.html".format(time.strftime("%Y%m%d%H%M%S"))
print(file_name)
# 报告文件存放路径
with open(file_name,"wb")as f:
    runner = HTMLTestRunner(stream=f, title="自动化测试报告", description="Chrome浏览器")
    runner.run(suite)