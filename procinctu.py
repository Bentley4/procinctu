import pyglet

class Assassin(pyglet.sprite.Sprite):
    def __init__(self, batch):
        pyglet.sprite.Sprite.__init__(self, pyglet.resource.image("assassin1.png"), x = 50)
        self.y = 30

class ProcinctuWindow(pyglet.window.Window):
    def __init__(self):
        pyglet.window.Window.__init__(self, width = 315, height = 220)
        self.batch_draw = pyglet.graphics.Batch()
        self.background = pyglet.resource.image("battlebackground.png")
        self.player = Assassin(batch = self.batch_draw)
        self.fps_display = pyglet.clock.ClockDisplay()
        self.keys_held = []      
 
    def on_draw(self):
        self.background.blit(0, 0)
        self.fps_display.draw()
        self.batch_draw.draw()
        self.player.draw()

    def on_key_press(self, symbol, modifiers):
        self.keys_held.append(symbol)
        if symbol == pyglet.window.key.A:
            print "The 'A' key was pressed"
        if symbol == pyglet.window.key.RIGHT:
            print "The 'RIGHT' key was pressed"
            pyglet.clock.schedule_interval(func = self.update1, interval = 1/60.)
        if symbol == pyglet.window.key.LEFT:
            print "The 'LEFT' key was pressed"
        if symbol == pyglet.window.key.S:
            self.music = pyglet.media.load("Comet.wav", streaming = False)
            self.music.play() 
        if symbol == pyglet.window.key.UP:
            pyglet.clock.schedule_interval(func = self.update2, interval = 1/60.)
            print "The 'UP' key was pressed"

    def on_key_release(self, symbol, modifiers):
        self.keys_held.pop(self.keys_held.index(symbol))

    def update1(self, interval):
        # Move 10 pixels per second
        self.player.x += interval * 10

    def update2(self, interval): #New movement function
        if pyglet.window.key.UP in self.keys_held:
            self.player.y += 0.05

if __name__ == "__main__":
    window = ProcinctuWindow()
    pyglet.app.run()
