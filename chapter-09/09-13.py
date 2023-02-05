from random import randint


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


dice = Dice()
for i in range(0, 10):
    dice.roll_die()

dice = Dice(10)
for i in range(0, 10):
    dice.roll_die()

dice = Dice(20)
for i in range(0, 10):
    dice.roll_die()
