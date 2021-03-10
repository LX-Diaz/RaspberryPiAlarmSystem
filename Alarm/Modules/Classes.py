#!/usr/bin/python3
import RPi.GPIO as GPIO
import serial
import re



class DataCollector:


    def __init__(self):
        self.line = None
        self.linedec = None
        self.idclean = None
        self.buzzclean = None
        self.cleanline = None
        self.cline_s = None
        self.splitlist = None
        self.splitList = None
        self.data = None
        self.ser_data_process()

    def ser_data_process(self):
        print('Opening Serial port...')
        with serial.Serial('/dev/ttyS0', 9600, timeout = 1) as ser:
            self.line = ser.read(100).strip()   
            print('Retrieving data...\nProcessing...')
            self.linedec = self.line.decode('cp437')
            self.idclean = re.sub('\d\.\d\d+\s+(ID):', 'ID:', self.linedec)
            self.buzzclean = re.sub('Buzzer\s+(Off)(On)?', '', str(self.idclean))
            self.cleanline = re.sub('\s', '', str(self.buzzclean))
            self.cline_s = str(self.cleanline)
            self.splitlist = self.cline_s.split(":")
            self.splitList = self.cline_s.split(":")
            self.data = dict(zip(self.splitlist[0::2],self.splitList[1::2])

                             
    def get_data(self):
        return self.data

    def get_data_dictionary_string(self):
        return str(self.data)

    def get_data_values(self):
        return self.data.values()

    def get_data_items(self):
        return self.data.items()

    def get_data_keys(self):
        return self.data.keys()


    

    
class AlarmController:

    def __init__(self):
        self.system_armed = False
        self.values = None
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(22,GPIO.OUT)
        GPIO.output(22,GPIO.LOW)
        

    def arm_system(self):
        self.system_armed = True
        print('Arming System...')

    def disarm_system(self):
        self.system_armed = False
        print('Disarming System...')
        
    def get_alarm_status(self):
        return self.system_armed
    
    def Alarm_on(self):
        GPIO.output(22,GPIO.HIGH)
        print('Sounding Alarm!')

    def Alarm_off(self):
        GPIO.output(22,GPIO.LOW)
        print('Shutting alarm off...')
        

