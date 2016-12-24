import requests
import bs4
import argparse
import random
import time

url = 'https://www.biblegateway.com/passage'
parser = argparse.ArgumentParser(description='Generates Bible Verses')
parser.add_argument('-n', nargs='+')
parser.add_argument('-r', type=int)
args = parser.parse_args()
options = vars(args)['r']
def get_random_verse(iterations):
    for i in range(iterations):
        try:
            time.sleep(.5)
            url_books = 'https://www.biblegateway.com/versions/New-American-Bible-Revised-Edition-NABRE-Bible/#booklist'
            raw_html = requests.get(url_books).content
            html = bs4.BeautifulSoup(raw_html, 'html.parser')
            book_list = html.select('table tr')
            book = random.choice(book_list)
            chapter_list = book.select('a')
            chapter = random.choice(chapter_list)
            chapter_url_r = chapter['href']
            chapter_url_a = 'https://www.biblegateway.com' + str(chapter_url_r)
            time.sleep(.5)
            raw_html = requests.get(chapter_url_a).content
            html = bs4.BeautifulSoup(raw_html, 'html.parser')
            # print html
            para_list = html.select('.version-NABRE > p')
            # print para_list
            para = random.choice(para_list)
            verse_list = para.select('.text')
            verse = random.choice(verse_list)
            text = verse.contents[1]
            print text
        except IndexError as e:
            pass

def getdata(data):
    for i in data:
        print i
        variables = {'search': i, 'version': 'NABRE'}
        raw_html = requests.get(url, params=variables)
        raw_html = raw_html.content
        html = bs4.BeautifulSoup(raw_html, 'html.parser')
        text = html.select(".version-NABRE p span")[0].contents
        text.pop(0)

        for i, j in enumerate(text):
            text[i] = j.string

        text = ''.join(text)
        print text


if options:
    get_random_verse(options)
else:
    getdata(vars(args)['n'])
