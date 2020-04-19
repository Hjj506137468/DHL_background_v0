from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class ToDoPage(BasePage):
    """代办事项——对象库层"""

    def __init__(self):
        super().__init__()
        self.to_do_click = (By.XPATH, '/html/body/app-root/app-nav/div/div[2]/div[1]/div[1]/div')
        self.data_controls_click = (By.XPATH, '//*[@id="datetimeStart"]')

    def find_to_do(self):
        """代办事项"""
        return self.find_element_method(self.to_do_click)
    def find_data_controls(self):
        """日期控件"""
        return self.find_element_method(self.data_controls_click)


class ToDoHandle(BaseHandle):
    """待办事项——操作库层"""

    def __init__(self):
        self.to_do_page = ToDoPage()

    def click_to_do(self):
        self.element_click(self.to_do_page.find_to_do())
    def click_data_controls(self):
        self.element_click(self.to_do_page.find_data_controls())


class ToDoProxy(object):
    """首页——对象库层"""

    def __init__(self):
        self.to_do_handle = ToDoHandle()

    def click_to_do(self):
        self.to_do_handle.click_to_do()
    def click_data_controls(self):
        self.to_do_handle.click_data_controls()
