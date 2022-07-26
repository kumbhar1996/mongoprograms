

# inerted the many document in the mongodb

import pymongo 

url='mongodb://localhost:27017'

mongoclient=pymongo.MongoClient(url)

db=mongoclient['mydb']
collection=db['student']

document={'name':'akshay','rno':1,'loc':'pune'},{'name':'sandip','rno':100,'loc':'solapur'}

result=collection.insert_many(document)
print(result.inserted_ids)