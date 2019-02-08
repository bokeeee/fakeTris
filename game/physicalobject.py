import pyglet

class PhysicalObject(pyglet.sprite.Sprite):
    """A sprite with physical properties."""
    
    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        # In addition to position, we have velocity
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.gravity = 0.01

    def update(self, dt):
        """This method is called every frame."""

        # Update position according to velocity and time
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.velocity_y += -self.gravity        