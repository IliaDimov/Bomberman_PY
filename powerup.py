import random

class Bonus():
    def __init__(self):
        self.bomb_range = 7
        self.bomb_number = 8

    def get_bonus(self):
        a = random.randint(1,2)
        if a == 1:
            return self.bomb_range
        else:
            return self.bomb_number