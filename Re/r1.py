import re

# search() 方法会依次扫描字符串，直到找到第一个符合规则的字符串，然后返回匹配内容，如果没有则返回 None。

html = '''<div id = "song-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">经典老歌列表</p>
    <ul id="list" class="list-group">
    <li data-view="2">一路上有你</li>
    <li data-view="7">
        <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
    </li>
    <li data-view="4" class="active">
        <a href="/3.mps" singer="齐秦">往事随风</a>
    </li>
    <li data-view="6"><a href="/6.mp3" singer="beyond">光辉岁月</a></li>
    <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
    <li data-view="1"><a href="/1.mp3" singer="beyond">但愿人长久</a></li>
'''
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)

# result = re.findall('<li.*?>.*?(<a.*?</a>).*?</li>', html, re.S)
result = re.findall('<a.*?href="(.*?)" singer="(.*?)">(.*?)</a>', html, re.S)
base_url = 'http://www.zhangao.com'
for a in result:
    print('连接：',base_url+a[0], '名称：',a[1], '歌名：',a[2])