import requests
import random
from bs4 import BeautifulSoup
import datetime

url = "https://pixelford.com/blog/"

random_numbers = random.randint(1,999)
response = requests.get(url, headers= {'user-agent' : f'Hello {random_numbers}'})
# this could be another way to implement user agent
# response = requests.get(url, headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})
html = response.content
soup = BeautifulSoup(html, 'html.parser')
a_tags = soup.find_all('a', class_="entry-title-link")

#for a_tag in a_tags:
    #print(a_tag.get_text())
titles = list(map(lambda a_tag: a_tag.get_text(), a_tags ))
print(titles)

#print(requests.utils.default_headers())

soups = BeautifulSoup(html, 'html.parser')
blogs = soups.find_all('article', class_="type-post")

for blog in blogs:
    title = blog.find('a',class_="entry-title-link").get_text()
    time_tag_string = blog.find('time', class_="entry-time").get('datetime')
    blog_datetime = datetime_tag = datetime.datetime.fromisoformat(time_tag_string)
    pretty_time = blog_datetime.strftime("%B %d %Y")
    print(f"{pretty_time} - {title}")