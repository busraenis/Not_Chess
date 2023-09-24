

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
piece_dict_w = {
    'P' : -1,
    'R' : -5,
    'N' : -3,
    'B' : -3,
    'Q' : -9,
    'K' : -999,
}
list_piece_w = list(piece_dict_w)

piece_dict_b = {
    'p': 1,
    'r': 5,
    'n': 3,
    'b': 3,
    'q': 9,
    'k': 999
}
list_piece_b = list(piece_dict_b)
board = [ 0, 1, 2, 3, 4, 5, 6, 7, 8,
          'a','R','P','-','-','-','-','p','r',
          'b','N','P','-','-','-','-','p','n',
          'c','B','P','-','-','-','-','p','b',
          'd','Q','P','-','-','-','-','p','q',
          'e','K','P','-','-','-','-','p','k',
          'f','N','P','-','-','-','-','p','n',
          'g','B','P','-','-','-','-','p','b',
          'h','R','P','-','-','-','-','p','r']

def board11():
    for n in range(8, -1, -1):
        if n in board:
            if n==8:
                print(n, board[17], board[26], board[35], board[44], board[53], board[62], board[71], board[80])
            if n==7:
                print(n, board[16], board[25], board[34], board[43], board[52], board[61], board[70], board[79])
            if n==6:
                print(n, board[15],board[24], board[33], board[42], board[51], board[60], board[69], board[78])
            if n==5:
                print(n, board[14], board[23], board[32], board[41], board[50], board[59], board[68], board[77])
            if n==4:
                print(n, board[13], board[22], board[31], board[40], board[49], board[58], board[67], board[76])
            if n==3:
                print(n, board[12], board[21], board[30], board[39], board[48], board[57], board[66], board[75])
            if n==2:
                print(n, board[11], board[20], board[29], board[38], board[47], board[56], board[65], board[74])
            if n==1:
                print(n, board[10], board[19], board[28], board[37], board[46], board[55], board[64], board[73])
            if n==0:
                print(' ', board[9], board[18], board[27], board[36], board[45], board[54], board[63], board[72])
        else:
            print('hh')
board11()


score = 0
player = 0
while True:

    if player % 2 == 0:
        print("White's turn")

        move = input()  # e 2 e 4
        location = list(move)
        ilk_row = int(location[1]) #2
        ilk_column = ord(str(location[0])) - 96 #1. e
        next_row = int(location[3]) #4
        next_column = ord(str(location[2])) - 96 #2. e

        a = board[ilk_row]
        if a in board and a != 0:
            a1 = int(a)
            curr_loc = 9*ilk_column + a1
            if curr_loc >= 81:
                print('Invalid Move!')
            else:
                elimdeki_tas = board[curr_loc]
                if elimdeki_tas == '-':
                    print('SCORE:', score)
                    print('Invalid Move!')


                else:
                    next_loc= 9*next_column + next_row
                    if next_loc >= 81:
                        print('Invalid Move!')
                    else:
                        gidecegi_tas = board[next_loc]
                        if gidecegi_tas == '-':
                            board[curr_loc] = '-'
                            board[next_loc] = elimdeki_tas
                            board11()
                            print('SCORE:', score)
                            player += 1


                        elif gidecegi_tas in list_piece_w:
                            print('SCORE:', score)
                            print('Invalid Move!')

                        elif gidecegi_tas == 'k':
                            board[curr_loc] = '-'

                            score += 999
                            board[next_loc] = elimdeki_tas
                            print('SCORE:', score)
                            print('GAME OVER !')
                            print('WHITE WON !')
                            break

                        else:
                            board[curr_loc] = '-'
                            c = piece_dict_b.get(gidecegi_tas)
                            score += c
                            board[next_loc] = elimdeki_tas
                            board11()
                            print('SCORE:', score)
                            player += 1


        else:
            print('Invalid Move!')

    else:
        print("Black's turn")
        move = input()  # e 2 e 4
        location = list(move)
        ilk_row = int(location[1])  # 2
        ilk_column = ord(str(location[0])) - 96  # 1. e
        next_row = int(location[3])  # 4
        next_column = ord(str(location[2])) - 96  # 2. e

        a = board[ilk_row]
        if a in board and a !=0:
            a1 = int(a)
            curr_loc = 9 * ilk_column + a1
            if curr_loc >= 81:
                print('Invalid Move!')
            else:
                elimdeki_tas = board[curr_loc]
                if elimdeki_tas == '-':
                    print('SCORE:', score)
                    print('Invalid Move!')

                else:
                    next_loc = 9 * next_column + next_row
                    if next_loc >= 81:
                        print('Invalid Move!')
                    else:
                        gidecegi_tas = board[next_loc]
                        if gidecegi_tas == '-':
                            board[curr_loc] = '-'
                            board[next_loc] = elimdeki_tas
                            board11()
                            print('SCORE:', score)
                            player += 1


                        elif gidecegi_tas in list_piece_b:
                            print('SCORE:', score)
                            print('Invalid Move!')

                        elif gidecegi_tas == 'K':
                            board[curr_loc] = '-'
                            score -= 999
                            board[next_loc] = elimdeki_tas
                            print('SCORE:', score)
                            print('GAME OVER !')
                            print('BLACK WON !')
                            break
                        else:
                            board[curr_loc] = '-'
                            c = piece_dict_w.get(gidecegi_tas)
                            score += c
                            board[next_loc] = elimdeki_tas
                            board11()
                            print('SCORE:', score)
                            player += 1

        else:
            print('Invalid Move!')





# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE