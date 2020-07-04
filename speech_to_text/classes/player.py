class Player(object):
    def __init__(self):
        self.x = 250
        self.y = 250
        self.width = 25
        self.height = 25
        self.color = (219, 198, 7)
        self.velocity = 5

    def draw(self, pg, screen):
        pg.draw.rect(screen, self.color, pg.Rect(self.x, self.y, self.width, self.height))
    
    def move_up(self, game):
        if self.y > 0:
            self.y -= self.velocity

    def move_down(self, game):
        if self.y < game.height - 25:
            self.y += self.velocity

    def move_left(self, game):
        if self.x > 0:
            self.x -= self.velocity

    def move_right(self, game):
        if self.x < game.width - 25:
            self.x += self.velocity