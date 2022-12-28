from bs4 import BeautifulSoup
import requests
import pandas as pd
# import csv
#
# with open('data-crawl.csv', 'w') as csv_file:
#     filenames = ['title', 'brand', 'rating', 'price', 'shipping', 'imgUrl']
#     writer = csv.DictWriter(csv_file, fieldnames=filenames)
#     writer.writeheader()

title = []
brand = []
rating = []
price = []
shipping = []
imgUrl = []

def process_crawling(pagination):
    pagination = str(pagination)
    page = 'https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48/Page-' + pagination + '?Tid=7709'
    result = requests.get(page)
    source = result.text
    soup = BeautifulSoup(source, 'html.parser')
    cards = soup.findAll('div', class_='item-cell')

    for i in range(len(cards)):
        full_price = 'Out of stock OR See price in cart'
        check_rating = ''
        check_brand = ''
        if(len(cards[i].select('.price-current > strong')) > 0):
            full_price = cards[i].select('.price-current > strong')[0].text + cards[i].select('.price-current > sup')[0].text
        if(len(cards[i].select('.item-branding .item-rating')) > 0):
            check_rating = cards[i].select('.item-branding .item-rating')[0].attrs['title']
        if (len(cards[i].select('img')) > 1):
            check_brand = cards[i].select('img')[1]['title']

        title.append(cards[i].select('img')[0]['src'])
        brand.append(check_brand)
        rating.append(check_rating)
        price.append(full_price)
        shipping.append(cards[i].select('.price-ship')[0].text)
        imgUrl.append(cards[i].select('img')[0]['src'])

for i in range(1,101):
    process_crawling(i)

data_raw = {
    'title': title,
    'brand': brand,
    'rating': rating,
    'price': price,
    'shipping': shipping,
    'imgUrl': imgUrl
}

data = pd.DataFrame(data_raw, columns=['title', 'brand', 'rating', 'price', 'shipping', 'imgUrl'])

# data.to_csv(r'C:\Users\MSI GF\Desktop\DE Coaching\Projects\Graphic_cards\data-crawl.csv')

# print(data_df.head())


# print(soup.findAll('div', class_='item-cell')[0].select('img')[0]['src'])     img
# print(soup.findAll('div', class_='item-cell')[0].select('img')[0]['title'])   title
# print(soup.findAll('div', class_='item-cell')[0].select('img')[1]['title'])   branding
# print(soup.findAll('div', class_='item-cell')[0].select('.item-branding .item-rating')[0].attrs['title'])   rating
# print(soup.findAll('div', class_='item-cell')[0].select('.price-current > strong')[0].text + soup.findAll('div', class_='item-cell')[0].select('.price-current > sup')[0].text)   price
# print(soup.findAll('div', class_='item-cell')[0].select('.price-ship')[0].text)   shipping

