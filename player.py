


class Player:

    def __init__(self):
        
        self.wins = 0
        self.name = ''
        self.list_of_gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.chosen_gesture = ''

    def choose_gesture(self): #selects from the list and is overriden each turn to give each player/ai their independent selection.

        valid_gesture = False

        while valid_gesture is False:

            list_of_gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
            
            for gesture in list_of_gestures:

                print(f'Press [{list_of_gestures.index(gesture)}] for {gesture}.')

            chosen_gesture = input('Selection: ')

            if (chosen_gesture == '0' or chosen_gesture == '1' or chosen_gesture == '2' or chosen_gesture == '3' or chosen_gesture == '4' or chosen_gesture == '5'):

                valid_gesture = True
                
                integer_chosen_gesture = int(chosen_gesture)

                self.chosen_gesture = self.list_of_gestures[integer_chosen_gesture]

                return self.chosen_gesture

            else:

                valid_gesture = False

                print('Invalid selection, try again.')