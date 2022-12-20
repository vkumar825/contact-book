from src.trie import *


class ContactBook():

    def __init__(self):
        self.trie = Trie()
        self.contacts = {}

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

    def get_contacts(self):
        return self.contacts

    def get_trie(self):
        return self.trie
