class TrieNode:
    # Initialize your data structure here.
    li = []
    hasValue = False
    def __init__(self):
        self.li = [None]*26
        self.hasValue = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        def inserthelp(word,root,index):
            c = ord(word[index])-97
            if not root.li[c]:
                root.li[c] = TrieNode()
            if index+1==len(word):
                root.li[c].hasValue = True
            else:
                inserthelp(word,root.li[c],index+1)
        if len(word):
            inserthelp(word,self.root,0)

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        def searchhelp(word,root,index):
            c = ord(word[index]) - 97
            if not root.li[c]:
                return False
            if index+1==len(word):
                return root.li[c].hasValue
            else:
                return searchhelp(word,root.li[c],index+1)
        if len(word):
            return searchhelp(word,self.root,0)
        else:
            return True

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        def startshelp(word,root,index):
            c = ord(word[index])-97
            if not root.li[c]:
                return False
            if index+1==len(word):
                return True
            else:
                return startshelp(word,root.li[c],index+1)
        if len(prefix):
            return startshelp(prefix,self.root,0)
        else:
            return True
