


class Player:

    def __init__(self, name):
        
        self.wins = 0
        self.name = name
        self.list_of_gestures = []
        self.chosen_gesture = ''

    def choose_gesture(self): #selects from the list and is overriden each turn to give each player/ai their independent selection.
        pass