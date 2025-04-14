def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check this row on left side
        for i in range(col):
            if board[row][i] == 1:
                return False
        
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # Check lower diagonal on left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        return True

    def solve_util(board, col):
        # Base case: If all queens are placed
        if col >= n:
            solutions.append([row[:] for row in board])
            return True
        
        res = False
        # Consider this column and try placing queen in all rows one by one
        for i in range(n):
            if is_safe(board, i, col):
                # Place this queen in board[i][col]
                board[i][col] = 1
                
                # Make result true if any placement is possible
                res = solve_util(board, col + 1) or res
                
                # If placing queen in board[i][col] doesn't lead to a solution,
                # then remove queen from board[i][col]
                board[i][col] = 0  # Backtrack
        
        return res

    # Initialize all solutions
    solutions = []
    
    # Create an empty board
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    solve_util(board, 0)
    
    return solutions

def print_solutions(solutions):
    for i, solution in enumerate(solutions, 1):
        print(f"Solution {i}:")
        for row in solution:
            print(" ".join("Q" if cell == 1 else "." for cell in row))
        print()

# Example usage for 4-queens problem
n = 4
solutions = solve_n_queens(n)
print(f"Total solutions for {n}-queens problem: {len(solutions)}")
print_solutions(solutions)
