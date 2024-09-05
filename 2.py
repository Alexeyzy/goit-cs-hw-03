from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

client = MongoClient(
    "mongodb+srv://a03221983:alexeyb344@cluster0.e7awz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1')
)

db = client.book

# # Створення
result_many = db.cats.insert_many(
    [{"name": "Lama","age": 2,"features": ["ходить в лоток", "не дає себе гладити", "сірий"],},
    {"name": "Liza","age": 4,"features": ["ходить в лоток", "дає себе гладити", "білий"],},
    {"name": "barsik","age": 3,"features": ["ходить в капці", "дає себе гладити", "рудий"],}])
print(result_many.inserted_ids)

# # Пошук
find_all = db.cats.find({})
for el in find_all:
    print(el)

cat_name = input("Введіть імя кота: ")
find_cat = db.cats.find_one({"name": cat_name})
if find_cat is not None:
    print(find_cat)
else:
    print("Такого імя не має!")

    
# # Оновлення
cat_name = input("Введіть імя кота для оновлення віку: ")
find_cat = db.cats.find_one({"name": cat_name})

if find_cat is not None:
    cat_age = input("Введіть вік для оновлення: ")   
    db.cats.update_one({"name": cat_name}, {"$set": {"age": cat_age}})
    print("Вік оновленно!")
else:
    print("Такого імя не має!")

    
# Додати характеристику
cat_name = input("Введіть імя кота для додавання характеристики: ")
find_cat = db.cats.find_one({"name": cat_name})

if find_cat is not None:
    cat_features = [input("Введіть характеристику: ")]
    db.cats.update_one({"name": cat_name}, {"$addToSet": {"features": {"$each": cat_features}}})
    find_cat = db.cats.find_one({"name": cat_name})
    print(find_cat)
    print("Характеристика додана!")
else:
    print("Такого імя не має!")


# # Видалення
cat_name = input("Введіть імя кота для видалення: ")
find_cat = db.cats.find_one({"name": cat_name})

if find_cat is not None:
    db.cats.delete_one({"name": cat_name})
    print(cat_name, "Кота видалено!")
else:
    print("Такого імя не має!")

delete_all = int(input("Видалити всіх? 1-Так, 2-Ні: "))
if delete_all == 1:
    db.cats.delete_many({})
    print("Всіх котів видалено!")


    



