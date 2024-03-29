import pyglet

def preload():
    """These values are loaded before the game loop is initiated in order to run the game more smoothly""" 
    assassin_moving_forward_image_list = [pyglet.image.load('assassin1.png'), pyglet.image.load('assassin2.png')]    
    global assassin_moving_forward_animation
    assassin_moving_forward_animation = pyglet.image.Animation.from_image_sequence(assassin_moving_forward_image_list, 0.3) 
    
    global assassin_standing_animation
    assassin_standing_animation = pyglet.image.load("assassin1.png")

    global warrior_standing_animation
    warrior_standing_animation = pyglet.image.load("warrior1.png")

    global comet
    comet = pyglet.media.load("Comet.wav", streaming = False)    

preload()


class Assassin(pyglet.sprite.Sprite):
    def __init__(self, batch, img):
        pyglet.sprite.Sprite.__init__(self, img, x = 50, y = 30)

    def stand(self):
        self.image = assassin_standing_animation
        return self

    def move(self):
        self.image = assassin_moving_forward_animation   
        return self

class Warrior(pyglet.sprite.Sprite):
    def __init__(self, batch, img):
        pyglet.sprite.Sprite.__init__(self, img, x = 220, y = 30)

    
class Fireball(pyglet.sprite.Sprite):
    def __init__(self, batch):
        pyglet.sprite.Sprite.__init__(self, pyglet.resource.image("fireball.png"))
        self.x = window.player1.x + 10
        self.y = window.player1.y + 10

          
class ProcinctuWindow(pyglet.window.Window):
    def __init__(self):
        pyglet.window.Window.__init__(self, width = 315, height = 220)
        self.batch_draw = pyglet.graphics.Batch()
        self.background = pyglet.resource.image("battlebackground.png")
        self.player1 = Assassin(batch = self.batch_draw, img = assassin_standing_animation)
        self.player2 = Warrior(batch = self.batch_draw, img =  warrior_standing_animation)
        self.fps_display = pyglet.clock.ClockDisplay()
        self.keys_held = []      
        self.fireball = []
        self.schedule3 = pyglet.clock.schedule_interval(func = self.update3, interval = 1/60.)
        self.schedule1 = pyglet.clock.schedule_interval(func = self.update1, interval = 1/60.) 
 
    def on_draw(self):
        self.background.blit(0, 0)
        self.fps_display.draw()
        self.batch_draw.draw()
        self.player1.draw() 
        self.player2.draw() 
        if len(self.fireball) != 0:
            for i in range(len(self.fireball)):
                self.fireball[i].draw()

    def on_key_press(self, symbol, modifiers):
        self.keys_held.append(symbol)
        if symbol == pyglet.window.key.A:
            self.fireball.append(Fireball(batch = self.batch_draw))            
            print "The 'A' key was pressed"
        if symbol == pyglet.window.key.S:
            self.music = comet
            self.music.play()
            print "The 'S' key was pressed"
        if symbol == pyglet.window.key.RIGHT:
            self.player1.move()
            print "The 'RIGHT' key was pressed"
        if symbol == pyglet.window.key.LEFT:
            print "The 'LEFT' key was pressed"
        if symbol == pyglet.window.key.UP:
            print "The 'UP' key was pressed"
        if symbol == pyglet.window.key.DOWN:
            print "The 'DOWN' key was pressed"

    def on_key_release(self, symbol, modifiers):
        self.keys_held.pop(self.keys_held.index(symbol))
        if symbol == pyglet.window.key.RIGHT:
            self.player1.stand()

    def update1(self, interval):
        if pyglet.window.key.RIGHT in self.keys_held:
            self.player1.x += 50 * interval
        if pyglet.window.key.LEFT in self.keys_held:
            self.player1.x -= 50 * interval
        if pyglet.window.key.UP in self.keys_held:
            self.player1.y += 50 * interval
        if pyglet.window.key.DOWN in self.keys_held:
            self.player1.y -= 50 * interval

    def update3(self, interval):
        for i in range(len(self.fireball)):
            self.fireball[i].x += 100 * interval 


if __name__ == "__main__":
    window = ProcinctuWindow()
    pyglet.app.run()
