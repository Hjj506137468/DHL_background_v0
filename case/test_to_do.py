#代办事项测试用例
import unittest
import time
from parameterized import parameterized

from config import BASE_DIR, CD_DIR
from data.read_to_do_data import handler_excel
from page.dhl01_to_do_page import ToDoProxy
from page.login_page import LoginProxy
from utils import DriverUtils


class ToDo(unittest.TestCase):
    """代办事项测试类"""
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtils.get_driver()
        cls.login_proxy = LoginProxy()
        cls.to_do_proxy = ToDoProxy()

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtils.quit_driver()
    @parameterized.expand(handler_excel())
    def test_to_do(self,name,pwd,mess):
        self.login_proxy.login_method(name,pwd)
        time.sleep(1)
        self.to_do_proxy.click_to_do()
        self.to_do_proxy.click_data_controls()
        message = self.driver.find_element_by_xpath('/html/body/app-root/app-nav/div/div[2]/div[2]/app-backlog/div[3]/table/tbody/tr[2]/td[1]').text
        print(message)
        try:
            self.assertIn(str(mess), message)
        except Exception as e:
            now_time = time.strftime('%Y%m%d_%H%M%S')
            # 截图
            print(CD_DIR)
            self.driver.get_screenshot_as_file(CD_DIR + '/screenshot/bug_{}_{}bg_to_do.png'.format(now_time, e))
            raise e



if __name__ == '__main__':
    unittest.main()



