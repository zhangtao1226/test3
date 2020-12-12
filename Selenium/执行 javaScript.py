'''
execute_script() 方法：直接模拟运行 JavaScript ，比如 下拉框
'''

from selenium import webdriver

brower = webdriver.Chrome()
brower.get('htpps://www.zhihu.com/explore')
brower.execute_script('window.scrollTo(0, document.body.scrollHeight)')
brower.execute_script('alert("to Bottom")')