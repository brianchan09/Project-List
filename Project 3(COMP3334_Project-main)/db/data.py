from db.params import user_table, art_table, exchange_table

# combine all search db into 1 function
# search target collection from database
def search_db(target_table, data):
    if target_table == user_table: # if the collection in personal info
        user = list(user_table.find({"username": data})) # get the username
        if not user:
            return user
        else:
            return user[0]
    elif target_table == art_table: # if the collection is digit art
        digital_art = art_table.find({"_id": data})# get the id
        if not digital_art:
            return digital_art
        else:
            return digital_art[0]
    else:
        exchange_block = exchange_table.find({"_id": data}) # remain is the exchange collection
        if not exchange_block:
            return exchange_block
        else:
            return exchange_block[0]