import random
from colorama import init, Fore, Style
init(autoreset=True)

def display_screen(bd):

    
    def colored(cell):
        if cell == 'X':
            return Fore.MAGENTA + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.RED + cell + Style.RESET_ALL
        else:
            return Fore.GREEN + cell + Style.RESET_ALL
    print(' ' + colored(bd[0]) + ' | ' + colored(bd[1]) + ' | ' + colored(bd[2]))
    print(Fore.MAGENTA + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(bd[3]) + ' | ' + colored(bd[4]) + ' | ' + colored(bd[5]))
    print(Fore.MAGENTA + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(bd[6]) + ' | ' + colored(bd[7]) + ' | ' + colored(bd[8]))
    print()

def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Hey ! Do you want to be X or O? " + Style.RESET_ALL).upper()
    if symbol == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def player_move(bd, symbol):
    move = -1
    while move not in range(1, 10) or not bd[move - 1].isdigit():
        try:
            move = int(input("Please Enter your move between 1-9): "))
            if move not in range(1, 10) or not bd[move - 1].isdigit():
                print("This is an invalid move. Please try again")
        except ValueError:
            print("Kindly select a number between 1 and 9.")
    bd[move - 1] = symbol

def ai_move(bd, ai_symbol, player_symbol):
    for i in range(9):
        if bd[i].isdigit():
            board_copy = bd.copy()
            board_copy[i] = ai_symbol
            if check_win(board_copy, ai_symbol):
                bd[i] = ai_symbol
                return
    for i in range(9):
        if bd[i].isdigit():
            bd_copy = bd.copy()
            bd_copy[i] = player_symbol
            if check_win(bd_copy, player_symbol):
                bd[i] = ai_symbol
                return
    possible_moves = [i for i in range(9) if bd[i].isdigit()]
    move = random.choice(possible_moves)
    bd[move] = ai_symbol

def check_win(bd, symbol):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
        (0, 4, 8), (2, 4, 6)
    ]
    for cond in win_conditions:
        if bd[cond[0]] == bd[cond[1]] == bd[cond[2]] == symbol:
            return True
    return False

def check_full(bd):
    return all(not spot.isdigit() for spot in bd)

def ttt():
    print("Welcome to Tic-Tac-Toe!")
    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)
    while True:
        bd = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        player_symbol, ai_symbol = player_choice()
        turn = 'Player'
        game_on = True

        while game_on:
            display_screen(bd)
            if turn == 'Player':
                player_move(bd, player_symbol)
                if check_win(bd, player_symbol):
                    display_screen(bd)
                    print("Congratulations! " + player_name + ", you have won the game!")
                    game_on = False
                else:
                    if check_full(bd):
                        display_screen(bd)
                        print("It's a tie!")
                        break
                    else:
                        turn = 'AI'
            else:
                ai_move(bd, ai_symbol, player_symbol)
                if check_win(bd, ai_symbol):
                    display_screen(bd)
                    print("AI has won the game!")
                    game_on = False
                else:
                    if check_full(bd):
                        display_screen(bd)
                        print("It's a tie!")
                        break
                    else:
                        turn = 'Player'
        play_again = input("Do you want to play this again ? please answer yes or no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Have a Great Dayyyy")
            break

if __name__ == "__main__":
    ttt()
