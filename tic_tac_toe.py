#GLOBAL VARIABLES
#original empty 3x3 array
array=[['1','1','1'], ['1','1','1'], ['1','1','1']]

#previous player global variable
previous=2
#end_of_game global variable
end_of_game=False

#print the gaming board
def print_board(arr):
    for i in xrange(3):
        print arr[i]

#function to check if the point is not empty
def not_empty(point):
    x=(point-1)/3
    y=(point-1)%3
    return (array[x][y]=='X' or array[x][y]=='O')

#function to check the choice
def check_choice():
    global choice
    read_var=raw_input("give me your point with a number between 1-9 ")
    choice=int(read_var)

    while (choice<1 or choice>9):
        print 'wrong choice again'
        read_var = raw_input("give me your point with a number between 1-9 ")
        choice=int(read_var)
        print choice

#play_game
def play_game(player):
    global choice
    print 'Player ', player
    check_choice()

    while not_empty(choice):
        print 'this point is not empty'
        check_choice()

    if player==1:
        array[(choice-1)/3][(choice-1)%3]='X'
    else:
        array[(choice - 1) / 3][(choice - 1) % 3] = 'O'


#check if someone wins
def is_winner(arr):
    flag=False

    for i in range(0,3):
        if arr[i][0]==arr[i][1]==arr[i][2]=='X' or arr[i][0]==arr[i][1]==arr[i][2]=='O':
            flag=True
    for j in range(0,3):
        if arr[0][j]==arr[1][j]==arr[2][j]=='X' or arr[0][j]==arr[1][j]==arr[2][j]=='O':
            flag=True
    if arr[0][0]==arr[1][1]==arr[2][2]=='X'or arr[0][0]==arr[1][1]==arr[2][2]=='O':
        flag =True
    if arr[2][0]==arr[1][1]==arr[0][2]=='X' or arr[2][0]==arr[1][1]==arr[0][2]=='O':
        flag=True
    print 'winner? ', flag
    return flag


#play player1 or player2
def next_player():
    global previous
    if previous==1:
        play_game(2)
        previous=2
    else:
        play_game(1)
        previous=1

#check if board is full
def board_is_full(arr):
    flag=True
    for i in range(3):
        for j in range(3):
            if arr[i][j]=='1':
                flag=False

    return flag


print_board(array)
while not end_of_game:
    next_player()
    if is_winner(array):
        end_of_game=True
    if board_is_full(array):
        end_of_game=True
    print_board(array)


