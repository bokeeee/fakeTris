import pyglet

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

# Tell pyglet where to find the resources
pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

blue_block = pyglet.resource.image("blue.png")
center_image(blue_block)

orange_block = pyglet.resource.image("orange.png")
center_image(orange_block)

pink_block = pyglet.resource.image("pink.png")
center_image(pink_block)