import random

class GameBoard:
    def __init__(self):
        self.board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.board_height = 4
        self.board_width = 4
        self.isAlive = True
        self.score = 0
        self.spawnValue()
        self.spawnValue()

    def displayBoard(self):
        print("--------------- Score: " + str(self.score) + " ------------------------")
        for i in range(self.board_height):
            for j in range(self.board_width):
                print(self.board[j][i], end="  ")
            print("\n")
        print("-------------------------------")

    def get_flat_board(self):
        flat_board = []

        for i in range(self.board_height):
            for j in range(self.board_width):
                flat_board.append(self.board[j][i])

        return flat_board

    def getScore(self):
        return self.score

    def spawnValue(self):

        empty_coords = []

        for i in range(self.board_width):
            for j in range(self.board_height):
                if(self.board[i][j] == 0):
                    empty_coords.append((i, j))


        selection_coord = random.randrange(0, len(empty_coords))
        point = empty_coords[selection_coord]

        value = random.randrange(0, 10)
        if(value == 0):
            self.board[point[0]][point[1]] = 4
            #Spawn 4
        else:
            self.board[point[0]][point[1]] = 2
            #Spawn 2
    
    def slideRight(self):
        cur_val = 0
        is_valid = False
        for row in range(self.board_height):
            list_vals = []

            #Generate the list of values including those that need to be added up
            for pre_col in range(self.board_width):
                col = (self.board_width - 1) - pre_col
                if(self.board[col][row] != 0 and self.board[col][row] == cur_val):
                    list_vals.append(cur_val * 2)
                    self.score += cur_val * 2
                    cur_val = 0
                elif(self.board[col][row] != 0 and cur_val == 0):
                    cur_val = self.board[col][row]
                elif(self.board[col][row] != 0 and self.board[col][row] != cur_val):
                    list_vals.append(cur_val)
                    cur_val = self.board[col][row]
            if(cur_val != 0):
                list_vals.append(cur_val)
                cur_val = 0

            #Insert the list of values into the current board
            for col in range(self.board_width):
                if(col < len(list_vals)):
                    if(self.board[(self.board_width - 1) - col][row] != list_vals[col]):
                        is_valid = True
                    self.board[(self.board_width - 1) - col][row] = list_vals[col]
                else:
                    self.board[(self.board_width - 1) - col][row] = 0
        if(is_valid):
            self.spawnValue()

    def slideLeft(self):
        cur_val = 0
        is_valid = False
        for row in range(self.board_height):
            list_vals = []

            #list vals = []
            #cur_val = 4

            #Generate the list of values including those that need to be added up
            for col in range(self.board_width):
                if(self.board[col][row] != 0 and self.board[col][row] == cur_val):
                    list_vals.append(cur_val * 2)
                    self.score += cur_val * 2
                    cur_val = 0
                elif(self.board[col][row] != 0 and cur_val == 0):
                    cur_val = self.board[col][row]
                elif(self.board[col][row] != 0 and self.board[col][row] != cur_val):
                    list_vals.append(cur_val)
                    cur_val = self.board[col][row]
            if(cur_val != 0):
                list_vals.append(cur_val)
                cur_val = 0

            #Insert the list of values into the current board
            for col in range(self.board_width):
                if(col < len(list_vals)):
                    if(self.board[col][row] != list_vals[col]):
                        is_valid = True
                    self.board[col][row] = list_vals[col]
                else:
                    self.board[col][row] = 0
        if(is_valid):
            self.spawnValue()


    def slideUp(self):
        cur_val = 0
        is_valid = False
        for col in range(self.board_width):
            list_vals = []

            #list vals = []
            #cur_val = 4

            #Generate the list of values including those that need to be added up
            for row in range(self.board_height):
                if(self.board[col][row] != 0 and self.board[col][row] == cur_val):
                    list_vals.append(cur_val * 2)
                    self.score += cur_val * 2
                    cur_val = 0
                elif(self.board[col][row] != 0 and cur_val == 0):
                    cur_val = self.board[col][row]
                elif(self.board[col][row] != 0 and self.board[col][row] != cur_val):
                    list_vals.append(cur_val)
                    cur_val = self.board[col][row]
            if(cur_val != 0):
                list_vals.append(cur_val)
                cur_val = 0

            #Insert the list of values into the current board
            for row in range(self.board_height):
                if(row < len(list_vals)):
                    if(self.board[col][row] != list_vals[row]):
                        is_valid = True
                    self.board[col][row] = list_vals[row]
                else:
                    self.board[col][row] = 0
        if(is_valid):
            self.spawnValue()

    def slideDown(self):
        cur_val = 0
        is_valid = False
        for col in range(self.board_width):
            list_vals = []

            #list vals = []
            #cur_val = 4

            #Generate the list of values including those that need to be added up
            for pre_row in range(self.board_height):
                row = (self.board_height - 1) - pre_row
                if(self.board[col][row] != 0 and self.board[col][row] == cur_val):
                    list_vals.append(cur_val * 2)
                    self.score += cur_val * 2
                    cur_val = 0
                elif(self.board[col][row] != 0 and cur_val == 0):
                    cur_val = self.board[col][row]
                elif(self.board[col][row] != 0 and self.board[col][row] != cur_val):
                    list_vals.append(cur_val)
                    cur_val = self.board[col][row]
            if(cur_val != 0):
                list_vals.append(cur_val)
                cur_val = 0

            #Insert the list of values into the current board
            for row in range(self.board_height):
                if(row < len(list_vals)):
                    if(self.board[col][(self.board_height - 1) - row] != list_vals[row]):
                        is_valid = True
                    self.board[col][(self.board_height - 1) - row] = list_vals[row]
                else:
                    self.board[col][(self.board_height - 1) - row] = 0
        if(is_valid):
            self.spawnValue()
    
    def checkBoard(self):
        available_move = False
        for row in range(self.board_height - 1):
            for col in range(self.board_width - 1):
                if(self.board[col][row] == self.board[col + 1][row] or self.board[col][row] == 0):
                    available_move = True
                    break
        if(available_move == False):
            for col in range(self.board_width - 1):
                for row in range(self.board_height - 1):
                    if(self.board[col][row] == self.board[col][row + 1] or self.board[col][row] == 0):
                        available_move = True       

        return available_move