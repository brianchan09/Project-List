import certifi
import pymongo
from pymongo import MongoClient

cluster = MongoClient(
    f"mongodb+srv://Anson:ansonwong123@cluster0.77k1z.mongodb.net/personal_info?retryWrites=true&w=majority&ssl=true",
    tlsCAFile=certifi.where()) # open the database with the account
try: # get the main database
    cluster.server_info()
    database = cluster["personal_info"] # set the database
    backup_cluster = MongoClient(
        f"mongodb+srv://Him:Elvinw123@cluster0.y5oka.mongodb.net/Backup?retryWrites=true&w=majority&ssl=true",
        tlsCAFile=certifi.where()) # open back up database
    backup_database = backup_cluster["Backup"]# set to backup database
# if the main database is down for some reason, change the backup database to main
except pymongo.errors.PyMongoError as err:
    cluster = MongoClient(
        f"mongodb+srv://Him:Elvinw123@cluster0.y5oka.mongodb.net/Backup?retryWrites=true&w=majority&ssl=true",
        tlsCAFile=certifi.where()) # open back up database
    database = cluster["Backup"] # set the database
    backup_cluster = MongoClient(
        f"mongodb+srv://Anson:ansonwong123@cluster0.77k1z.mongodb.net/personal_info?retryWrites=true&w=majority&ssl=true",
        tlsCAFile=certifi.where()) # open main database
    backup_database = backup_cluster["personal_info"]# set to backup database

# database collection table
user_table = database["personal_info"]
art_table = database["digital_art"]
exchange_table = database["exchange"]
backup_user_table = backup_database["personal_info"]
backup_coll1 = backup_database["digital_art"]
backup_coll2 = backup_database["exchange"]
