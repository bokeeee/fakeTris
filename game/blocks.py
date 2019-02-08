import pyglet, math
from pyglet.window import key
from game import physicalobject, resources

class Block(physicalobject.PhysicalObject):
    """A block that responds to user input."""

    def __init__(self, *args, **kwargs):
        super(Block, self).__init__(img=resources.blue_block, *args, **kwargs)

        # Some constants
        self.key_handler = key.KeyStateHandler()

    def update(self, dt):
        # Physics
        super(Block, self).update(dt)

        if self.key_handler[key.LEFT]:
            self.velocity_x -= 1.0   
        if self.key_handler[key.RIGHT]:
            self.velocity_x += 1.0 
        
        if self.key_handler[key.DOWN]:
            self.velocity_y += -1        
        