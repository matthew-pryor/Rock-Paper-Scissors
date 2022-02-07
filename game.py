from human import Human
from ai import Ai


class Game:
    
    def __init__(self) -> None:
        pass

    def introduction(self): #displays rules and asks the user if they want to play single player or multiplayer. void

        self.player_1 = Human()

        player_1_input_valid = False

        while player_1_input_valid is False:

            player_1_input = input('Would you like to play against an opponent or by yourself: Press [1] to play with a friend or press [2] play against the CPU. ')

            if(player_1_input == '1'):

                self.player_2 = Human()
                player_1_input_valid = True

            elif(player_1_input == '2'):

                self.player_2 = Ai()
                player_1_input_valid = True

            else:
                
                print('Invalid response, please try again.')
                player_1_input_valid = False



    def run_game(self): #runs all functions. void
        pass

    def round(self): #keeps track of wins - while loop until wins for either player == 2. void

        while self.player_1.wins < 2 or self.player_2 < 2:
        
            self.player_1.choose_gesture()
        
            self.player_2.choose_gesture()

    def display_winner(self): #once two wins are achieved by either player, this is displayed. void, funtion complete.
        pass