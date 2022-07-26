
# how to delete the document from mongodb

import pymongo 

url='mongodb://localhost:27017'

mongoclient=pymongo.MongoClient(url)
db=mongoclient['mydb']
collection=db['student']

query={'name':'Sachin'}

result=collection.delete_one(query)
print(result.deleted_count)

'''
how to delete 

1. write the query which we want to delete
2. write the delete_one and pass the query
3. print deleted_count
'''