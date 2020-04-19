import time

SudokuNormal = [[0,2,0,5,1,9,0,0,0],
                [0,5,0,7,0,0,0,1,0],
                [0,6,0,2,0,0,9,0,0],
                [6,8,5,0,2,3,0,0,0],
                [0,0,0,0,0,0,8,0,2],
                [0,7,0,1,4,0,0,0,0],
                [7,0,1,0,0,0,0,5,9],
                [0,0,0,0,0,1,0,0,7],
                [0,3,0,4,9,0,0,2,1]]


# SudokuÇözüm = [[8,2,3,5,1,9,7,4,6],
#                [4,5,9,7,3,6,2,1,8],
#                [1,6,7,2,8,4,9,3,5],
#                [6,8,5,9,2,3,1,7,4],
#                [3,1,4,6,7,5,8,9,2],
#                [9,7,2,1,4,8,5,6,3],
#                [7,4,1,8,6,2,3,5,9],
#                [2,9,6,3,5,1,4,8,7],
#                [5,3,8,4,9,7,6,2,1]]

SudokuHardest = [[8,0,0,0,0,0,0,0,0],
                 [0,0,3,6,0,0,0,0,0],
                 [0,7,0,0,9,0,2,0,0],
                 [0,5,0,0,0,7,0,0,0],
                 [0,0,0,0,4,5,7,0,0],
                 [0,0,0,1,0,0,0,3,0],
                 [0,0,1,0,0,0,0,6,8],
                 [0,0,8,5,0,0,0,1,0],
                 [0,9,0,0,0,0,4,0,0]]

count = 0

def find_empty(Sudo):
    for x in range(9):
        for y in range(9):
            if Sudo[x][y] == 0:
                return x,y


    return None,None


def control(Sudo,x,y,Number):

    for i in range(9):
        if Sudo[x][i] == Number:
            return False

    for j in range(9):
        if Sudo[j][y] == Number:
            return False

    box_X = x // 3
    box_Y = y // 3

    for m in range(box_X * 3, box_X * 3 + 3):
        for n in range(box_Y * 3, box_Y * 3 + 3):
            if Sudo[m][n] == Number:
                return False

    return True

def solve(Sudo):
    global count
    count += 1
    x,y = find_empty(Sudo)

    if x == None:
        return True
    else:
        for i in range(1,10):

            if control(Sudo,x,y,i):
                Sudo[x][y] = i
                # print(Sudo) # Adım adım görmek için
                if solve(Sudo):
                    return Sudo

                Sudo[x][y] = 0


    return False


t1 = time.time()
print(f"Normal Sudoku = {SudokuNormal}"
      f"Solution Normal S. = {solve(SudokuNormal)}")
t2 = time.time() - t1

NormalCount = count
count = 0 # reset count

t3 = time.time()
print(f"Hardest Sudoku = {SudokuNormal}"
      f"Solution Hardest S. = {solve(SudokuHardest)}")
t4 = time.time() - t3

print(f"Hardest takes {count} steps, Normal takes {NormalCount}\n"
      f"Hardest takes {t4} seconds, Normal takes {t2} seconds.")