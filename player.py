


class Player:

    def __init__(self, name):
        
        self.wins = 0
        self.name = name
        self.list_of_gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.chosen_gesture = ''

    def choose_gesture(self): #selects from the list and is overriden each turn to give each player/ai their independent selection.

        list_of_gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        
        for gesture in list_of_gestures:

            print(f'Press [{list_of_gestures.index(gesture)}] for {gesture}.')

        chosen_gesture = input('Selection: ')

        integer_chosen_gesture = int(chosen_gesture)

        self.chosen_gesture = self.list_of_gestures[integer_chosen_gesture]

        return self.chosen_gesture