
# Insert one document in mongodb database

import pymongo 

url='mongodb://localhost:27017'

mongoclient=pymongo.MongoClient(url)
db=mongoclient['mydb']
collection=db['student']

document={'name':'Sachin','rno':55,'loc':'Mumbai'}

result=collection.insert_one(document)
print(result.inserted_id)

'''
steps in inserting one document in mongodb

1. import pymongo
2. give the url 'mongodb://localhost:27017'
3. create a mongoclient
4. create database
5. create collection
6. create document
7. inert the document by using collection
8. use inserted_id and then print

'''