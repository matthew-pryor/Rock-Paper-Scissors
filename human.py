from mimetypes import init
from player import Player


class Human(Player):
    
    def __init__(self): #dont forget superinit
        
        super().__init__()

    def set_name(self):

            self.name = input("Welcome to the game. What is your name?  \n")