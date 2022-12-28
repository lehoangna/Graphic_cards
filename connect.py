import sqlalchemy as db
from data import data

engine = db.create_engine('mysql+mysqlconnector://root:admin@localhost:3306/graphic_card')
connection = engine.connect()
data.to_sql('information', engine)

