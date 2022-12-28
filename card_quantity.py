import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy as db

engine = db.create_engine('mysql+mysqlconnector://root:admin@localhost:3306/graphic_card')
connection = engine.connect()

#get data from sql
data = pd.read_sql_table('information', connection)

quantity_by_brand = data.loc[:, ['brand']]
quantity_by_brand['brand'] = quantity_by_brand['brand'].replace('', 'Unknown brand')
quantity_by_brand = quantity_by_brand.groupby(['brand']).size().reset_index(name='count').sort_values(by=['count'])
quantity_by_brand.plot.bar( x='brand', y='count')

plt.show()
