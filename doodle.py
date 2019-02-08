import pyglet, random

game_window = pyglet.window.Window(800, 600)

batch = pyglet.graphics.Batch()

left_wall = batch.add(2, pyglet.gl.GL_LINES, None,
    ('v2i', (200, 0, 200, 600)),
    ('c3B', (0, 0, 255, 0, 255, 0))
)
right_wall = batch.add(2, pyglet.gl.GL_LINES, None,
    ('v2i', (600, 0, 600, 600)),
    ('c3B', (0, 60, 222, 0, 185, 64))
)
bottom_wall = batch.add(2, pyglet.gl.GL_LINES, None, 
    ('v2i', (200, 1, 600, 1)),
    ('c3B', (0, 60, 222, 0, 185, 64))
)


@game_window.event
def on_draw():
    game_window.clear()
    batch.draw()

if __name__ == '__main__':
    pyglet.app.run()