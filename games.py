import random
import os

if "variables" == "variables":
    choice = 0

    oTile = "\033[1;34;40m[O]"
    xTile = "\033[1;31;40m[X]"
    blankTile = "\033[1;37;40m[ ]"
    tl = blankTile
    tm = blankTile
    tr = blankTile
    ml = blankTile
    mm = blankTile
    mr = blankTile
    bl = blankTile
    bm = blankTile
    br = blankTile
    num1 = 1
    num2 = 2
    num3 = 3

    error = 0

    win = 0

    ticPick = "tl"

def rngGame():

    num1 = int(input("Minimum range: "))
    num2 = int(input("Maximum range: "))
    rngNum = random.randrange(num1, num2, 1)
    correct = False
    guess = 0

    while correct == False:
        guess = int(input("Guess: "))
        if  (rngNum == guess):
            print("Correct")
            correct = True
        elif (rngNum != guess):
            correct = False
            if guess >= rngNum:
                print("Lower")
            elif guess <= rngNum:
                print("Higher")

def TicP1(taken):

    global tl
    global tm
    global tr
    global ml
    global mm
    global mr
    global bl
    global bm
    global br
    global win
    global error

    clearScreen()
    if taken == 1:
        print("Taken, pick again")

    print('\033[1;37;40m    1   2   3', '\n', '\033[1;37;40m1', tl, tm, tr, '\n', '\033[1;37;40m2', ml, mm, mr, '\n', '\033[1;37;40m3', bl, bm, br)
    print("\033[1;37;40mPick column 1, 2, or 3")
    column = int(input('Player 1: '))
    clearScreen()
    print('\033[1;37;40m    1   2   3', '\n', '\033[1;37;40m1', tl, tm, tr, '\n', '\033[1;37;40m2', ml, mm, mr, '\n', '\033[1;37;40m3', bl, bm, br)
    print("\033[1;37;40mPick row 1, 2, or 3")
    row = int(input('Player 1: '))

    if column == 1:
        if row == 1 and tl == blankTile:
            tl = xTile
        elif row == 2 and ml == blankTile:
            ml = xTile
        elif row == 3 and bl == blankTile:
            bl = xTile
        else:
            print('Taken, Pick again')
            TicP1(1)
    if column == 2:
        if row == 1 and tm == blankTile:
            tm = xTile
        elif row == 2 and mm == blankTile:
            mm = xTile
        elif row == 3 and bm == blankTile:
            bm = xTile
        else:
            print('Taken, Pick again')
            TicP1(1)
    if column == 3:
        if row == 1 and tr == blankTile:
            tr = xTile
        elif row == 2 and mr == blankTile:
            mr = xTile
        elif row == 3 and br == blankTile:
            br = xTile
        else:
            print('Taken, Pick again')
            TicP1(1)
    print('\033[1;37;40m    1   2   3', '\n', '\033[1;37;40m1', tl, tm, tr, '\n', '\033[1;37;40m2', ml, mm, mr, '\n', '\033[1;37;40m3', bl, bm, br)

def clearScreen():  
    print("\033[1;37;40m\n" * 100)  

def TicP2(taken):

    global tl
    global tm
    global tr
    global ml
    global mm
    global mr
    global bl
    global bm
    global br
    global win
    global error

    clearScreen()
    if taken == 1:
        print("Taken, pick again")

    print('\033[1;37;40m    1   2   3', '\n', '\033[1;37;40m1', tl, tm, tr, '\n', '\033[1;37;40m2', ml, mm, mr, '\n', '\033[1;37;40m3', bl, bm, br)
    print("\033[1;37;40mPick column 1, 2, or 3")
    try:
        column = int(input('Player 2: '))
    except ValueError:
        print('Error, try again')
    clearScreen()
    print('\033[1;37;40m    1   2   3', '\n', '\033[1;37;40m1', tl, tm, tr, '\n', '\033[1;37;40m2', ml, mm, mr, '\n', '\033[1;37;40m3', bl, bm, br)
    print("\033[1;37;40mPick row 1, 2, or 3")
    row = int(input('Player 2: '))

    if column == 1:
        if row == 1 and tl == blankTile:
            tl = oTile
        elif row == 2 and ml == blankTile:
            ml = oTile
        elif row == 3 and bl == blankTile:
            bl = oTile
        else:
            print('Taken, Pick again')
            TicP2(1)
    if column == 2:
        if row == 1 and tm == blankTile:
            tm = oTile
        elif row == 2 and mm == blankTile:
            mm = oTile
        elif row == 3 and bm == blankTile:
            bm = oTile
        else:
            print('Taken, Pick again')
            TicP2(1)
    if column == 3:
        if row == 1 and tr == blankTile:
            tr = oTile
        elif row == 2 and mr == blankTile:
            mr = oTile
        elif row == 3 and br == blankTile:
            br = oTile
        else:
            print('Taken, Pick again')
            TicP2(1)
    print('\033[1;37;40m    1   2   3', '\n', '\033[1;37;40m1', tl, tm, tr, '\n', '\033[1;37;40m2', ml, mm, mr, '\n', '\033[1;37;40m3', bl, bm, br)

def TicWin():
    global tl
    global tm
    global tr
    global ml
    global mm
    global mr
    global bl
    global bm
    global br
    global win

    if tl == xTile and tm == xTile and tr == xTile:
        win = 1
    elif tl == oTile and tm == oTile and tr == oTile:
        win = 2
    elif ml == xTile and mm == xTile and mr == xTile:
        win = 1
    elif ml == oTile and mm == oTile and mr == oTile:
        win = 2
    elif bl == xTile and bm == xTile and br == xTile:
        win = 1
    elif bl == oTile and bm == oTile and br == oTile:
        win = 2
    elif tl == xTile and ml == xTile and bl == xTile:
        win = 1
    elif tl == oTile and ml == oTile and bl == oTile:
        win = 2
    elif tm == xTile and mm == xTile and bm == xTile:
        win = 1
    elif tm == oTile and mm == oTile and bm == oTile:
        win = 2
    elif tr == xTile and mr == xTile and br == xTile:
        win = 1
    elif tr == oTile and mr == oTile and br == oTile:
        win = 2
    elif tl == xTile and mm == xTile and br == xTile:
        win = 1
    elif tl == oTile and mm == oTile and br == oTile:
        win = 2
    elif tr == xTile and mm == xTile and bl == xTile:
        win = 1
    elif tr == oTile and mm == oTile and bl == oTile:
        win = 2

def P1Win():
    clearScreen()
    print('\033[1;37;40m                          __________        ___     ')
    print('                          |  _____  \      /   |    ')
    print('                          | |     |  \    /_/| |    ')
    print('                          | |_____|  /       | |    ')
    print('                          | _______ /        | |    ')
    print('                          | |                | |    ')
    print('                          | |                | |    ')
    print('                          | |                | |    ')
    print('                          | |                | |    ')
    print('                          | |                | |    ')
    print('                          | |              __| |__  ')
    print('                          |_|             |_______| ')
    print('                                                                        ')
    print('___                __                ____ _____________   _          _  ')
    print('\  \              /  \              /  / |_____   _____| | \        | | ')
    print(' \  \            /    \            /  /        | |       |  \       | | ')
    print('  \  \          /  /\  \          /  /         | |       |   \      | | ')
    print('   \  \        /  /  \  \        /  /          | |       | |\ \     | | ')
    print('    \  \      /  /    \  \      /  /           | |       | | \ \    | | ')
    print('     \  \    /  /      \  \    /  /            | |       | |  \ \   | | ')
    print('      \  \  /  /        \  \  /  /             | |       | |   \ \  | | ')
    print('       \  \/  /          \  \/  /              | |       | |    \ \ | | ')
    print('        \    /            \    /          _____| |_____  | |     \ \| | ')
    print('         \__/              \__/          |_____________| |_|      \___| ')

def P2Win():
    clearScreen()
    print('\033[1;37;40m                      __________        _________')
    print('                      |  _____  \      /  ______ \ ')
    print('                      | |     |  \     \_/     /  \ ')
    print('                      | |_____|  /            /   / ')
    print('                      | _______ /            /   / ')
    print('                      | |                   /   /')
    print('                      | |                  /   / ')
    print('                      | |                 /   / ')
    print('                      | |                /   / ')
    print('                      | |               /   / ')
    print('                      | |              /   /______ ')
    print('                      |_|             |___________| ')
    print('                                                                        ')
    print('___                __                ____ _____________   _          _  ')
    print('\  \              /  \              /  / |_____   _____| | \        | | ')
    print(' \  \            /    \            /  /        | |       |  \       | | ')
    print('  \  \          /  /\  \          /  /         | |       |   \      | | ')
    print('   \  \        /  /  \  \        /  /          | |       | |\ \     | | ')
    print('    \  \      /  /    \  \      /  /           | |       | | \ \    | | ')
    print('     \  \    /  /      \  \    /  /            | |       | |  \ \   | | ')
    print('      \  \  /  /        \  \  /  /             | |       | |   \ \  | | ')
    print('       \  \/  /          \  \/  /              | |       | |    \ \ | | ')
    print('        \    /            \    /          _____| |_____  | |     \ \| | ')
    print('         \__/              \__/          |_____________| |_|      \___| ')

if "start" == "start":
    clearScreen()
    print("\033[1;37;40mWelcome to Game Center, What would you like to play?")
    print("\033[1;37;40m1. Guess the Number")
    print("\033[1;37;40m2. Tic-Tac-Toe")
    choice = int(input("\033[1;37;40m1-2: "))

if choice == 1:
    rngGame()

elif choice == 2:

    tl = blankTile
    tm = blankTile
    tr = blankTile
    ml = blankTile
    mm = blankTile
    mr = blankTile
    bl = blankTile
    bm = blankTile
    br = blankTile
    print('\033[1;37;40m    1   2   3', '\n', '\033[1;37;40m1', tl, tm, tr, '\n', '\033[1;37;40m2', ml, mm, mr, '\n', '\033[1;37;40m3', bl, bm, br)
    while win == 0:     
        TicP1(0)
        turn = 1
        TicWin()
        if win == 1:
            P1Win()
            break
        TicP2(0)
        turn = 2
        TicWin()
        if win == 2:
            P2Win()
            break
        