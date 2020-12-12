import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

brower = webdriver.Chrome()
url = 'https://www.runoob.com/try/try.php?filename=tryjs_this_method'
brower.get(url)

print(brower.get_cookies())

exit()


brower.switch_to.frame('iframeResult') # 切换到子 Frame
try:
    logo = brower.find_element_by_tag_name('h2')
except NoSuchElementException:
    print('NO TAG')

brower.switch_to.parent_frame() # 切换到父Frame
logo = brower.find_element_by_tag_name('textarea')
print(logo)
print(logo.text)
