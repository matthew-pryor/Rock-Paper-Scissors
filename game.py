from human import Human
from ai import Ai

class Game:
    
    def __init__(self) -> None:
        
        self.player_1 = Human()

    def introduction(self): #displays rules and asks the user if they want to play single player or multiplayer. void

        player_1_input_valid = False

        self.player_1.set_name()

        print(f'Welcome to the game {self.player_1.name}\n')

        print("Before you play you'll have to know the rules! This isn't your ma and pa's rock, paper, scissors!\n")

        print("HERE ARE THE RULES!\n")
        print("****************************")

        list_of_rules = ['--Rock crushes Scissors & smashes Lizard', '--Scissors cuts Paper & decapitates Lizard', '--Paper covers Rock & disproves Spock', '--Lizard poisons Spock & eats Paper', '--Spock smashes Scissors & vaporizes Rock\n']

        for rule in list_of_rules:

            print(rule)

        while player_1_input_valid is False:

            player_1_input = input('Would you like to play against an opponent or the AI?: Press [1] to play with a friend or [2] to face the CPU. \n')
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


    def run_game(self): #runs all functions. void
        
        self.introduction()

        self.winner = False

        while self.winner is False:
        
            self.round()

            if ((self.player_1.wins == 2) or (self.player_2.wins == 2)):
                
                self.winner = True
            
            else:

                self.winner = False
                print(f"{self.player_1.name} has {self.player_1.wins} wins and {self.player_2.name} has {self.player_2.wins} wins.\n")

        self.display_winner()

    def round(self): #keeps track of wins - while loop until wins for either player == 2. void self.player_1.wins < 2 or self.player_2.wins < 2:
        
        self.player_1.choose_gesture()
        
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
        
        if (self.player_1.wins == 2):

            print(f"{self.player_1.name} has won the game!\n")

        elif (self.player_2.wins):

            print(f"{self.player_2.name} has won the game!\n")

        # elif (self..wins == 2):
            # print ("The AI has become self-aware and won the game!\n")

        