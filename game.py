from human import Human
from ai import Ai

# Add how many rounds the players want to play.

class Game:
    
    def __init__(self) -> None:
        
        self.player_1 = Human()

        self.desired_rounds = 2

    def introduction(self): #displays rules and asks the user if they want to play single player or multiplayer. void

        player_1_input_valid = False

        self.player_1.set_name()

        print(f'Welcome to the game {self.player_1.name}\n')

        print("Before you play you'll have to know the rules! This isn't your ma and pa's rock, paper, scissors!\n")

        print("HERE ARE THE RULES!\n")
        print("************************************************************************************")

        list_of_rules = ['--Rock crushes Scissors & smashes Lizard', '--Scissors cuts Paper & decapitates Lizard', '--Paper covers Rock & disproves Spock', '--Lizard poisons Spock & eats Paper', '--Spock smashes Scissors & vaporizes Rock\n']

        for rule in list_of_rules:

            print(rule)

        print("************************************************************************************")

        while player_1_input_valid is False:

            player_1_input = input('Would you like to play against an opponent or the AI?: Press [1] to play with a friend or [2] to face the CPU. ')
            print("")

            if(player_1_input == '1'):
                self.player_2 = Human()
                self.player_2.name = input("What is the 2nd player's name? ")
                print("")
                print(f"Welcome to the game, {self.player_2.name}\n")
                player_1_input_valid = True

            elif(player_1_input == '2'):

                self.player_2 = Ai()
                player_1_input_valid = True

            else:
                
                print('Invalid response, please try again.')
                player_1_input_valid = False

        is_digit = False

        while is_digit is False:

            self.desired_rounds_input = (input('How many rounds do you want to win the game? '))
            
            if self.desired_rounds_input.isnumeric() == True:

                self.desired_rounds = int(self.desired_rounds_input)

                self.maximum_rounds = (self.desired_rounds * 2) - 1

                print(f"Looks like you chose best {self.desired_rounds} out of {self.maximum_rounds}.\n")

                is_digit = True

            else:

                print('Invalid response, please try again.')

                is_digit = False


    def run_game(self): #runs all functions. void
        
        self.introduction()

        self.winner = False

        while self.winner is False:
        
            self.round()

            if ((self.player_1.wins == self.desired_rounds) or (self.player_2.wins == self.desired_rounds)):
                
                self.winner = True
            
            else:

                self.winner = False
                print(f"{self.player_1.name} has {self.player_1.wins} wins and {self.player_2.name} has {self.player_2.wins} wins.\n")

        self.display_winner()

    def round(self): #keeps track of wins - while loop until wins for either player == 2. void self.player_1.wins < 2 or self.player_2.wins < 2:

        print(f"It is now {self.player_1.name}'s turn")
        self.player_1.choose_gesture()
                
        print(f"It is now {self.player_2.name}'s turn")
        self.player_2.choose_gesture()

        self.compare_gestures()

    def compare_gestures(self):

        if (self.player_1.chosen_gesture == 'Rock' and self.player_2.chosen_gesture == 'Scissors'):               
            print(f'{self.player_1.name} chose Rock and {self.player_2.name} chose Scissors\n')
            print(f'Rock crushes scissors! {self.player_1.name} wins!\n')
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Rock' and self.player_1.chosen_gesture == 'Scissors'):
            print(f'{self.player_2.name} chose Rock and {self.player_1.name} chose Scissors\n')
            print(f'Rock crushes scissors! {self.player_2.name} wins!\n')
            self.player_2.wins += 1

        elif (self.player_1.chosen_gesture == 'Rock' and self.player_2.chosen_gesture == 'Lizard'):         
            print(f'{self.player_1.name} chose Rock and {self.player_2.name} chose Lizard\n')            
            print(f'Rock crushes Lizard! {self.player_1.name} wins!\n')
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Rock' and self.player_1.chosen_gesture == 'Lizard'):
            print(f'{self.player_2.name} chose Rock and {self.player_1.name} chose Lizard\n')
            print(f'Rock crushes Lizard! {self.player_2.name} wins!\n')
            self.player_2.wins += 1  

        elif (self.player_1.chosen_gesture == 'Scissors' and self.player_2.chosen_gesture == 'Paper'):      
            print(f'{self.player_1.name} chose Scissors and {self.player_2.name} chose Paper\n')
            print(f'Scissors cuts paper! {self.player_1.name} wins!\n')    
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Scissors' and self.player_1.chosen_gesture == 'Paper'):
            print(f'{self.player_2.name} chose Scissors and {self.player_1.name} chose Paper\n')
            print(f'Scissors cuts paper! {self.player_2.name} wins!\n')
            self.player_2.wins += 1

        elif (self.player_1.chosen_gesture == 'Scissors' and self.player_2.chosen_gesture == 'Lizard'):               
            print(f'{self.player_1.name} chose Scissors and {self.player_2.name} chose Lizard\n')
            print(f'Scissors crushes Lizard! {self.player_1.name} wins!\n')
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Scissors' and self.player_1.chosen_gesture == 'Lizard'):
            print(f'{self.player_2.name} chose Scissors and {self.player_1.name} chose Lizard\n')
            print(f'Scissors crushes Lizard! {self.player_2.name} wins!\n')
            self.player_2.wins += 1

        elif (self.player_1.chosen_gesture == 'Paper' and self.player_2.chosen_gesture == 'Rock'):               
            print(f'{self.player_1.name} chose Paper and {self.player_2.name} chose Rock\n')
            print(f'Paper suffocates Rock! {self.player_1.name} wins!\n')
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Paper' and self.player_1.chosen_gesture == 'Rock'):
            print(f'{self.player_2.name} chose Paper and {self.player_1.name} chose Rock\n')
            print(f'Paper suffocates Rock! {self.player_2.name} wins!\n')
            self.player_2.wins += 1

        elif (self.player_1.chosen_gesture == 'Paper' and self.player_2.chosen_gesture == 'Spock'):               
            print(f'{self.player_1.name} chose Paper and {self.player_2.name} chose Spock\n')
            print(f'Paper overwhelms Spock! {self.player_1.name} wins!\n')
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Paper' and self.player_1.chosen_gesture == 'Spock'):
            print(f'{self.player_2.name} chose Paper and {self.player_2.name} chose Spock\n')
            print(f'Paper overwhelms Spock! {self.player_2.name} wins!\n')
            self.player_2.wins += 1

        elif (self.player_1.chosen_gesture == 'Lizard' and self.player_2.chosen_gesture == 'Spock'):               
            print(f'{self.player_1.name} chose Lizard and {self.player_2.name} chose Spock\n')
            print(f'Lizard licks Spock to death! {self.player_1.name} wins!\n')
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Lizard' and self.player_1.chosen_gesture == 'Spock'):
            print(f'{self.player_2.name} chose Lizard and {self.player_1.name} chose Spock\n')
            print(f'Lizard licks Spock to death! {self.player_2.name} wins!\n')
            self.player_2.wins += 1

        elif (self.player_1.chosen_gesture == 'Lizard' and self.player_2.chosen_gesture == 'Paper'):               
            print(f'{self.player_1.name} chose Lizard and {self.player_2.name} chose Paper\n')
            print(f'Lizard licks paper into a drooly mess! {self.player_1.name} wins!\n')
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Lizard' and self.player_1.chosen_gesture == 'Paper'):
            print(f'{self.player_2.name} chose Lizard and {self.player_1.name} chose Paper\n')
            print(f'Lizard licks paper into a drooly mess! {self.player_2.name} wins!\n')
            self.player_2.wins += 1

        elif (self.player_1.chosen_gesture == 'Spock' and self.player_2.chosen_gesture == 'Scissors'):               
            print(f'{self.player_1.name} chose Spock and {self.player_2.name} chose Scissors\n')
            print(f'Spock dismantles scissors! {self.player_1.name} wins!\n')
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Spock' and self.player_1.chosen_gesture == 'Scissors'):
            print(f'{self.player_2.name} chose Spock and {self.player_1.name} chose Scissors\n')
            print(f'Spock dismantles scissors! {self.player_2.name} wins!\n')
            self.player_2.wins += 1

        elif (self.player_1.chosen_gesture == 'Spock' and self.player_2.chosen_gesture == 'Rock'):               
            print(f'{self.player_1.name} chose Spock and {self.player_2.name} chose Rock\n')
            print(f'Spock phasers Rock into dust! {self.player_1.name} wins!\n')
            self.player_1.wins += 1
        
        elif (self.player_2.chosen_gesture == 'Spock' and self.player_1.chosen_gesture == 'Rock'):
            print(f'{self.player_2.name} chose Spock and {self.player_1.name} chose Rock\n')
            print(f'Spock phasers Rock into dust! {self.player_2.name} wins!\n')
            self.player_2.wins += 1

        elif (self.player_2.chosen_gesture == self.player_1.chosen_gesture):
            print(f'{self.player_2.name} and {self.player_1.name} chose the same thing!')
            print("It's a tie, no one wins. Select again.\n")
            self.player_2.wins += 0

        

    def display_winner(self): #once two wins are achieved by either player, this is displayed. void, funtion complete.

            if (self.player_1.wins == self.desired_rounds):

                print(f"{self.player_1.name} has won the game!\n")

            elif (self.player_2.wins == self.desired_rounds):

                if (self.player_2.name == 'WALL-E'):

                    print("WALL-E had become self-aware and has finally defeated his human overlords!\n")

                else:

                    print(f"{self.player_2.name} has won the game!\n")

            play_again_value = False

            while play_again_value is False:

                play_again = (input("Would you like to play again? Yes or No. "))

                if (play_again == 'Yes' or play_again == 'yes' or play_again == 'y'):

                    play_again_value = True
                    
                    self.player_1.wins = 0

                    self.player_2.wins = 0

                    self.run_game()

                elif (play_again == "No" or play_again == 'no' or play_again == 'n'):

                    play_again = True

                    print("Goodbye!")

                    break

                else:
                
                    print('Invalid response, please try again.')

                    play_again_value = False
                
             
                
                    
                
        