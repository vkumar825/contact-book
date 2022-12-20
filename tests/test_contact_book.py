import unittest
from src.contact_book import ContactBook

class Test_ContactBook(unittest.TestCase):

    def test_add_contact(self):

        cb = ContactBook()

        cb.add_contact("Bob Smith", "123-324-8729")
        cb.add_contact("Michael Jackson", "182-265-1983")

        with self.assertRaises(Exception):

            # adding a contact that already exists
            cb.add_contact("Bob Smith", "123-324-8729")
            cb.add_contact("Bob Smith", "113-238-2827")

            # adding a contact with an existing phone number
            cb.add_contact("Chris Rock", "123-324-8729")

        
        cb.add_contact("Robert De Niro", "872-233-1873")
        cb.add_contact("James Bond", "672-334-1007")
        self.assertEqual(4, len(cb.get_contacts()))

    
    def test_remove_contact(self):

        cb = ContactBook()

        cb.add_contact("Bob Smith", "123-324-8729")
        cb.add_contact("Michael Jackson", "182-262-1965")
        cb.add_contact("Mike Schmidt", "182-265-1983")
        cb.add_contact("Michael Afton", "189-223-1983")
        cb.add_contact("Robert De Niro", "872-233-1873")
        cb.add_contact("James Bond", "672-334-1007")

        self.assertEqual(6, len(cb.get_contacts()))
        self.assertEqual(3, len(cb.get_trie().query("M")))

        print(cb.get_trie().query("M"))

        cb.remove_contact("Michael Afton")

        self.assertEqual(5, len(cb.get_contacts()))
        self.assertEqual(2, len(cb.get_trie().query("M")))

        print(cb.get_trie().query("M"))

