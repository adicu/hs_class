import sys
import pantograph
import random

class BouncingBallHandler(pantograph.PantographHandler):
    def setup(self):
        # This method is run once when the animation starts 
        # Put any code which sets up the animation here

    def update(self):
        # This method is called repeatedly at a fixed interval
        # Here, you should update the bouncing ball's postion and redraw it


if __name__ == '__main__':
    app = pantograph.PantographApplication([
        ("Pantograph", "/", BouncingBallHandler)
    ])
    app.run()
