from pymongo import MongoClient

monogodb_url = "mongodb+srv://erickGAmaris:1234@cluster0.vqqagay.mongodb.net/?retryWrites=true&w=majority"
port = 8000

conn = MongoClient(monogodb_url, port)
db = conn["tiendaOnline"]