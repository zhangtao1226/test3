import requests

data = {
    'name': 'germey',
    'age': 25
}

r = requests.get('https://movie.youku.com/?spm=a2hcb.12675304.m_6913.5~5~5~5~5!2~5~5~A')

# print(r.)

with open('html_2.html', 'wb') as f:
    f.write(r.content)


