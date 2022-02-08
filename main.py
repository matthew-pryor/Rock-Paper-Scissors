# we want to do a method override. Both child classes should be able to do the thing but in a slightly different way.
# AI or other player. Choose gesture method. child classes need choose gesture. method override in both child classes.
# put everything (options) in a list in the parent class
# validating bad user input is an if/else statement inside of a while loop.
# best of 3 or 3/5 or first to get 2 wins
# if wins = 2 then winner == True
# account for ties (thing == thing)

#Rock curshes scissors
#rock crushes lizard

#Scissors cut paper
#scissors decapitates lizard

#paper covers rock
#paper disproves spock

#lizard poisons spock
#lizard eats paper

#spock smashes scissors
#spock vaporizes rock

#each variable or item in the list wins x2, loses 2x, and only ties with itself.

from game import Game

game = Game()

game.run_game()
