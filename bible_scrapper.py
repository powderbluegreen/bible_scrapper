import requests
import bs4
import sys

url = 'https://www.biblegateway.com/passage'
bible_data = sys.argv[1]
variables = {'search': bible_data, 'version': 'NABRE'}
raw_html = requests.get(url, params=variables)
raw_html = raw_html.content
html = bs4.BeautifulSoup(raw_html, 'html.parser')
text = html.select(".version-NABRE p span")[0].contents
text.pop(0)

for i, j in enumerate(text):
    text[i] = j.string

text = ''.join(text)
print text
