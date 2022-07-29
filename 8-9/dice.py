from random import randint

class Dice():

    def __init__(self,sides):
        self.sides = sides

    def roll_dice(self):
        if self.sides == 6:
            self.sides = randint(1, 6)
        elif self.sides == 10:
            self.sides = randint(1,10)
        elif self.sides == 12:
            self.sides = randint(1,12)

        print(self.sides)



dc = Dice(12)

dc.roll_dice()
