import pymongo
client = pymongo.MongoClient("mongodb+srv://jaimaa12:jaimaa12@mani.rvumdp1.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"mani",
    "email":"mchoudhury80@gmail.com",
    "surname":"choudhury"
}
db1 = client['mongotest']
cill = db1['test']
cill.insert_one(d)