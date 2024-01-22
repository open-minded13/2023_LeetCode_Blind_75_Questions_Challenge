# Date of Last Practice: Jan 9, 2024
#
# Time Complexity: O(N^2 * M^2), where N is the number of rows and M is the number of columns.
#                  For each cell that matches the first letter of the word, we perform a DFS.
#                  The worst-case time complexity of DFS in a grid is O(N*M).
#                  However, since we have multiple possible starting points, in the worst case,
#                  this could be every cell in the grid.
#                  Therefore, the time complexity is O(N*M*N*M) = O(N^2 * M^2).
#                  The time complexity might seem high,
#                  but given the small size of the grid and word, it's quite reasonable.
#
# Space Complexity: O(N*M), where N is the number of rows and M is the number of columns.
#                   The space complexity is mainly due to the 'visited' array.


from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dfs_sources = []
        row_length = len(board)
        col_length = len(board[0])
        for i in range(row_length):
            for j in range(col_length):
                if board[i][j] == word[0]:
                    dfs_sources.append((i, j))

        visited = [[False for _ in range(col_length)] for _ in range(row_length)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(source, cur_level):
            if cur_level == len(word):
                return False

            (row, col) = source
            if board[row][col] == word[cur_level]:
                if cur_level == len(word) - 1:
                    return True

                visited[row][col] = True
                word_exists = False
                for r, c in directions:
                    if (
                        0 <= row + r < row_length
                        and 0 <= col + c < col_length
                        and visited[row + r][col + c] == False
                    ):
                        word_exists = (
                            dfs((row + r, col + c), cur_level + 1) or word_exists
                        )
                visited[row][col] = False
                return word_exists
            else:
                return False

        for source in dfs_sources:
            if dfs(source, 0):
                return True

        return False


# Test cases
sol = Solution()

# Provided test cases
assert (
    sol.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
    )
    == True
)
assert (
    sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
    == True
)
assert (
    sol.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
    )
    == False
)

# Additional test cases
assert sol.exist([["A"]], "A") == True  # Single cell, matching word
assert (
    sol.exist([["A", "A", "A"], ["A", "A", "A"], ["A", "A", "A"]], "AAAA") == True
)  # Word formed in a square
assert (
    sol.exist([["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]], "AEI") == False
)  # Non-adjacent cells

print("All test cases passed!")