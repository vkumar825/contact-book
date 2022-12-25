from pymongo import MongoClient


class Database():

    def __init__(self):

        # mongodb uri string
        self.cluster = MongoClient("INSERT MONGODB CONNECTION URI HERE")
        self.db = self.cluster["contact-book"]
        self.collection = self.db["users"]

    def insert(self, email, name, phone_number):
        print(email)
        contact_to_insert = {"name": name, "phone_number": phone_number}
        self.collection.update_one(
            {'email': email}, {'$push': {'contacts': contact_to_insert}})

    def remove(self, email, name, phone_number):
        contact_to_insert = {"name": name, "phone_number": phone_number}
        self.collection.update_one(
            {'email': email}, {'$pull': {'contacts': contact_to_insert}})

    def fetch(self, email):
        for result in self.collection.find({"email": email}):
            return result["contacts"]

    def contains_user(self, email, password):

        # check if database contains the user
        if (self.collection.count_documents({"email": email}) == 1):
            for user_info in self.collection.find({"email": email}):
                if user_info["password"] == password:
                    return True
                else:
                    return False
        else:
            print("User does not exist")

    def create_user(self, email, password):

        # check if user already exists in database before inserting
        if self.contains_user(email, password):
            print("User already exists!")
        else:
            user_doc = {"email": email, "password": password, "contacts": []}
            self.collection.insert_one(user_doc)
            print("Successfully inserted user!")
