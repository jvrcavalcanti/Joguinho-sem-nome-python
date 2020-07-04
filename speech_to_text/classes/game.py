class Screen(object):
    def __init__(self, pg):
        self.pg = pg
        self.width = 500
        self.height = 500
        self.spriters = []
        self.screen = self.pg.display.set_mode((self.width, self.height))
        self.color = (181, 181, 181)

    def update(self):
        self.pg.display.flip()
        self.screen.fill(self.color)
        for i in self.spriters:
            i.draw(self.pg, self.screen)