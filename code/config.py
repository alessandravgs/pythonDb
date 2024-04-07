from pymongo import MongoClient

#Conexão MySql
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/test'

#Conexão MongoDb

cliente = MongoClient('mongodb://localhost:27017')
mongodb = cliente['banco']
pedidos_collection = mongodb['pedidos']
