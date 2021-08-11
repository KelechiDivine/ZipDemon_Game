from kivy.properties import (ListProperty, NumericProperty,

 ObjectProperty, StringProperty)

class Game(FloatLayout): # Will contain everything
    # blocks = ListProperty([])
    player = ObjectProperty() # The game's Player instance
    ball = ObjectProperty() # The game's Ball instance

class Player(Widget): # A moving paddle
    position = NumericProperty(0.5)
    direction = StringProperty('none')
 
class Ball(Widget): # A bouncing ball
 # pos_hints are for proportional positioning, see below
    pos_hint_x = NumericProperty(0.5)
    pos_hint_y = NumericProperty(0.3)
    proper_size = NumericProperty(0.)
    velocity = ListProperty([0.1, 0.5])
 
class Block(Widget): # Each coloured block to destroy
    colour = ListProperty([1, 0, 0])


class Player(Widget):
    def __init__(self, **kwargs):
        super(Player, self).__init__(**kwargs)
        with self.canvas:
            Color(1, 0, 0, 1) # r, g, b, a -> red
            Rectangle(pos=self.pos, size=self.size)
 # or without the with syntax, self.canvas.add(...)