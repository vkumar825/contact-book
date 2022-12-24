# for unit testing
# from src.trie import Trie

# for tkinter app
from trie import Trie


class ContactBook():

    def __init__(self):

        # TODO: Use a list of dictionary instead of nested dict for mongodb
        self.trie = Trie()
        self.contacts = []
        self.search_result = []

    def add_contact(self, name, phone_number):

        if (len(self.contacts) > 0):
            for i in range(len(self.contacts)):
                if self.contacts[i].get("phone_number") == phone_number:
                    existing_contact = self.contacts[i].get("name")
                    raise Exception(
                        f"Failed to add contact. {phone_number} already used for contact {existing_contact}")

        if (name not in self.trie.query("")):
            self.trie.insert(name)
            self.contacts.append({"name": name,
                                  "phone_number": phone_number})
            self.contacts.sort(key=lambda x: x["name"])

        else:
            raise Exception(f"Failed to add contact. {name} already exists.")

    def remove_contact(self, name):

        if (len(self.trie.query(name)) == 0):
            raise Exception("Cannot remove non-existent name.")

        list_of_names = [d["name"] for d in self.contacts]
        for i in range(len(list_of_names)):
            if list_of_names[i] == name:
                self.contacts.pop(i)
                self.trie.delete(name)

    def get_contacts_by_search(self, search_input):

        if (len(search_input) == 0):
            self.search_result = self.contacts

        results = []
        list_of_names = self.trie.query(search_input)

        if (len(list_of_names) > 0):
            for i in range(len(list_of_names)):
                for j in range(len(self.contacts)):
                    if list_of_names[i] == self.contacts[j].get("name"):
                        results.append({"name": self.contacts[j].get("name"),
                                        "phone_number": self.contacts[j].get("phone_number")})
            self.search_result = results
        else:
            self.search_result = results

    def get_trie(self):
        return self.trie

    def get_contacts(self):
        return self.contacts

    def get_search_result(self):
        return self.search_result
