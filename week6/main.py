import sys
import pantograph
import random

class BouncingBall(pantograph.PantographHandler):
    def setup(self):
        self.x = random.randint(0, self.width)
        self.y = random.randint(0, self.height)
        self.xvel = random.randint(1, 5)
        self.yvel = random.randint(1, 5)

    def update(self):
        if self.x < 0 or self.x > self.width:
            self.xvel *= -1
        if self.y < 0 or self.y > self.height:
            self.yvel *= -1

        self.x += self.xvel
        self.y += self.yvel

        self.clear_rect(0, 0, self.width, self.height)
        self.fill_circle(self.x, self.y, 10, "red")


if __name__ == '__main__':
    app = pantograph.SimplePantographApplication(BouncingBall)
    app.run()
