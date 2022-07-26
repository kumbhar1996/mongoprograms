
# update the document in mongodb

import pymongo

url='mongodb://localhost:27017'

mongoclient=pymongo.MongoClient(url)

db=mongoclient['mydb']
collection=db['student']

query={'name':'akshay'}
updated_data={'$set':{'rno':60,'loc':'Hydrabad'}}

result=collection.update_one(query,updated_data)

print(result.modified_count)


'''
How to update one document

1. write querry which we want to update document
2. which things we want to update these things write inside the updateddata
3. by using $set
4. pass the two parameters querry,updated data
5. during printing write modified count
'''
