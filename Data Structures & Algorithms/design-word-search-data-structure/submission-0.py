class TreeNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TreeNode()

            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        
        def dfs(i, node):

            # 1
            if i == len(word):
                return True

            # 2 
            char = word[i]
            if char == '.':
                for letter in node.children:
                    child = node.children[letter]
                    result = dfs(i+1, child)

                    if result == True:
                        return True

                return False

            # 3
            for char in word:
                if char not in node.children:
                    return False

            node = node.children[char]

        return dfs(0, self.root)

