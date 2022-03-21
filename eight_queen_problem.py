from tabnanny import check
from time import sleep


MUTATION_PROBABILITY = 0.01
CROSSOVER_PROBABILITY = 0.7
CHROMOSOME_POPULATION = 100

# Define the chess board, 1 - represents queens
chess_board = [
    [1, 1, 1, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Chess board to test for row breaks
# Expected result - [0, 1, 1, 0, 1, 0, 0, 0]
row_test_chess_board = [
    [1, 0, 0, 0, 1, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 1, 0, 0, 0], 
    [0, 1, 0, 0, 1, 0, 0, 0], 
    [0, 0, 0, 0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0, 1, 0, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1]
]

# Chess board to test for column breaks
# Expected result - [0, 1, 0, 1, 1, 0, 1, 0]
column_test_chess_board = [
    [1, 0, 0, 0, 1, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 1, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 1, 1, 0], 
    [0, 0, 0, 0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0],
]

diagonal_test_chess_board = [
    [1, 0, 0, 0, 1, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0]
]
# Define the chromosomes - This will keep changing with every iteration
chromosomes = []

# Define rows for validity - 1: Valid, 0: Invalid
check_rows = [1, 1, 1, 1, 1, 1, 1, 1]
# Define columsn for validity 
check_columns = [1, 1, 1, 1, 1, 1, 1, 1]

def check_row_validity():

    print("\nCheck Row Validity method called")

    for i in range(8):
        queen_exists_row = False
        for j in range(8):
            print("Element: [", i, "][", j, "]: ", row_test_chess_board[i][j])

            # Queen found at the spot
            if row_test_chess_board[i][j] == 1:
                # Queen already exists and another found
                if queen_exists_row:
                    print("Row ", i, ": Second Queen found")
                    check_rows[i] = 0
                    break
                # Queen does not exist in row yet
                else:
                    print("Row ", i, ": First Queen found")
                    queen_exists_row = True
            else:
                if j == 7:
                    if not queen_exists_row:
                        print("Row ", i, ": No Queens in Row")
                        check_rows[i] = 0
    print(check_rows)

def check_column_validity():
    
    print("\nCheck Column Validity method called")

    for i in range(8):
        queen_exists_column = False
        for j in range(8):
            
            print("Element: [", j, "][", i, "]: ", row_test_chess_board[j][i])

            # Queen found at the spot
            if column_test_chess_board[j][i] == 1:
                # Queen already exists and another found
                if queen_exists_column:
                    print("Column ", i, ": Second Queen found")
                    check_columns[i] = 0
                    break
                # Queen does not exist in row yet
                else:
                    print("Column ", i, ": First Queen found")
                    queen_exists_column = True
            else:
                if j == 7:
                    if not queen_exists_column:
                        print("Column ", i, ": No Queens in Column")
                        check_columns[i] = 0
    
    print(check_columns)

# This is a dedicated method to check for a diagonal attack
# Assumption - Chosen element is a 1
def check_diagonal_validity(chess_board, i, j):

    print("\nCheck Diagonal Validity method called")
    print("Element: [", i, "][", j, "]: ", chess_board[i][j])
    original_i = i
    original_j = j

    # Find the first element to start checking at for primary diagonal
    if i < j:
        ni = 0
        nj = j - i
    elif j < i:
        ni = i - j
        nj = 0
    else:
        ni = 0
        nj = 0

    print("Primary Diagonal Start Element: [", ni, "][", nj, "]: ", chess_board[ni][nj])
    
    # Loop for Primary diagonal
    while ni <= 7 and nj <= 7:

        print(ni, original_i, nj, original_j)
        
        # If its 1 break and return false
        if chess_board[ni][nj] == 1:
            # Skip the iteration when they are equal
            if ni == original_i and nj == original_j:
                ni += 1
                nj += 1        
                continue
            else:
                print("Issue with Primary Diagonal: Element: [", ni, "][", nj, "]: ", chess_board[ni][nj])
                return False

        ni += 1
        nj += 1

    print("Primary Diagonal valid")

    # Find the first element to start checking at for primary diagonal
    if i + j < 7:
        ni = i + j
        nj = 0
    elif i + j > 7: 
        ni = 7
        nj = j - (7 - i)
    else:
        ni = 7
        nj = 0

    print("Alternate Diagonal Start Element: [", ni, "][", nj, "]: ", chess_board[ni][nj])
    
    # Loop for Alternate diagonal
    while ni >= 0 and nj <= 7:

        print(ni, original_i, nj, original_j)

        # If its 1 break and return false
        if chess_board[ni][nj] == 1:
            # Skip the iteration when they are equal
            if ni == original_i and nj == original_j:
                ni -= 1
                nj += 1
                continue
            else:
                print("Issue with Alternate Diagonal: Element: [", ni, "][", nj, "]: ", diagonal_test_chess_board[ni][nj])
                return False

        ni -= 1
        nj += 1
    
    print("Alternate Diagonal valid")
    return True


# Check validity for the chess board
def check_validity_board():

    # Print the board for testing
    for i in range(len(chess_board)):
        for j in range(len(chess_board[i])):
            if chess_board[i][j] == 1:
                print("QUEEN")
            else:
                print("EMPTY")
    print("-------------------------------")

    check_row_validity()
    check_column_validity()              
    test_i = 0
    test_j = 0
    check_diagonal_validity(diagonal_test_chess_board, test_i, test_j)              

# Method to perform Mutation
def mutation(parent):
    pass

# Method to perform Crossover
def crossover(parent1, parent2):
    pass

# Method to perform Cloning
def cloning():
    pass

def main(): 
    check_validity_board()

if __name__ == '__main__':
    main()