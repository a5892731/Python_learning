'''
Take the code from the How To Decode A Website exercise
(if you didn’t do it or just want to play with some different code, use the code from the solution),
and instead of printing the results to a screen, write the results to a txt file. In your code,
just make up a name for the file you are saving to.

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

