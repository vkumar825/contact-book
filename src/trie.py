class TrieNode:
    def __init__(self, char):

        self.char = char
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):

        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_word = True

    def delete(self, word):
        node = self.root

        for char in word[:-1]:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        if word[-1] in node.children:
            del node.children[word[-1]]
            return True
        else:
            return False

    def dfs(self, node, prefix):
        if node.is_word:
            self.output.append(prefix + node.char)

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):

        self.output = []
        node = self.root

        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        self.dfs(node, x[:-1])

        # to be stored in alphabetical order
        return sorted(self.output)
