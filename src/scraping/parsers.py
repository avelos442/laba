import requests

from bs4 import BeautifulSoup as Bs


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
                    else:
                        title = ''
                    if div.a:
                        href = div.a['href']
                    else:
                        href = ''
                    if div.find('div', attrs={'class': 'LayoutSnippet__description'}):
                        content = div.find('div', attrs={'class': 'LayoutSnippet__description'}).text
                    else:
                        content = ''
                    if div.find('div', attrs={'class': 'Price'}):
                        main_price = div.find('div', attrs={'class': 'Price'}).text
                    else:
                        main_price = ''
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


'''
if __name__ == '__main__':
    apart, errors = cian(url)
    h = codecs.open('work.txt', 'w', 'utf-8')
    h.write(str(apart))
    h.close()
'''
