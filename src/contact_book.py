# for unit testing
# from src.trie import Trie

# for tkinter app
from trie import Trie


class ContactBook():

    def __init__(self):
        self.trie = Trie()
        self.contacts = {}
        self.search_result = {}

    def add_contact(self, name, phone_number):

        if (len(self.contacts) > 0):
            for contact in self.contacts.values():
                if contact["phone_number"] == phone_number:
                    existing_contact = contact["name"]
                    raise Exception(
                        f"Failed to add contact. {phone_number} already used for contact {existing_contact}")

        if (name not in self.trie.query("")):
            self.trie.insert(name)
            self.contacts[len(self.trie.query("")) - 1] = {"name": name,
                                                           "phone_number": phone_number}

        else:
            raise Exception(f"Failed to add contact. {name} already exists.")

    def remove_contact(self, name):

        temp_dict = {}

        for key in self.contacts.keys():
            if self.contacts[key]["name"] == name:
                key_to_remove = key

        self.trie.delete(name)

        for key, value in self.contacts.items():
            if key < key_to_remove:
                temp_dict[key] = value
            elif key > key_to_remove:
                temp_dict[key-1] = value
            else:
                continue

        self.contacts = temp_dict

    def get_ordered_contacts(self):

        temp_dict = {}

        # getting the keys from nested dict in the alphabetical order of names
        sorted_keys = [key for key in dict(
            sorted(self.contacts.items(), key=lambda x: x[1]["name"]))]

        for i in range(len(self.trie.query(""))):
            temp_dict[i] = {"name": self.contacts.get(sorted_keys[i]).get("name"),
                            "phone_number": self.contacts.get(sorted_keys[i]).get("phone_number")}

        self.contacts = temp_dict

    def get_contacts_by_search(self, search_input):

        if (len(search_input) == 0):
            self.get_ordered_contacts()

        search_dict = {}
        list_of_names = self.trie.query(search_input)

        if (len(list_of_names) > 0):
            for i in range(len(list_of_names)):
                for contact in self.contacts.values():
                    if list_of_names[i] == contact["name"]:
                        search_dict[i] = {"name": contact["name"],
                                          "phone_number": contact["phone_number"]}
            self.search_result = search_dict

        else:
            self.search_result = search_dict

    def get_trie(self):
        return self.trie

    def get_contacts(self):
        return self.contacts

    def get_search_result(self):
        return self.search_result
