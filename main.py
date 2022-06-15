import requests
from bs4 import BeautifulSoup
import pprint

def request_func(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titlelink')
    subtext = soup.select('.subtext')
    return links, subtext

page1 = request_func('https://news.ycombinator.com/news')
page2 = request_func('https://news.ycombinator.com/news?p=2')

def sorted_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse = True)


def create_costum_hn(links, subtext):
    hn =  []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sorted_votes(hn)


pprint.pprint(create_costum_hn(page1[0], page1[1]))
pprint.pprint(create_costum_hn(page2[0], page2[1]))
