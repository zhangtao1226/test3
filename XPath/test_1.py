from lxml import etree

text = '''
<div> 
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">thride item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
</div>
'''
html = etree.HTML(text)
print('打印类型:', type(html))
result = etree.tostring(html) # 输出结果为 bytes 类型
print('打印结果:', result, '打印结果类型:', type(result))
new_result = result.decode('utf-8')
print('转换结果类型:', type(new_result))  # 将 bytes 类型转为 str类型
print('打印新结果:', new_result)
