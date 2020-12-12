import pandas

df = pandas.read_csv('music.csv')


text = df.loc[1:3, 'Artist']

print(text)