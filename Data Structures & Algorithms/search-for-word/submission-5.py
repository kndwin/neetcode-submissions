class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        exist = False

        def backtrack(curr, row, col, visited):
            nonlocal exist

            if curr == word:
                exist = True
                return 
            
            if len(curr) > len(word):
                return

            char = word[len(curr)]
            hasVisited = visited.get((row, col))
            if not hasVisited:
                visited[(row, col)] = True

            print(char, curr)
            # up
            if row > 0 and board[row-1][col] == char and not visited.get((row-1, col)):
                backtrack(curr+char, row-1, col, visited)
            # down
            if row < len(board)-1 and board[row+1][col] == char and not visited.get((row+1, col)):
                backtrack(curr+char, row+1, col, visited)
            # left
            if col > 0 and board[row][col-1] == char and not visited.get((row, col-1)):
                backtrack(curr+char, row, col-1, visited)
            # right
            if col < len(board[0])-1 and board[row][col+1] == char and not visited.get((row, col+1)):
                backtrack(curr+char, row, col+1, visited)
            
            visited[(row, col)] = False 
            return

        for row in range(len(board)):
            for col in range(len(board[0])):
                char = board[row][col]
                if char == word[0]:
                    backtrack(char, row, col, {})
                if exist:
                    break


        return exist
        