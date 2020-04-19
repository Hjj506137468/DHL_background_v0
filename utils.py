from selenium import webdriver
class DriverUtils(object):
    """浏览器公共工具"""
    driver = None
    # 初始化浏览器对象
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.get("https://witest.cndhl.com/v2server/login")
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        """退出浏览器"""
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None

if __name__ == '__main__':
    DriverUtils.get_driver()
    DriverUtils.quit_driver()