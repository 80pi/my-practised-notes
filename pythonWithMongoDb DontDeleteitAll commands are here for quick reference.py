import pymongo

cc=pymongo.MongoClient()
# cc=python.MongoClient('localhost',27017) #or
# cc=pymongo.MongoClient("mongodb://localhost:27017/")

db=cc.school #if given db name is like "test-school"then
#db=cc.test-school # this line wont works so we need to use below line for group of list_database_names
# db=cc["test-school"]


# to see list of databses present in mongo db
# print(cc.list_database_names())

# to see list of collections present in mongo db
# print(db.list_collection_names())

# to see insert one document in databse in mongo db
# db.stu2.insert({"name":"ajay","age":"10","g":"m"})

# to see insert multiple document in databse in mongo db
# db.stu2.insert([{"name":"ajay1","age":"10","g":"f"},{"name":"ajay2","age":"10","g":"m"}])

# to get output of firest document(row)
# print(db.stu2.find_one())

# to print all find()
# for i in db.stu2.find():
    # print(i)

# to print only req column like name by negelecting _id
# for i in db.stu2.find({},{"_id":0,"name":1,"g":1}):
    # print(i)

# to print only req column with regular expression with name starts with a
# for i in db.stu2.find({"name":{"$regex":"^a"}}):
    # print(i)

# to sort ths documnet
# for i in db.stu2.find().sort("name"):#here our req feild need to write id/name/age/g(gender)
    # print(i)

# to sort ths documnet in desc
# for i in db.stu2.find().sort("name",-1):#here our req feild need to write id/name/age/g(gender)
    # print(i)

# to limit ths documnet
# for i in db.stu2.find().limit(2):#here our req feild need to write id/name/age/g(gender)
    # print(i)

# to skip ths documnet
# for i in db.stu2.find().skip(2):#here our req feild need to write id/name/age/g(gender)
    # print(i)

#delete only one collections with condition
# db.stu2.delete_one({"name":"ajay"})# here in our db ajay is deleted

#delete many collections with condition
# print(db.stu2.delete_many({"age":"10"}).deleted_count) #here in our db age=10  is deleted

# to count no of document in db
# print(db.stu2.count())

# to update one document
# db.stu2.update_one({"age":"10"},{"$set":{"age":"25"}})
# or
# db.stu2.update({"age":"10"},{"$set":{"age":"25"}})

## to update many document
# db.stu2.update_many({"age":"10"},{"$set":{"age":"25"}})
