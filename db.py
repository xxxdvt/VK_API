import dotenv
import pymongo

config = dotenv.dotenv_values(".env")

mongo_client = pymongo.MongoClient(config["HOST"], int(config["PORT"]))
db = mongo_client[config["MONGO_DATABASE"]]
collection = db[config["MONGO_COLLECTION"]]


def create_dataset():
    return [
        {
            "title":         item["title"],
            "image_url":     item["image_url"],
            "price":         item["price"],
            "discount":      item["discount"],
            "referral_link": item["referral_link"],
        } for item in collection.find()
    ]

