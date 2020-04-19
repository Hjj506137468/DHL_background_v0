# 登录测试用例
import unittest
import time

from assert_collect import BgAssertHandle
from config import BASE_DIR
from data.read_login_data import handler_excel
from page.login_page import LoginProxy
from utils import DriverUtils
from parameterized import parameterized
print(BASE_DIR)

class TestBGlogin(unittest.TestCase):
    """后台 测试类"""
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtils.get_driver()
        cls.login_proxy = LoginProxy()
        cls.bg_assert_handle = BgAssertHandle()
    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtils.quit_driver()
    def setUp(self) -> None:
        self.driver.get('https://witest.cndhl.com/v2server/login')
    @parameterized.expand(handler_excel())
    def test_login(self,name,pwd,mess):
        self.login_proxy.login_method(name,pwd)
        time.sleep(1)
        message = self.bg_assert_handle.login_succeed_test()
        print(message)
        try:
            self.assertIn(str(mess), message)
        except Exception as e:
            now_time = time.strftime('%Y%m%d_%H%M%S')
            # 截图
            print(BASE_DIR)
            self.driver.get_screenshot_as_file(BASE_DIR + '/screenshot/bug_{}_{}bg_login.png'.format(now_time, e))
            raise e

if __name__ == '__main__':
    unittest.main()
