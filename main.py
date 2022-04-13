import requests
from bs4 import BeautifulSoup as bs4

github_user = input('Input Github User: ')
url = 'https://github.com/macmullensantiago'
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image =  soup.find('img', {'alt' : 'Avatar'})['src']
print(profile_image)


