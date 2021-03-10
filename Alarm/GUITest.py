import pyglet, glooey
from pyglet import image
from pyglet.gl import *
from pyglet.window import mouse


pyglet.resource.path = ['./Resources']
pyglet.resource.reindex()
window = pyglet.window.Window(width=800,height=480)#fullscreen=True
glui = glooey.Gui(window)


class Arm_Button (glooey.Button):
        
        class Base(glooey.Image):
                custom_image = pyglet.resource.image('Button2.png')
                
                
button = Arm_Button()
Clocktxt = pyglet.text.Label('00:00:00', font_name='Outrider Condensed', font_size=20, x=610, y=425)


glui.add(button)
glui.add(Clocktxt)


pyglet.app.run()
