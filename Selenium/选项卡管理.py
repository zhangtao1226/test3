import time
from selenium import webdriver

brower = webdriver.Chrome()
brower.get('https://www.baidu.com')
brower.execute_script('window.open()')
print(brower.window_handles)
brower.switch_to_window(brower.window_handles[1])
brower.get('https://www.taobao.com')
time.sleep(1)
brower.switch_to_window(brower.window_handles[0])
brower.get('https://python.org')
