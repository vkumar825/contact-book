import unittest

# need to uncomment line 2 in contact_book.py to run the tests below
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

        cb.remove_contact("Michael Afton")
        self.assertEqual(5, len(cb.get_contacts()))
        self.assertEqual(2, len(cb.get_trie().query("M")))


        self.assertEqual(1, len(cb.get_trie().query("J")))
        cb.remove_contact("James Bond")
        self.assertEqual(4, len(cb.get_contacts()))
        self.assertEqual(0, len(cb.get_trie().query("J")))

        # attempting to remove non-existent name
        self.assertEqual(0, len(cb.get_trie().query("H")))
        with self.assertRaises(Exception):
            cb.remove_contact("Harry Styles")

    def test_get_contacts_by_search(self):

        cb = ContactBook()

        cb.add_contact("Bob Smith", "123-324-8729")
        cb.add_contact("Michael Jackson", "182-262-1965")
        cb.add_contact("Mike Schmidt", "182-265-1983")
        cb.add_contact("Manny Smith", "189-223-1983")
        cb.add_contact("Michael Jordan", "189-223-1992")
        cb.add_contact("Michelle Lawrence", "189-333-1322")
        cb.add_contact("Morgan Yoder", "612-846-8337")
        cb.add_contact("Morgana", "202-918-2132")
        cb.add_contact("Matthew Smith", "213-622-9425")
        cb.add_contact("Matthew", "505-351-5452")
        cb.add_contact("Robert De Niro", "872-233-1873")
        cb.add_contact("James Bond", "672-334-1007")

        self.assertEqual(12, len(cb.get_contacts()))

        cb.get_contacts_by_search("M")
        self.assertEqual(9, len(cb.get_search_result()))
        self.assertEqual(9, len(cb.get_trie().query("M")))

        list_of_ordered_names = cb.get_trie().query("M")
        
        for i in range(len(list_of_ordered_names)):
            self.assertEqual(
                list_of_ordered_names[i], cb.get_search_result()[i].get('name'))

        # searching for all should return back 12 contacts
        cb.get_contacts_by_search("")
        self.assertEqual(12, len(cb.get_contacts()))
        list_of_ordered_names = cb.get_trie().query("")

        # both get_search_result and get_contacts should be the same 
        for i in range(len(list_of_ordered_names)):
            self.assertEqual(
                list_of_ordered_names[i], cb.get_search_result()[i].get('name'))
            self.assertEqual(
                list_of_ordered_names[i], cb.get_contacts()[i].get('name'))

        cb.get_contacts_by_search("Ma")
        self.assertEqual(3, len(cb.get_search_result()))
        self.assertEqual(3, len(cb.get_trie().query("Ma")))
        self.assertEqual(12, len(cb.get_contacts()))

        list_of_ordered_names = cb.get_trie().query("Ma")
        for i in range(len(list_of_ordered_names)):
            self.assertEqual(
                list_of_ordered_names[i], cb.get_search_result()[i].get('name'))

        # searching for contact that doesn't exist yields 0 result
        cb.get_contacts_by_search("Y")
        self.assertEqual(0, len(cb.get_search_result()))
