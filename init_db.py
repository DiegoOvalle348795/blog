from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

# Conexión con MongoDB local
client = MongoClient("mongodb://localhost:27017/")
db = client["blog_db"]

# Limpiar datos anteriores
db.users.delete_many({})
db.categories.delete_many({})
db.articles.delete_many({})
db.comments.delete_many({})

# Insertar usuarios de ejemplo (sin hash por simplicidad en pruebas)
users = [
    {"email": "alice@example.com", "password": "1234"},
    {"email": "bob@example.com", "password": "abcd"}
]
db.users.insert_many(users)

# Insertar categorías
categories = [
    {"name": "Tecnología"},
    {"name": "Educación"},
    {"name": "Noticias"}
]
db.categories.insert_many(categories)

# Insertar artículos
articles = [
    {
        "title": "Bienvenido al Blog",
        "content": "Este es el primer post de prueba. Esperamos que te guste.",
        "author": "alice@example.com",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "category": "Tecnología"
    },
    {
        "title": "Avances Educativos",
        "content": "Exploramos las nuevas tendencias en educación online.",
        "author": "bob@example.com",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "category": "Educación"
    }
]
article_ids = db.articles.insert_many(articles).inserted_ids

# Insertar comentarios
comments = [
    {
        "post_id": article_ids[0],
        "content": "Muy interesante el artículo!",
        "author": "bob@example.com",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    },
    {
        "post_id": article_ids[1],
        "content": "Gracias por compartir esta información.",
        "author": "alice@example.com",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
]
db.comments.insert_many(comments)

print("✅ Datos de ejemplo cargados en blog_db.")