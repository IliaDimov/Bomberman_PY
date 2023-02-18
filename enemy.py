import random

class Enemy():
    def __init__(self, x , y, spot):
        self.x = x
        self.y = y
        self.spot = spot
        self.alive = True
        self.direction = random.randint(1,4)
        self.counter = 0

    def move(self, map, player, player2):

        make_move = False

        while(make_move == False):
            #direction = random.randint(1,4)

            check_Space = False

            if(player.x == self.x and player.alive):
                if self.y > player.y:
                    for y in range(player.y,self.y):
                        if(map[self.x][y] != 0 and map[self.x][y] != 3):
                            check_Space = True 
                    if check_Space == False:
                        map[self.x][self.y - 1] = self.spot
                        map[self.x][self.y] = 0
                        self.y -= 1
                        make_move = True
                    else:
                        check_Space = False
                elif self.y < player.y:
                    for y in range(self.y+1,player.y):
                        if(map[self.x][y] != 0 and map[self.x][y] != 3):
                            check_Space = True 
                    if check_Space == False:
                        map[self.x][self.y + 1] = self.spot
                        map[self.x][self.y] = 0
                        self.y += 1
                        make_move = True
                    else:
                        check_Space = False
            if(player2.x == self.x and player2.alive):
                if self.y > player2.y:
                    for y in range(player2.y,self.y):
                        if(map[self.x][y] != 0 and map[self.x][y] != 4):
                            check_Space = True 
                    if check_Space == False:
                        map[self.x][self.y - 1] = self.spot
                        map[self.x][self.y] = 0
                        self.y -= 1
                        make_move = True
                    else:
                        check_Space = False
                elif self.y < player2.y:
                    for y in range(self.y+1,player2.y):
                        if(map[self.x][y] != 0 and map[self.x][y] != 4):
                            check_Space = True 
                    if check_Space == False:
                        map[self.x][self.y + 1] = self.spot
                        map[self.x][self.y] = 0
                        self.y += 1
                        make_move = True
                    else:
                        check_Space = False
            if(player.y == self.y and player.alive):
                if self.x > player.x:
                    for x in range(player.x,self.x):
                        if(map[x][self.y] != 0 and map[x][self.y] != 3):
                            check_Space = True 
                    if check_Space == False:
                        map[self.x - 1][self.y] = self.spot
                        map[self.x][self.y] = 0
                        self.x -= 1
                        make_move = True
                    else:
                        check_Space = False
                elif self.x < player.x:
                    for x in range(self.x+1,player.x):
                        if(map[x][self.y] != 0 and map[x][self.y] != 3):
                            check_Space = True 
                    if check_Space == False:
                        map[self.x + 1][self.y] = self.spot
                        map[self.x][self.y] = 0
                        self.x += 1
                        make_move = True
                    else:
                        check_Space = False
            if(player2.y == self.y and player2.alive):
                if self.x > player2.x:
                    for x in range(player2.x,self.x):
                        if(map[x][self.y] != 0 and map[x][self.y] != 4):
                            check_Space = True 
                    if check_Space == False:
                        map[self.x - 1][self.y] = self.spot
                        map[self.x][self.y] = 0
                        self.x -= 1
                        make_move = True
                    else:
                        check_Space = False
                elif self.x < player2.x:
                    for x in range(self.x+1,player2.x):
                        if(map[x][self.y] != 0 and map[x][self.y] != 4):
                            check_Space = True 
                    if check_Space == False:
                        map[self.x + 1][self.y] = self.spot
                        map[self.x][self.y] = 0
                        self.x += 1
                        make_move = True
                    else:
                        check_Space = False
            if(make_move == False):

                if self.direction == 1 :
                    if(map[self.x - 1 ][self.y] == 0 or map[self.x - 1 ][self.y] == 3 or map[self.x - 1 ][self.y] == 4):
                        map[self.x - 1][self.y] = self.spot
                        map[self.x][self.y] = 0
                        self.x -= 1
                        make_move = True
                        self.counter += 1
                        if self.counter > 2:
                            self.direction = random.randint(1,4)
                            self.counter = 0
                    else:
                        self.direction = random.randint(1,4)
                        self.counter = 0
                        #self.y += y_to
                elif self.direction == 2:
                    if(map[self.x + 1 ][self.y] == 0 or map[self.x + 1 ][self.y] == 3 or map[self.x + 1 ][self.y] == 4):
                        map[self.x + 1][self.y] = self.spot
                        map[self.x][self.y] = 0
                        make_move = True
                        self.x += 1
                        self.counter += 1
                        if self.counter > 2:
                            self.direction = random.randint(1,4)
                            self.counter = 0
                    else:
                        self.direction = random.randint(1,4)
                        self.counter = 0    
                elif self.direction == 3:
                    if(map[self.x][self.y + 1] == 0 or map[self.x][self.y + 1] == 3 or map[self.x][self.y + 1] == 4):
                        map[self.x][self.y + 1] = self.spot
                        map[self.x][self.y] = 0
                        self.y += 1
                        make_move = True
                        self.counter += 1
                        if self.counter > 2:
                            self.direction = random.randint(1,4)
                            self.counter = 0
                    else:
                        self.direction = random.randint(1,4)
                        self.counter = 0
                elif self.direction == 4:
                    if(map[self.x][self.y - 1] == 0 or map[self.x][self.y - 1] == 3 or map[self.x][self.y - 1] == 4):
                        map[self.x][self.y - 1] = self.spot
                        map[self.x][self.y] = 0
                        self.y -= 1
                        make_move = True
                        self.counter += 1
                        if self.counter > 2:
                            self.direction = random.randint(1,4)
                            self.counter = 0
                    else:
                        self.direction = random.randint(1,4)
                        self.counter = 0
