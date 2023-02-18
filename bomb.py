
class Bomb():

    def __init__(self , x , y, marker, range_ex):
        self.x_plant = x
        self.y_plant = y
        self.timer = 100
        self.range_ex = range_ex
        self.sectors = []
        self.marker = marker


    def explode(self , map):
        #self.sectors.append([self.x_plant, self.y_plant])
        for x in range(0, self.range_ex):
            if map[self.x_plant + x][ self.y_plant] == 1:
                break
            elif map[self.x_plant+x][ self.y_plant] == 0 or map[self.x_plant+x][ self.y_plant] == 3 or map[self.x_plant+x][ self.y_plant] == 4:
                self.sectors.append([self.x_plant+x,  self.y_plant])
            elif map[self.x_plant+x][ self.y_plant] == 2 or map[self.x_plant+x][self.y_plant] == 5 or map[self.x_plant+x][ self.y_plant] == 6:
                self.sectors.append([self.x_plant+x,  self.y_plant])
                break
        for x in range(0, self.range_ex):
            if map[self.x_plant - x][ self.y_plant] == 1:
                break
            elif map[self.x_plant-x][ self.y_plant] == 0 or map[self.x_plant-x][ self.y_plant] == 3 or map[self.x_plant-x][ self.y_plant] == 4:
                self.sectors.append([self.x_plant-x,  self.y_plant])
            elif map[self.x_plant-x][ self.y_plant] == 2 or map[self.x_plant-x][self.y_plant] == 5 or map[self.x_plant-x][ self.y_plant] == 6:
                self.sectors.append([self.x_plant-x,  self.y_plant])
                break
        for y in range(0, self.range_ex):
            if map[self.x_plant][ self.y_plant + y] == 1:
                break
            elif map[self.x_plant][ self.y_plant + y] == 0 or map[self.x_plant][ self.y_plant + y] == 3 or map[self.x_plant][ self.y_plant + y] == 4:
                self.sectors.append([self.x_plant,  self.y_plant + y])
            elif map[self.x_plant][ self.y_plant + y] == 2 or map[self.x_plant][self.y_plant+y] == 5 or map[self.x_plant][ self.y_plant+y] == 6:
                self.sectors.append([self.x_plant,  self.y_plant + y])
                break
        for y in range(0, self.range_ex):
            if map[self.x_plant][ self.y_plant - y] == 1:
                break
            elif map[self.x_plant][ self.y_plant - y] == 0 or map[self.x_plant][ self.y_plant - y] == 3 or map[self.x_plant][ self.y_plant - y] == 4:
                self.sectors.append([self.x_plant,  self.y_plant - y])
            elif map[self.x_plant][ self.y_plant - y] == 2 or map[self.x_plant][self.y_plant-y] == 5 or map[self.x_plant][ self.y_plant-y] == 6:
                self.sectors.append([self.x_plant,  self.y_plant - y])
                break

    def update(self):
        self.timer -= 1

    #def get_coord(self):
    #    coord = [self.x_plant,self.y_plant]
    #   return coord

    def get_sectors(self):
        return self.sectors

    def get_marker(self):
        return self.marker

