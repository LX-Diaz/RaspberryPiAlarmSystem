#!/usr/bin/python3
from Modules import AlarmController, SerialDataCollector
import pyglet, glooey
from pyglet import image
from pyglet.gl import *
from pyglet.window import mouse
import RPi.GPIO as GPIO

pyglet.resource.path = ['./Resources']
pyglet.resource.reindex()

"""Device indicator dictionary (for more transmitters, add them here)
 remember to add new label and refer to the dictionary key"""
DEVICES = {'1': 'Front Door', '2': 'Sliding Door'}

# Initiate classes
alarm = AlarmController.AlarmController()
DataReader = SerialDataCollector.DataReader()


pyglet.resource.path = ['./Resources']
pyglet.resource.reindex()
alarm.get_alarm_status()

# Open a Window
window = pyglet.window.Window(width=800, height=480)  # fullscreen=True
gui = glooey.Gui(window)


def displayGUI():
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

    sensor_status_Vbox = glooey.VBox()
    for key in DEVICES:
        sensor = DEVICES[DataReader.device_id]
        sensor_status_label = DoorStatusLabel(f"{sensor}:{DataReader.door_stat}")
        sensor_status_Vbox.add(sensor_status_label)
    right_panel = glooey.VBox()

    # Add to grid
    grid = glooey.HBox()
    grid.add(sensor_status_Vbox)  # Left Panel
    grid.add(glooey.placeholder())  # Center Panel
    grid.add(right_panel)  # Right Panel
    gui.add(grid)


def update(dt):
    print(dt)
    DataReader.ser_data_process()
    alarm.get_alarm_status()
    displayGUI()



@window.event
def on_draw():
    window.clear()
    displayGUI()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    window.config.alpha_size = 8
    window.set_exclusive_mouse(False)


# main code starts here
pyglet.clock.schedule(update)
pyglet.app.run()
