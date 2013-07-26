import sys
import pantograph
import random

# You'll probably want to change the name
class FinalProject(pantograph.PantographHandler):
    def setup(self):
        pass

    def update(self):
        pass


if __name__ == '__main__':
    app = pantograph.SimplePantographApplication(FinalProject)
    app.run()
