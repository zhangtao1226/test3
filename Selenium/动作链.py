'''
对于输入框、输入文字、清空文字、按钮的点击、或者鼠标拖拽、键盘按键等。
'''

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

brower = webdriver.Chrome()
url = 'https://www.runoob.com/try/try.php?filename=tryhtml5_draganddrop'
brower.get(url)
# brower.swithc_to.frame('iframeResult')

print(brower.find_elements(By.id, 'div1'))

exit()
source = brower.find_element_by_id('drag1')
target = brower.find_element_by_id('div1')
actions = ActionChains(brower)
actions.drag_and_drop(source, target)
actions.perform()

