import pyglet
from game import resources, blocks

# Set up a window
game_window = pyglet.window.Window(800,600)

# Create a collection of vertex lists for batched rendering
main_batch = pyglet.graphics.Batch()

# Initialize a block
blue = blocks.Block(x=400, y=600, batch=main_batch)

# Create game object array
game_objects = [blue]

# Input handler
game_window.push_handlers(blue.key_handler)

# Create walls
left_wall = main_batch.add(2, pyglet.gl.GL_LINES, None,
    ('v2i', (200, 0, 200, 600)),
    ('c3B', (0, 0, 255, 0, 255, 0))
)
right_wall = main_batch.add(2, pyglet.gl.GL_LINES, None,
    ('v2i', (600, 0, 600, 600)),
    ('c3B', (0, 60, 222, 0, 185, 64))
)
bottom_wall = main_batch.add(2, pyglet.gl.GL_LINES, None, 
    ('v2i', (200, 1, 600, 1)),
    ('c3B', (0, 60, 222, 0, 185, 64))
)

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

def update(dt):
    for obj in game_objects:
        obj.update(dt)
    
    
    

if __name__ == '__main__':
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1 / 120)

    pyglet.app.run()