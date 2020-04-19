from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    """登录——对象库层"""

    def __init__(self):
        super().__init__()
        self.username = (By.CSS_SELECTOR,'input[placeholder="请输入用户名"]')#用户名
        self.password = (By.CSS_SELECTOR,'input[placeholder="请输入密码"]')#密码
        self.login = (By.XPATH,'//*[text()="登 录"]') #登录
    def find_username(self):
        return self.find_element_method(self.username)
    def find_password(self):
        return self.find_element_method(self.password)
    def find_login(self):
        return self.find_element_method(self.login)
class LoginHandle(BaseHandle):
    """登录——操作层"""
    def __init__(self):
        self.login_page = LoginPage()
    def input_username(self,name):
        self.input_text(self.login_page.find_username(),name)
    def input_password(self,pwd):
        self.input_text(self.login_page.find_password(),pwd)
    def cilck_login(self):
        self.element_click(self.login_page.find_login())
class LoginProxy(object):
    """登录——业务层"""
    def __init__(self):
        self.login_handle = LoginHandle()
    def login_method(self,name,pwd):
        self.login_handle.input_username(name)
        self.login_handle.input_password(pwd)
        self.login_handle.cilck_login()