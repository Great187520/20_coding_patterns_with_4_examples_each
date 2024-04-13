class TrieNode:
    def __init__(self):
        self.chidren = {}
        self.endOfWord = False

class Trie:
    def _init__(self):
        """
        Initialize your data structure
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie
        """
        cur = self.root

        for c in word:
            if c not in cur.chidren:
                cur.children[c] = TrieNode()
            cur = cur.chidren[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord 

    def startswith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True