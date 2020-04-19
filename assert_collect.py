from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle
class BgAssert(BasePage):
    """断言——元素获取层"""
    def __init__(self):
        super().__init__()
        self.login_succeed = (By.XPATH,'/html/body/app-root/div/span')#登录成功断言
    def find_login_succeed(self):
        """登录成功断言"""
        return self.find_element_method(self.login_succeed)
class BgAssertHandle(BaseHandle):
    """断言——获取文本"""
    def __init__(self):
        self.bg_assert = BgAssert()
    def login_succeed_test(self):
        """登录成功文本"""
        return self.bg_assert.find_login_succeed().text

