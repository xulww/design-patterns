from Circle import Circle
from Square import Square
from Triangle import Triangle


class ShapeFacade:
    _circle = None
    _square = None
    _triangle = None

    def __init__(self):
        self._circle = Circle()
        self._square = Square()
        self._triangle = Triangle()

    # let's say the task is to create an easy interface to draw shapes

    def drawCircle(self):
        # TODO drawing circle complexity goes here
        # step 1 (ex. get pen)
        # step 2 (ex. go to whiteboard)
        # step 3 (ex. touch the whiteboard with the pen)
        # ...

        self._circle.draw()

    def drawSquare(self):
        # TODO drawing square complexity goes here
        # step 1
        # step 2
        # step 3
        # ...

        self._square.draw()

    def drawTriangle(self):
        # TODO drawing triangle complexity goes here
        # step 1
        # step 2
        # step 3
        # ...

        self._triangle.draw()
