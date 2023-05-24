import requests
import codecs
from bs4 import BeautifulSoup as Bs
from random import randint

__all__ = ('cian', 'm_2')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}


def cian(url, city=None, metro=None):

    apart = []
    errors = []
    if url:
        resp = requests.get(url, headers)
        if resp.status_code == 200:
            soup = Bs(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': '_93444fe79c--wrapper--W0WqH'})
            if main_div:
                div_list = main_div.find_all('div', attrs={'class': '_93444fe79c--wide--gEKNN'})
                for div in div_list:
                    title = div.find('span', attrs={'data-mark': 'OfferTitle'}).text
                    href = div.a['href']
                    content = div.find('div', attrs={'data-name': 'Description'}).text
                    main_price = div.find('span', attrs={'data-mark': 'MainPrice'}).text
                    res_complex = ' '
                    if div.find('div', attrs={'data-name': 'ContentRow'}):
                        res_complex = div.find('div', attrs={'data-name': 'ContentRow'}).string
                    apart.append({'title': title, 'url': href, 'residential_complex': res_complex,
                                  'description': content, 'price': main_price,
                                  'city_id': city, 'metro_id': metro})
            else:
                errors.append({'url': url, 'title': 'Div does not exists'})
        else:
            errors.append({'url': url, 'title': 'Page do not response'})

    return apart, errors


def m_2(url, city=None, metro=None):
    apart = []
    errors = []
    if url:
        resp = requests.get(url, headers)
        if resp.status_code == 200:
            soup = Bs(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': 'OffersSearch'})
            if main_div:
                div_list = main_div.find_all('li', attrs={'class': 'OffersSearchList__item'})
                for div in div_list:
                    if div.find('a', attrs={'class': 'LinkSnippet LinkSnippet_hover'}):
                        title = str(div.find('a', attrs={'class': 'LinkSnippet LinkSnippet_hover'}).text)
                    if div.a:
                        href = div.a['href']
                    if div.find('div', attrs={'class': 'LayoutSnippet__description'}):
                        content = div.find('div', attrs={'class': 'LayoutSnippet__description'}).text
                    if div.find('div', attrs={'class': 'Price'}):
                        main_price = div.find('div', attrs={'class': 'Price'}).text
                    res_complex = ' '
                    if div.find('div', attrs={'class': 'LayoutSnippet__building'}):
                        res_complex = div.find('div', attrs={'class': 'LayoutSnippet__building'}).text
                    apart.append({'title': title, 'url': href, 'residential_complex': res_complex,
                                  'description': content, 'price': main_price,
                                  'city_id': city, 'metro_id': metro})
            else:
                errors.append({'url': url, 'title': 'Div does not exists'})
        else:
            errors.append({'url': url, 'title': 'Page do not response'})

    return apart, errors


if __name__ == '__main__':
    url = 'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&metro%5B0%5D=352&offer_type=flat&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&room7=1&room9=1'
    #url = 'https://m2.ru/moskva/nedvizhimost/kupit-kvartiru/metro-petrovskii-park/second/?rooms=studiya&rooms=1-komnata&rooms=2-komnaty&rooms=5-komnat_i_bolee&rooms=4-komnaty&rooms=3-komnaty&rooms=svobodnaya-planirovka'
    apart, errors = cian(url)
    h = codecs.open('work.txt', 'w', 'utf-8')
    h.write(str(apart))
    h.close()

