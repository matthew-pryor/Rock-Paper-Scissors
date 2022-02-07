from human import Human
from ai import Ai


class Game:
    
    def __init__(self) -> None:
        pass

    def introduction(self): #displays rules and asks the user if they want to play single player or multiplayer. void

        player_1 = Human()

        player_1_input_valid = False

        while player_1_input_valid is False:

            player_1_input = input('Would you like to play against an opponent or by yourself: Press [1] to play with a friend or press [2] play against the CPU. ')

            if(player_1_input == '1'):

                player_2 = Human()
                player_1_input_valid = True

            elif(player_1_input == '2'):

                player_2 = Ai()
                player_1_input_valid = True

            else:
                
                print('Invalid response, please try again.')
                player_1_input_valid = False



    def run_game(self): #runs all functions. void
        pass

    def round(self): #keeps track of wins - while loop until wins for either player == 2. void
        pass

    def player_1(self): #picks from the list of options void
        pass

    def player_2(self): #picks from the list. If they choose singleplayer in the welcome, then AI overrides and just picks randomly from the list of options. void
        pass

    def display_winner(self): #once two wins are achieved by either player, this is displayed. void, funtion complete.
        pass