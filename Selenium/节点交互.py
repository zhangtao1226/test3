from selenium import webdriver
import time

brower = webdriver.Chrome()
brower.get('https://www.taobao.com')
input = brower.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
button = brower.find_element_by_class_name('btn-search')
button.click()

brower.close() # 关闭浏览器