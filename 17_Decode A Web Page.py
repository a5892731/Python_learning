'''
Use the BeautifulSoup and requests Python packages to print out
a list of all the article titles on the New York Times homepage.

https://www.nytimes.com/

https://www.practicepython.org
'''

import requests
from bs4 import BeautifulSoup


# >>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<
print("-------------------------------------------------------------------------")
print("this program prints all the article titles on the New York Times homepage")


url = 'http://www.nytimes.com'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser") # "html.parser" is for get rid of warnings > https://stackoverflow.com/questions/33511544/how-to-get-rid-of-beautifulsoup-user-warning
headline_data = soup.find_all("h2") # <h2>This is heading 2</h2>

number_of_headline = 1
for item in headline_data:  # item is headline with atributs <h2>

    if "Site" in item.text: #remove site bookmarks
        continue
    else:
        print("{}) >>> {}".format(number_of_headline, item.text)) # item.text is our headline with out atributes <h2>
        number_of_headline += 1
