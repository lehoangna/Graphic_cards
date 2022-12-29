import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy as db

engine = db.create_engine('mysql+mysqlconnector://root:admin@localhost:3306/graphic_card')
connection = engine.connect()

#get data from sql
data = pd.read_sql_table('information', connection)

product = data.loc[:, ['rating', 'price']]
product['rating'] = product['rating'].str[9:]
product['rating'] = pd.to_numeric(product['rating'])
product['price'] = product['price'].str.replace(',', '')
product['price'] = pd.to_numeric(product['price'])
plt.scatter(product['rating'], product['price'])
plt.show()