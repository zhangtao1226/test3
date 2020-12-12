
# f = open('test_1.txt','w')
#
# f.write('hello')
#
# f.write('word')

# f.close()

f = open('test_1.txt', 'r')

txt = f.readline()
print(txt)
f.close()