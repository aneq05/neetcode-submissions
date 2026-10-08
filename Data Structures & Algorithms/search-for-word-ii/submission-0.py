class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        # 1. Inicjalizacja Trie
        root = TrieNode()

        # 2. Dodanie wszystkich szukanych słów do Trie
        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]

            node.word = word

        # 3. Przygotowanie zmiennych
        rows = len(board)
        cols = len(board[0])
        result = []

        # 4. DFS - przeszukiwanie planszy
        def dfs(r, c, node):

            # 4.1. Sprawdzenie granic planszy
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            char = board[r][c]

            # 4.2. Sprawdzenie, czy znak pasuje do Trie
            if char not in node.children:
                return

            # 4.3. Przejście do kolejnego węzła Trie
            node = node.children[char]

            # 4.4. Sprawdzenie, czy znaleziono całe słowo
            if node.word is not None:
                result.append(node.word)
                node.word = None

            # 4.5. Oznaczenie aktualnej komórki jako odwiedzonej
            board[r][c] = "#"

            # 4.6. DFS dla czterech sąsiadów
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            # 4.7. Backtracking - przywrócenie znaku
            board[r][c] = char

        # 5. Uruchomienie DFS z każdej komórki
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        # 6. Zwrócenie znalezionych słów
        return result