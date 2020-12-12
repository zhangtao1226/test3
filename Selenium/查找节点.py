from selenium import webdriver

brower = webdriver.Chrome()

brower.get('https://www.taobao.com')  # 获取淘宝页面

def get_single_element():
    """
    单个节点
    :return:
    """
    input_first = brower.find_element_by_name('q')
    input_second = brower.find_element_by_id('q')
    input_third = brower.find_element_by_xpath('//*[@id="q"]')
    print(input_first, input_second, input_third)
    brower.close()
get_single_element()