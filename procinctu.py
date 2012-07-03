import pyglet

class Assassin(pyglet.sprite.Sprite):
    def __init__(self, batch):
        pyglet.sprite.Sprite.__init__(self, pyglet.resource.image("assassin1.png"))
        self.x = 50
        self.y = 30

    def forward_movement(self):
        pyglet.sprite.Sprite.__init__(self,
pyglet.resource.image("assassin2.png"), x = self.x, y = self.y)
        pyglet.sprite.Sprite.__init__(self,
pyglet.resource.image("assassin1.png"), x = self.x, y = self.y)     

class Fireball(pyglet.sprite.Sprite):
    def __init__(self, batch):
        pyglet.sprite.Sprite.__init__(self, pyglet.resource.image("fireball.png"))
        self.x = window.player.x + 10
        self.y = window.player.y + 10
          
class ProcinctuWindow(pyglet.window.Window):
    def __init__(self):
        pyglet.window.Window.__init__(self, width = 315, height = 220)
        self.batch_draw = pyglet.graphics.Batch()
        self.background = pyglet.resource.image("battlebackground.png")
        self.player = Assassin(batch = self.batch_draw)
        self.fps_display = pyglet.clock.ClockDisplay()
        self.keys_held = []      
        self.fireball = []
        self.schedule3 = pyglet.clock.schedule_interval(func = self.update3, interval = 1/60.)
        self.schedule1 = pyglet.clock.schedule_interval(func = self.update1, interval = 1/60.) 
 
    def on_draw(self):
        self.background.blit(0, 0)
        self.fps_display.draw()
        self.batch_draw.draw()
        self.player.draw()  
        if len(self.fireball) != 0:
            for i in range(len(self.fireball)):
                self.fireball[i].draw()

    def on_key_press(self, symbol, modifiers):
        self.keys_held.append(symbol)
        if symbol == pyglet.window.key.A:
            self.fireball.append(Fireball(batch = self.batch_draw))            
            print "The 'A' key was pressed"
        if symbol == pyglet.window.key.S:
            self.music = pyglet.media.load("Comet.wav", streaming = False)
            self.music.play()
            print "The 'S' key was pressed"
        if symbol == pyglet.window.key.RIGHT:
            self.player.forward_movement()
            print "The 'RIGHT' key was pressed"
        if symbol == pyglet.window.key.LEFT:
            print "The 'LEFT' key was pressed"
        if symbol == pyglet.window.key.UP:
            print "The 'UP' key was pressed"
        if symbol == pyglet.window.key.DOWN:
            print "The 'DOWN' key was pressed"

    def on_key_release(self, symbol, modifiers):
        self.keys_held.pop(self.keys_held.index(symbol))

    def update1(self, interval):
        if pyglet.window.key.RIGHT in self.keys_held:
            self.player.x += 50 * interval
        if pyglet.window.key.LEFT in self.keys_held:
            self.player.x -= 50 * interval
        if pyglet.window.key.UP in self.keys_held:
            self.player.y += 50 * interval
        if pyglet.window.key.DOWN in self.keys_held:
            self.player.y -= 50 * interval

    def update3(self, interval):
        for i in range(len(self.fireball)):
            self.fireball[i].x += 100 * interval 

if __name__ == "__main__":
    window = ProcinctuWindow()
    pyglet.app.run()
