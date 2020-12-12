import re, requests

base_url = 'http://kaijiang.500.com/shtml/ssq/20069.shtml'

html = requests.get(base_url).text

result = re.findall('<a href="(http://.*?.shtml)">(.*?)</a>', html)

url_list = []

# print()
try:
    for li in result:
        url_list.append(li[0])
finally:
    print('error')


print(url_list)