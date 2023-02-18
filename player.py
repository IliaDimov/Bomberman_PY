
from bomb import Bomb

class Player:
    #bomb_limit = 1
    #range_limit = 3
    #x = 1
    #y = 1

    def __init__(self, spot, x_from, y_from, marker):
        self.alive = True
        self.spot = spot
        self.x = x_from
        self.y = y_from
        self.marker = marker
        self.bomb_limit = 1
        self.range_limit = 3
    
    def move(self, x_to, y_to, map):
        if(map[self.x + x_to][self.y + y_to] == 0 and map[self.x][self.y] == self.spot):
            map[self.x + x_to][self.y + y_to] = self.spot
            map[self.x][self.y] = 0
            self.x += x_to
            self.y += y_to
        elif(map[self.x + x_to][self.y + y_to] == 7 and map[self.x][self.y] == self.spot):
            map[self.x + x_to][self.y + y_to] = self.spot
            map[self.x][self.y] = 0
            self.x += x_to
            self.y += y_to
            self.range_limit+=1
        elif(map[self.x + x_to][self.y + y_to] == 8 and map[self.x][self.y] == self.spot):
            map[self.x + x_to][self.y + y_to] = self.spot
            map[self.x][self.y] = 0
            self.x += x_to
            self.y += y_to
            self.bomb_limit+=1
    
    def plant_bomb(self):
        bomb = Bomb(self.x, self.y, self.marker, self.range_limit)
        return bomb

        