
# a = set()
# b = set()
#
# a.add(frozenset(b))
#
# print(a)


c = {1,2,3,4}
print(id(c))
c = frozenset(c)
print(id(c))
print(type(c))

for i in c:
    print(1)
    print(type(i))