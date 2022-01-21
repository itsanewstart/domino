import random

all_domino = [[1, 4], [1, 3], [2, 3], [4, 5], [2, 2], [0, 3], [6, 6], [0, 6],
                [5, 5], [4, 4], [4, 6], [0, 1], [0, 5], [1, 6], [2, 5], [1, 2],
                [3, 6], [0, 0], [0, 2], [5, 6], [3, 5], [2, 4],
                [3, 4], [1, 5], [0, 4], [2, 6], [3, 3], [1, 1]]
doubles_set = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], []]
stock_pieces = []
computer_pieces = []
player_pieces = []
status = None
def give_dominos():
    while len(stock_pieces) < 14:
        stock_index = random.choice(all_domino)
        stock_pieces.append(stock_index)
    while len(computer_pieces) < 7:
        comp_index = random.choice(all_domino)
        if comp_index not in stock_pieces and comp_index not in computer_pieces:
            computer_pieces.append(comp_index)
    while len(player_pieces) < 7:
        play_index = random.choice(all_domino)
        if play_index not in stock_pieces and play_index not in computer_pieces and play_index not in player_pieces:
            player_pieces.append(play_index)
#  checking first player
move_list = []
for i in range(7, -1, -1):
    if doubles_set[i] in player_pieces:
        move_list.append(doubles_set[i])
        player_pieces.remove(doubles_set[i])
        status = 'player'
        break
    elif doubles_set[i] in computer_pieces:
        move_list.append(doubles_set[i])
        computer_pieces.remove(doubles_set[i])
        status = 'computer'
        break
    else:
        give_dominos()

def make_a_move():
    global player_pieces, computer_pieces, stock_pieces, move_list, status
    #  player makes a move
    if status == 'player':
        print('Status: It\'s your turn to make a move. Enter your command.')
        move = int(input())
        move_into_list = list(str(move))
        #  check if str or other invalid data
        if move_into_list[0] == '-':
            index_move_list = list(str(move))
            int_index = int(index_move_list[1]) - 1
            move_list.insert(0, player_pieces[int_index])
            player_pieces.remove(player_pieces[int_index])
            status = 'computer'
            return player_pieces, move_list, status
            interface()
        elif move > 0:
            index_move_list = list(str(move))
            int_index = int(index_move_list[0]) - 1
            move_list.append(player_pieces[int_index])
            player_pieces.remove(player_pieces[int_index])
            status = 'computer'
            return player_pieces, move_list, status
            interface()
        elif move_into_list[0] == '0':
            take_piece = random.choice(stock_pieces)
            player_pieces.append(take_piece)
            stock_pieces.remove(take_piece)
            status = 'computer'
            return player_pieces, stock_pieces, status
            interface()
    #  computer makes a move
    if status == 'computer':
        print('Status: Computer is about to make a move. Press Enter to continue...')
        prompt_player = input()
        if prompt_player == '':
            computer_move = random.choice(computer_pieces)
            first_num = move_list[0][0]
            move_list_len = len(move_list) - 1
            last_num = move_list[move_list_len][1]
            if computer_move[1] == first_num:
                move_list.insert(0, computer_move)
                computer_pieces.remove(computer_move)
                status = 'player'
                return computer_pieces, move_list, status
                interface()
            elif computer_move[0] == last_num:
                move_list.append(computer_move)
                computer_pieces.remove(computer_move)
                status = 'player'
                return computer_pieces, move_list, status
                interface()
            else:
                take_piece = random.choice(stock_pieces)
                computer_pieces.append(take_piece)
                stock_pieces.remove(take_piece)
                status = 'player'
                return computer_pieces, stock_pieces, status
                interface()
        else:
            print('Invalid input. Please try again.')
            make_a_move()

def check_status():
    if len(computer_pieces) == 0:
        print('Status: The game is over. The computer won!')
    elif len(player_pieces) == 0:
        print('Status: The game is over. You won!')
    elif len(stock_pieces) == 0:
        print('Status: The game is over. It\'s a draw!')
    else:
        make_a_move()

def interface():
    print('='*70)
    print('Stock size:', len(stock_pieces))
    print('Computer pieces:', len(computer_pieces))
    print()
    print(move_list)
    print()
    print('Your pieces:')
    for i in range(0, len(player_pieces)):
        print(f'{i+1}:{player_pieces[i]}')
    print()
    check_status()

interface()
make_a_move()