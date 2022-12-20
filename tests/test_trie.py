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

        self.assertEqual(1, len(test_trie.query("A")))
        self.assertEqual(3, len(test_trie.query("B")))
        self.assertEqual(2, len(test_trie.query("Bo")))
        self.assertEqual(5, len(test_trie.query("")))

        # testing the order of insertion for all names
        self.assertEqual("Abigail", test_trie.query("")[0])
        self.assertEqual("Billy", test_trie.query("")[1])
        self.assertEqual("Bob", test_trie.query("")[2])
        self.assertEqual("Bobby Jones", test_trie.query("")[3])
        self.assertEqual("David", test_trie.query("")[4])

        # testing the order of insertion for names starting with B
        self.assertEqual("Billy", test_trie.query("B")[0])
        self.assertEqual("Bob", test_trie.query("B")[1])
        self.assertEqual("Bobby Jones", test_trie.query("B")[2])

    def test_delete(self):
        test_trie = Trie()

        test_trie.insert("David")
        test_trie.insert("Bob")
        test_trie.insert("Billy")
        test_trie.insert("Abigail")
        test_trie.insert("Bobby Jones")

        self.assertEqual(5, len(test_trie.query("")))
        self.assertEqual(1, len(test_trie.query("Bi")))

        test_trie.delete("Billy")

        self.assertEqual(4, len(test_trie.query("")))
        self.assertEqual(0, len(test_trie.query("Bi")))
