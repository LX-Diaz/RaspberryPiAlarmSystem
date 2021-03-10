#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import sys
from .SerialDataCollector import DataReader


DEBUG = False


class AlarmController:

        def __init__(self):
                #on instantiation, sets the system as disarmed (Idle)
                #initiates the variables for the object
                #configures the RPI GPIO ppin for controlling the alarm buzzer
                self.system_armed = False #All functions dependent on system state should go by this variable
                self.values = None
                self.time_string = None
                GPIO.setmode(GPIO.BCM)
                GPIO.setwarnings(False)
                GPIO.setup(22,GPIO.OUT)
                GPIO.output(22,GPIO.LOW)
                self.dataReader = SerialDataCollector.DataReader()
                self.Clock()

        def arm_system(self):
                #Sets the system state variable to True, call to arm system
                self.system_armed = True
                print('Arming System...')

        def disarm_system(self):
                #Sets the system state variable to False, call to disarm system
                self.system_armed = False
                print('Disarming System...')

                
        
        # def get_alarm_status(self):
        #         if self.system_armed == True:
        #                 self.status = 'Armed'
        #         if self.system_armed == False:
        #                 self.status = 'Idle'
        #         if DEBUG:
        #                 print(f"System {self.status}")
        #         return self.status
    
        def Alarm_on(self):
                GPIO.output(22,GPIO.HIGH)
                print('Sounding Alarm!')

        def Alarm_off(self):
                GPIO.output(22,GPIO.LOW)
                print('Shutting alarm off...')

        def Clock(self):
                self.time_string = time.strftime("%H:%M:%S")
                return self.time_string

        def toggle_alarm_status(self):
                if self.system_armed == True:
                        self.system_armed = False
                        self.Alarm_off()
                        pass
                elif self.system_armed == False:
                        self.system_armed = True
                        self.status = 'Armed'
                        pass
                if DEBUG:
                        print(f"System {self.status}")
                return self.status

        def WatchDog(self):
                dataReader.ser_data_process()
                if dataReader.door_stat == "Open":
                        self.Alarm_on()


