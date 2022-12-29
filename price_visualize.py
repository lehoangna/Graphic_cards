import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy as db

engine = db.create_engine('mysql+mysqlconnector://root:admin@localhost:3306/graphic_card')
connection = engine.connect()

#get data from sql
data = pd.read_sql_table('information', connection)

fig, axs = plt.subplots(1, 2)

price_df = data.loc[:, ['price']]
price_df['price'] = price_df['price'].str.replace(',', '')
price_df['price'] = pd.to_numeric(price_df['price'])
axs[0].hist(price_df['price'])

price_by_brand = data.loc[:, ['brand', 'price']]
price_by_brand['brand'] = price_by_brand['brand'].replace('', 'Unknown brand')
price_by_brand = price_by_brand.groupby(['brand', 'price']).size().reset_index(name='count')
price_by_brand = price_by_brand.pivot(index='brand', columns='price', values='count')
price_by_brand = price_by_brand.fillna(0)
print(price_by_brand.head())

plt.show()