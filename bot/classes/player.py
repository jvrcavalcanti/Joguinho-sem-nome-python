from function import d_two_points
import csv

class Player(object):
    def __init__(self):
        self.x = 250
        self.y = 250
        self.width = 25
        self.height = 25
        self.color = (219, 198, 7)
        self.velocity = 10
        self.writer = csv.writer(open('data.csv', 'w', newline=''), delimiter=',')
        self.writer.writerow(['x_player', 'x_fruit', 'y_player', 'y_fruit', 'id_move'])

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

    def next_move(self, fruit, game):
        d = [
            # up
            d_two_points(self.x, fruit.x, self.y - self.velocity, fruit.y),
            # down
            d_two_points(self.x, fruit.x, self.y + self.velocity, fruit.y),
            #right
            d_two_points(self.x + self.velocity, fruit.x, self.y, fruit.y),
            # left
            d_two_points(self.x - self.velocity, fruit.x, self.y, fruit.y)
        ]
        menor = 1000000
        id = -1
        for i in range(len(d)):
            if d[i] < menor:
                menor = d[i]
                id = i
        data = [self.x, fruit.x, self.y, fruit.y, id]
        self.writer.writerow(data)
        if id == 0:
            self.move_up(game)
        elif id == 1:
            self.move_down(game)
        elif id == 2:
            self.move_right(game)
        else:
            self.move_left(game)