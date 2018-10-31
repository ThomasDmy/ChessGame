
class Board():
    def __init__(self):
        self.row = 8
        #Board initialisation. Everything at None, waiting pieces creation 
        self.board = [[None for x in range(self.row)] for y in range(self.row)]


    '''
    print_board : print the board :
    +---...-----+
    |T|F|...|P|P|
    +-----------+
    ...


    '''
    def print_board(self): 
        print("\n\n\t\t BOARD : \n ")
        border_line = "+---------------------------------------+"
        print(border_line)
        for line in range(self.row):
            str_line = "|"
            for column in range(self.row):
                #Overwrite the print function of each pieces 
                str_line += str(self.board[line][column])
                str_line += "|"
            print(str_line)
            print(border_line)

                

        