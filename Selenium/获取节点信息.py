# 获取属性

from selenium import webdriver

brower = webdriver.Chrome()
url = 'https://nj.fang.ke.com/loupan'
brower.get(url)
print(brower.page_source)
logo = brower.find_element_by_class_name('resblock-list-wrapper')
print(logo)
