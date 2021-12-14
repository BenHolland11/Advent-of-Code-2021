with open('input.txt') as f:
    lines = f.readlines()
    lines.append('\n')

numbers = lines[0]
numbers = numbers[:len(numbers)-1]
numbers = list(numbers.split(','))

boards = []
currentBoard = []
for line in lines[2:]:
    if line == '\n':
        boards.append(currentBoard)
        currentBoard = []
    else:
        currentBoard.append(list(map(int, line.split())))

def calcBoard(board, lastNum):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != -1:
                total += board[i][j]
    print(board)
    print(int(total)*int(lastNum))
    exit()

def checkHorizontal(r, board, lastNum):
    if sum(r) == -5:
        calcBoard(board, lastNum)
    else:
        return False

def checkVertical(b, lastNum):
    for i in range(0, 5):
      sum = 0
      sum = b[0][i]+b[1][i]+b[2][i]+b[3][i]+b[4][i]
      if sum == -5:
        calcBoard(b, lastNum)
      else:
        return False

for num in numbers:
    for board in range(len(boards)):
        for row in range(len(boards[board])):
            for number in range(len(boards[board][row])):                
                if int(num) == int(boards[board][row][number]):   
                    boards[board][row][number] = -1
                    checkHorizontal(boards[board][row], boards[board], num)
                    checkVertical(boards[board], num)
                