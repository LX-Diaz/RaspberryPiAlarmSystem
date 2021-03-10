import pyglet, glooey
from pyglet import image
from pyglet.gl import *
from .AlarmController import AlarmController


pyglet.resource.path = ['./Resources']
pyglet.resource.reindex()

alarm = AlarmController.AlarmController()
alarm.get_alarm_status()

def displayGUI():
        # Open a Window
        window = pyglet.window.Window(width=800, height=480)  # fullscreen=True
        gui = glooey.Gui(window)

        class StatusLabel(glooey.Label):
                custom_font_name = "Calibri"
                custom_font_size = 12
                custom_color = "0080ff"

        class ArmButton(glooey.Button):
                if alarm.system_armed:
                        class Base(glooey.Image):
                                custom_image = pyglet.resource.image('Button2.png')

                elif not alarm.system_armed:
                        class Base(glooey.Image):
                                custom_image = pyglet.resource.image('Button3.png')

        class DoorStatusLabel(glooey.Label):
                custom_font_name = "Calibri"
                custom_font_size = 9
                custom_color = "0080ff"

        class TemperatureData(glooey.Label):
                custom_font_name = "Calibri"
                custom_font_size = 9
                custom_color = "0080ff"

        class Clock(glooey.Label):
                custom_font_name = "Calibri"
                custom_font_size = 9
                custom_color = "0080ff"

        SensorStatusVbox = glooey.VBox()

        self.grid = glooey.Grid()
        gui.add(self.grid)

