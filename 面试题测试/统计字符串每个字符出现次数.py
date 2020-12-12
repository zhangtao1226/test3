from collections import Counter

a = 'kdisjdsdfnfnasfkaddienekdkddiwddffmsa;ddkiw:'

res = Counter(a)
print(res, type(res))

for i in res.items():
    print(i, type(i))
'''
Counter({'d': 12, 
        'k': 5, 
        'f': 5, 
        'i': 4, 
        's': 4, 
        'n': 3, 
        'a': 3, 
        'e': 2, 
        'w': 2, 
        'j': 1, 
        'm': 1, 
        ';': 1, 
        ':': 1}
        ) 
<class 'collections.Counter'>
'''