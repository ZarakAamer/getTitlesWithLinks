from operator import ne
import requests
from bs4 import BeautifulSoup
import pandas

questionlist = []
offstes = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000,
           24000, 25000, 26000, 27000, 28000, 29000, 30000, 31000, 32000, 33000, 34000, 35000, 36000, 37000, 38000, 39000, 40000, 41000, 42000, 43000, 44000, 45000, 46000, 47000]
for offset in offstes:
    print(offset)
    url = f'https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}' + \
        '&profile=default&search=intitle%3Astate&advancedSearch-current={%22fields%22:{%22intitle%22:%22state%22}}&ns0=1'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    questions = soup.find_all('div', {'class': 'mw-search-result-heading'})
    for item in questions:
        question = {
            'title': item.find('a').text,
            'link': 'https://en.wikipedia.org/'+item.find('a')['href'],
        }
        questionlist.append(question)

    # url = 'https://en.wikipedia.org/', str(
#     #     soup.find('a', {'class': 'mw-nextlink'})['href'])

df = pandas.DataFrame(questionlist)
df.to_excel('Words.xlsx', index=False)
print('Fin.')
