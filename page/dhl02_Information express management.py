from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class ExpressManagementPage(BasePage):
    """信息速递-对象库层"""
    def __init__(self):
        super().__init__()
        self.express_management_click = (By.XPATH,"")
    def find_express_management(self):
        return self.find_element_method(self.express_management_click)
class ExpressManagementHandle(BaseHandle):
    def __init__(self):
        self.express_management = ExpressManagementPage()
    def click_express_management(self):
        self.element_click(self.express_management.find_express_management())

