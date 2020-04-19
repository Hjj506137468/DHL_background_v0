import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://witest.cndhl.com/v2/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_xpath('/html/body/app-root/div[1]/div/div/div/a[1]').click()
driver.find_element_by_xpath('/html/body/modal-container/div/div/app-registered-login/div/ul/li[2]/span').click()
driver.find_element_by_xpath('/html/body/modal-container/div/div/app-registered-login/div/div[3]/form/div[1]/input').send_keys('18303007557')
driver.find_element_by_xpath('/html/body/modal-container/div/div/app-registered-login/div/div[3]/form/div[2]/input').send_keys('asd123')
driver.find_element_by_xpath('/html/body/modal-container/div/div/app-registered-login/div/div[3]/form/div[3]/input').send_keys('pentestyz')
driver.find_element_by_xpath('/html/body/modal-container/div/div/app-registered-login/div/div[3]/form/button').click()#点击登录
time.sleep(2)
driver.find_element_by_xpath('/html/body/app-root/div[1]/div/div/ul/li[3]/a').click()
driver.find_element_by_xpath('/html/body/app-root/div[1]/div/div/ul/li[3]/div/ul[1]/li[2]/span').click()
driver.find_element_by_xpath('/html/body/app-root/div[2]/app-express-search/div/div/div[2]/div[1]/div[1]/ul/li/input').click()
driver.find_element_by_xpath('/html/body/app-root/div[2]/app-express-search/div/div/div[2]/div[1]/div[1]/ul/li/input').send_keys('1023712583')
driver.find_element_by_xpath('/html/body/app-root/div[2]/app-express-search/div/div/div[2]/div[1]/div[1]/ul/li/input').click()#回车
driver.find_element_by_xpath('/html/body/app-root/div[2]/app-express-search/div/div/div[2]/div[1]/div[2]/button').click()

# 物流运转-查询快件状态
driver.find_element_by_xpath('/html/body/app-root/div[2]/app-express-search/div/div/div[3]/div[3]/div[2]/div[5]/div[1]/span').click()
driver.find_element_by_xpath('/html/body/app-root/div[2]/app-query-express-status/div/div/form/div[2]/div/textarea').click()
driver.find_element_by_xpath('/html/body/app-root/div[2]/app-query-express-status/div/div/form/div[2]/div/textarea').send_keys('aszxdhwerg')
driver.find_element_by_xpath('/html/body/app-root/div[2]/app-query-express-status/div/div/app-bh-common-contract-infomation/div/div/form/div[1]/div[2]/input').send_keys('小h1')
driver.find_element_by_xpath('/html/body/app-root/div[2]/app-query-express-status/div/div/app-bh-common-contract-infomation/div/div/form/div[1]/div[4]/input').send_keys('18210853727')
driver.find_element_by_xpath('/html/body/app-root/div[2]/app-query-express-status/div/div/div[4]/button[3]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/modal-container/div/div/div/div[2]/button[2]').click()
driver.find_element_by_xpath('/html/body/modal-container/div/div/div/div[3]/button').click()

# #物流运转-重新派送
# driver.find_element_by_xpath('/html/body/app-root/div[2]/app-express-search/div/div/div[3]/div[3]/div[2]/div[5]/div[3]/span').click()
# driver.find_element_by_xpath('//*[@id="lastDate"]').click()
# driver.find_element_by_xpath('/html/body/div[5]/div[3]/table/tbody/tr[2]/td[6]').click()
# driver.find_element_by_xpath('/html/body/div[5]/div[3]/table/tbody/tr[2]/td[6]').click()
# driver.find_element_by_xpath('/html/body/app-root/div[2]/app-again-give/div/div/div[2]/div/textarea').send_keys('afg')
# driver.find_element_by_xpath('/html/body/app-root/div[2]/app-again-give/div/div/app-bh-common-contract-infomation/div/div/form/div[1]/div[2]/input').send_keys('小h1')
# driver.find_element_by_xpath('/html/body/app-root/div[2]/app-again-give/div/div/app-bh-common-contract-infomation/div/div/form/div[1]/div[4]/input').send_keys('18210853727')
# driver.find_element_by_xpath('/html/body/app-root/div[2]/app-again-give/div/div/div[4]/button[3]').click()
# time.sleep(2)
# driver.find_element_by_xpath('/html/body/modal-container/div/div/div/div[2]/button[2]').click()
# driver.find_element_by_xpath('/html/body/modal-container/div/div/div/div[3]/button').click()
# #物流运转-截停
# driver.find_element_by_xpath('/html/body/app-root/div[2]/app-express-search/div/div/div[3]/div[3]/div[2]/div[5]/div[5]/span').click()
# driver.find_element_by_xpath('').send_keys('小h1')
# driver.find_element_by_xpath('').send_keys('18210853727')
# driver.find_element_by_xpath('').click()
# #物流运转-退回
# driver.find_element_by_xpath('/html/body/app-root/div[2]/app-express-search/div/div/div[3]/div[3]/div[2]/div[5]/div[5]/span').click()
# driver.find_element_by_xpath('').send_keys('小h1')
# driver.find_element_by_xpath('').send_keys('18210853727')
# driver.find_element_by_xpath('').click()
# #物流运转-补充收件人信息
# driver.find_element_by_xpath('/html/body/app-root/div[2]/app-express-search/div/div/div[3]/div[3]/div[2]/div[5]/div[5]/span').click()
# driver.find_element_by_xpath('').send_keys('小h1')
# driver.find_element_by_xpath('').send_keys('18210853727')
# driver.find_element_by_xpath('').click()
# #物流运转-更改运费支付方式
# driver.find_element_by_xpath('/html/body/app-root/div[2]/app-express-search/div/div/div[3]/div[3]/div[2]/div[5]/div[5]/span').click()

time.sleep(2)
driver.quit()