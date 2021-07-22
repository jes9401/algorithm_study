import pandas as pd
import pymongo
from pymongo import MongoClient
import datetime
client = MongoClient('121.133.48.198', 27017)
db = client['test']
collection = db['result']
t = datetime.datetime.now()
print(t,type(t))
res = collection.find({'Time':{'$gt':'2021-07-15T13:40'}})
a=[]
for r in res :
    a.append(r)

result = pd.DataFrame([a[0]])

for i in range(1,len(a)):
    temp = pd.DataFrame([i])
    #temp.drop('_id',inplace=True,axis=1)
    result = pd.concat([result,temp],axis=0)
display(result)
print(result.columns)
