from human import Human
from ai import Ai

class Game:
    
    def __init__(self) -> None:
        
        self.player_1 = Human()

    def introduction(self): #displays rules and asks the user if they want to play single player or multiplayer. void

        player_1_input_valid = False

        self.player_1.set_name()

        print(f'Welcome to the game {self.player_1.name}')

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
        
        self.introduction()

        self.winner = False

        while self.winner is False:
        
            self.round()

            if ((self.player_1.wins == 2) or (self.player_2.wins == 2)):
                
                self.winner = True

            else:

                self.winner = False

        self.display_winner()

    def round(self): #keeps track of wins - while loop until wins for either player == 2. void self.player_1.wins < 2 or self.player_2.wins < 2:
        
        self.player_1.choose_gesture()
        
        self.player_2.choose_gesture()

        self.compare_gestures()

    def compare_gestures(self):

        if (self.player_1.chosen_gesture == 'Rock' and self.player_2.chosen_gesture == 'Scissors'):               #Rock curshes scissors
            print(f'Rock crushes scissors! {self.player_1.name} wins!')
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Rock' and self.player_1.chosen_gesture == 'Scissors'):
            
            self.player_2.wins += 1

        elif (self.player_1.chosen_gesture == 'Rock' and self.player_2.chosen_gesture == 'Lizard'):               #Rock crushes lizard
            print(f'Rock crushes Lizard! {self.player_1.name} wins!')
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Rock' and self.player_1.chosen_gesture == 'Lizard'):

            self.player_2.wins += 1  

        elif (self.player_1.chosen_gesture == 'Scissors' and self.player_2.chosen_gesture == 'Paper'):      
            print(f'Scissors cuts paper! {self.player_1.name} wins!')    
            
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Scissors' and self.player_1.chosen_gesture == 'Paper'):
            
            self.player_2.wins += 1

        elif (self.player_1.chosen_gesture == 'Scissors' and self.player_2.chosen_gesture == 'Lizard'):               #scissors decapitates lizard
            
            print(f'Scissors crushes Lizard! {self.player_1.name} wins!')
            
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Scissors' and self.player_1.chosen_gesture == 'Lizard'):

            self.player_2.wins += 1

        elif (self.player_1.chosen_gesture == 'Paper' and self.player_2.chosen_gesture == 'Rock'):               #paper covers rock
            print(f'Paper suffocates Rock! {self.player_1.name} wins!')
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Paper' and self.player_1.chosen_gesture == 'Rock'):
            
            self.player_2.wins += 1

        elif (self.player_1.chosen_gesture == 'Paper' and self.player_2.chosen_gesture == 'Spock'):               #paper disproves spock
            print(f'Paper overwhelms Spock! {self.player_1.name} wins!')
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Paper' and self.player_1.chosen_gesture == 'Spock'):

            self.player_2.wins += 1

        elif (self.player_1.chosen_gesture == 'Lizard' and self.player_2.chosen_gesture == 'Spock'):               #lizard poisons spock
            print(f'Lizard licks Spock to death! {self.player_1.name} wins!')
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Lizard' and self.player_1.chosen_gesture == 'Spock'):

            self.player_2.wins += 1

        elif (self.player_1.chosen_gesture == 'Lizard' and self.player_2.chosen_gesture == 'Paper'):               #lizard eats paper
            print(f'Lizard licks paper into a drooly mess! {self.player_1.name} wins!')
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Lizard' and self.player_1.chosen_gesture == 'Paper'):

            self.player_2.wins += 1

        elif (self.player_1.chosen_gesture == 'Spock' and self.player_2.chosen_gesture == 'Scissors'):               #spock smashes scissors
            print(f'Spock dismantles scissors! {self.player_1.name} wins!')
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Spock' and self.player_1.chosen_gesture == 'Scissors'):

            self.player_2.wins += 1

        elif (self.player_1.chosen_gesture == 'Spock' and self.player_2.chosen_gesture == 'Rock'):               #spock vaporizes rock
            print(f'Spock phasers Rock into dust! {self.player_1.name} wins!')
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Spock' and self.player_1.chosen_gesture == 'Rock'):

            self.player_2.wins += 1

        elif (self.player_2.chosen_gesture == self.player_1.chosen_gesture):
            print("It's a tie, no one wins.")
            self.player_2.wins += 0

    def display_winner(self): #once two wins are achieved by either player, this is displayed. void, funtion complete.
        
        if (self.player_1.wins == 2):
            print(f"{self.player_1.name} has won the game!")
        elif (self.player_2.wins):
            print(f"{self.player_2.name} has won the game!")
        elif (self.ai.wins == 2):
            print ("The AI has become self-aware and won the game!")

        