import unittest
from src.trie import *


class Test_Trie(unittest.TestCase):

    def test_insert(self):
        test_trie = Trie()

        test_trie.insert("David")
        test_trie.insert("Bob")
        test_trie.insert("Billy")
        test_trie.insert("Abigail")
        test_trie.insert("Bobby Jones")

        self.assertEqual(1, len(test_trie.search("A")))
        self.assertEqual(3, len(test_trie.search("B")))
        self.assertEqual(2, len(test_trie.search("Bo")))
        self.assertEqual(5, len(test_trie.search("")))

        # testing the order of insertion for all names
        self.assertEqual("David", test_trie.search("")[0])
        self.assertEqual("Bob", test_trie.search("")[1])
        self.assertEqual("Bobby Jones", test_trie.search("")[2])
        self.assertEqual("Billy", test_trie.search("")[3])
        self.assertEqual("Abigail", test_trie.search("")[4])

        # testing the order of insertion for names starting with B
        self.assertEqual("Bob", test_trie.search("B")[0])
        self.assertEqual("Bobby Jones", test_trie.search("B")[1])
        self.assertEqual("Billy", test_trie.search("B")[2])

    def test_delete(self):
        test_trie = Trie()

        test_trie.insert("David")
        test_trie.insert("Bob")
        test_trie.insert("Billy")
        test_trie.insert("Abigail")
        test_trie.insert("Bobby Jones")

        self.assertEqual(5, len(test_trie.search("")))
        self.assertEqual(1, len(test_trie.search("Bi")))

        test_trie.delete("Billy")

        self.assertEqual(4, len(test_trie.search("")))
        self.assertEqual(0, len(test_trie.search("Bi")))
