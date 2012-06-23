import pyglet

class ProcinctuWindow(pyglet.window.Window):
    def __init__(self):
        pyglet.window.Window.__init__(self, width = 315, height = 220) 
        self.batch_draw = pyglet.graphics.Batch()
        self.background = pyglet.resource.image("battlebackground.png")
        self.image_assassin_standing = pyglet.resource.image("assassin1.png")
        self.sprite_assassin = pyglet.sprite.Sprite(self.image_assassin_standing, x = 50, y = 30, batch = self.batch_draw) 
        self.fps_display = pyglet.clock.ClockDisplay()

    def update(self, interval):
        # Move 10 pixels per second
        self.sprite_assassin.x += interval * 10

    def on_draw(self):
        self.background.blit(0, 0)
        self.fps_display.draw()
        self.batch_draw.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.A:
            print "The 'A' key was pressed"
        if symbol == pyglet.window.key.RIGHT:
            print "The 'RIGHT' key was pressed"
            pyglet.clock.schedule_interval(func = self.update, interval = 1/60.)
        if symbol == pyglet.window.key.LEFT:
            print "The 'LEFT' key was pressed"

if __name__ == "__main__":
    window = ProcinctuWindow()
    pyglet.app.run()
