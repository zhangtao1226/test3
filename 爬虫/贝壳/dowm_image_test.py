import urllib.request

url = 'https://ke-image.ljcdn.com/newhouse-user-image/9017d2104fabea6740c287da2adf1343.png.592x432.jpg'
request = urllib.request.Request(url)

try:
    response = urllib.request.urlopen(request)
    image_name = 'img.jpg'
    filename = './image/' + image_name
    if response.getcode == 200:
        with open(filename, 'wb') as f:
            f.write(response.read())
        print(filename)
except:
    print('error')