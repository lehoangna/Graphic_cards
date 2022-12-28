import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy as db

engine = db.create_engine('mysql+mysqlconnector://root:admin@localhost:3306/graphic_card')
connection = engine.connect()

#get data from sql
data = pd.read_sql_table('information', connection)

top_rating = data.loc[:, ['title', 'rating']]
top_rating['rating'] = top_rating['rating'].str[9:]
top_rating['rating'] = pd.to_numeric(top_rating['rating'])
top_rating = top_rating.sort_values(by=['rating'], ascending=False)
print(top_rating.head(10))