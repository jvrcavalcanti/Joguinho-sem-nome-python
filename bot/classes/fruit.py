import numpy as np

class Fruit(object):
    def __init__(self):
        self.x_possibles = [i for i in range(0, 475, 25)]
        self.y_possibles = [i for i in range(0, 475, 25)]
        self.x = self.x_possibles[np.random.randint(0, 19)]
        self.y = self.y_possibles[np.random.randint(0, 19)]
        self.width = 25
        self.height = 25
        self.color = (29, 150, 35)
    
    def draw(self, pg, screen):
        pg.draw.rect(screen, self.color, pg.Rect(self.x, self.y, self.width, self.height))

    def reposition(self):
        self.x = self.x_possibles[np.random.randint(0, 19)]
        self.y = self.y_possibles[np.random.randint(0, 19)]