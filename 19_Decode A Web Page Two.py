'''
Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website:
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that
you can read the full article without having to click any buttons.

(Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the solution
of the exercise posted here.)

This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise
we will learn how to write this text to a .txt file.
'''


import requests
from bs4 import BeautifulSoup


# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<



url = requests.get('https://web.archive.org/web/20140529103427/http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')
html = url.text
page = BeautifulSoup(html, 'html.parser')
match = page.find_all('div', 'parbase cn_text')
page_list = [[k.get_text() for k in i.find_all('p')] for i in match]

file = open('19_Decode A Web Page Two.txt', 'w', encoding="utf-8")

for i in page_list[:-2]:
    for k in i:
        print(k + '\n', file=file)

print("check file:  19_Decode A Web Page Two.txt")
file.close()
