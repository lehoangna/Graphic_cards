from bs4 import BeautifulSoup
import requests
import pandas as pd

FIRST_PAGE = 1
LAST_PAGE = 101

title = []
brand = []
rating = []
price = []
shipping = []
imgUrl = []
rating_num = []

def process_crawling(pagination):
    pagination = str(pagination)
    page = 'https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48/Page-' + pagination + '?Tid=7709'
    result = requests.get(page)
    source = result.text
    soup = BeautifulSoup(source, 'html.parser')
    cards = soup.findAll('div', class_='item-cell')

    for i in range(len(cards)):
        full_price = '0'
        check_rating = ''
        check_brand = ''
        check_num_rating = '0'
        if(len(cards[i].select('.price-current > strong')) > 0):
            full_price = cards[i].select('.price-current > strong')[0].text + cards[i].select('.price-current > sup')[0].text
        if(len(cards[i].select('.item-branding .item-rating')) > 0):
            check_rating = cards[i].select('.item-branding .item-rating')[0].attrs['title']
            check_num_rating = cards[i].select('.item-rating-num')[0].text[1:-1]
        if (len(cards[i].select('img')) > 1):
            check_brand = cards[i].select('img')[1]['title']

        title.append(cards[i].select('img')[0]['src'])
        brand.append(check_brand)
        rating.append(check_rating)
        price.append(full_price)
        shipping.append(cards[i].select('.price-ship')[0].text)
        imgUrl.append(cards[i].select('img')[0]['src'])
        rating_num.append(check_num_rating)


for i in range(FIRST_PAGE, LAST_PAGE):
    process_crawling(i)

data_raw = {
    'title': title,
    'brand': brand,
    'rating': rating,
    'price': price,
    'shipping': shipping,
    'imgUrl': imgUrl,
    'rating_num': rating_num
}

data = pd.DataFrame(data_raw, columns=['title', 'brand', 'rating', 'price', 'shipping', 'imgUrl', 'rating_num'])


