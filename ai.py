from player import Player
import random

class Ai(Player):

    def __init__(self) -> None: #dont forget superinit
        
        super().__init__()
        
        self.name = "WALL-E"

    def choose_gesture(self): #selects from the list and is overriden each turn to give each player/ai their independent selection.

        chosen_gesture_index = random.randint(0, len(self.list_of_gestures)-1)

        self.chosen_gesture = self.list_of_gestures[chosen_gesture_index]

        return self.chosen_gesture