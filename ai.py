from player import Player
import random

class Ai(Player):

    def __init__(self) -> None: #dont forget superinit
        
        super().__init__()
        
        self.name = "AI"

    # def random_ai_selection(self):
        
    #     self.random_selection = random.choice(self.list_of_gestures)
        
    #     return self.random_selection