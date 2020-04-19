"""po模式的基类"""
from utils import DriverUtils

class BasePage(object):
    """对象库层"""
    def __init__(self):
        self.driver = DriverUtils.get_driver()
        """调用打开浏览器"""
    def find_element_method(self,location):
        return self.driver.find_element(location[0],location[1])
class BaseHandle(object):
    """操作层-基类"""

    def input_text(self, element, text):
        """
        输入内容方法
        :param element: 元素对象
        :param text: 文本内容
        :return: 无
        """
        element.clear()
        element.send_keys(text)

    def element_click(self, element):
        element.click()
