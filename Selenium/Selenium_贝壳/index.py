import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

driver = webdriver.Chrome()
BASE_URL = 'https://nj.fang.ke.com/loupan'

try:
    driver.get(BASE_URL)
except TimeoutException:
    print('Time Out')

try:
    all_loupan_lists = driver.find_elements_by_class_name('resblock-list')
except NoSuchElementException:
    print('No Element')

new_house_lists = []
for loupan_list in all_loupan_lists:
    loupan = {}
    loupan['house_img'] = loupan_list.find_element_by_css_selector('a img').get_attribute('src')
    loupan['house_title'] = loupan_list.find_element_by_css_selector('a').get_attribute('title')
    loupan['house_detail_url'] = loupan_list.find_element_by_css_selector('a').get_attribute('href')
    loupan['house_status'] = loupan_list.find_element_by_css_selector('.resblock-name span').text
    loupan['house_location'] = loupan_list.find_element_by_css_selector('.resblock-location').text
    house_rooms = loupan_list.find_elements_by_css_selector('.resblock-room span')
    for house_room in house_rooms:
        loupan['house_room'] = []
        loupan['house_room'].append(house_room.text)
    print(loupan)
    new_house_lists.append(loupan)

print(new_house_lists)
driver.close()
