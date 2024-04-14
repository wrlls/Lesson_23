import requests
from bs4 import BeautifulSoup
url = 'https://dedmorozural.ru/'
responce = requests.get(url)
print(responce.status_code)
"""print(responce.text)"""

soup = BeautifulSoup(responce.text,'html.parser')
print(type(soup.title))
print(soup.a)

"""photo_tags = soup.find_all('img')
for images_tags in photo_tags:
    print(images_tags)
a_tags = soup.find_all('a')
for a_tags in a_tags:
    print(a_tags)"""

big_wb_div = soup.find('div', class_ = 'modulebody1')
print(big_wb_div)
