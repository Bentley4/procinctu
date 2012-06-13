import pyglet

background = pyglet.resource.image('battlebackground.png')

image_assassin_standing = pyglet.resource.image('assassin1.png')
sprite_assassin = pyglet.sprite.Sprite(image_assassin_standing, x = 50, y = 30) 

window = pyglet.window.Window(width=315, height=220)

def update(interval):
    # Move 10 pixels per second
    sprite_assassin.x += interval * 10

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.A:
        print 'The \'A\' key was pressed'
    if symbol == pyglet.window.key.RIGHT:
        print 'The \'RIGHT\' key was pressed'
        pyglet.clock.schedule_interval(func = update, interval = 1/60.)
    if symbol == pyglet.window.key.LEFT:
        print 'The \'LEFT\' key was pressed'

@window.event
def on_draw(): 
    background.blit(0, 0)
    sprite_assassin.draw()

fps_display = pyglet.clock.ClockDisplay()
fps_display.draw()

pyglet.app.run()
