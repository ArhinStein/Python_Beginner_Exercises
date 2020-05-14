from random import randint

class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self, times):
        for x in times:
            x = randint(times)
        print(x)
outcome = Die(6)
outcome.roll_dice(10)