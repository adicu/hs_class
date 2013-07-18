import sys
import pantograph
import random

class BouncingBallHandler(pantograph.PantographHandler):
    def setup(self):
        # This method is run once when the animation starts.
        # Put any initialization code for your animation here.
        # For instance, let's initialize the x and y coordinates of the ball.
        self.x = random.randint(0, self.width)
        self.y = random.randint(0, self.height)

        # The variables self.width and self.height will are already set for you.
        # They are set to the width and height of the canvas.

    def update(self):
        # This method is called repeatedly at a fixed interval.
        # Here, you should update the bouncing ball's postion.

        # The clear_rect method will clear a rectangular area of the screen
        # Let's just clear the entire screen
        self.clear_rect(0, 0, self.width, self.height)
        # Now draw the bouncing ball in position.
        # The arguments to fill_circle are x, y, radius, and color.
        self.fill_circle(self.x, self.y, 10, "red")


if __name__ == '__main__':
    app = pantograph.PantographApplication([
        ("Pantograph", "/", BouncingBallHandler)
    ])
    app.run()
