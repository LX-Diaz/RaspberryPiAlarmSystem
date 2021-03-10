#!/usr/bin/python3
import serial
import re

'''Core data source of the program, the back bone. Cleans and writes the received data from the
the transmitter circuit into a dictionary. Then outputs the dictionary to be displayed by main program'''

DEBUG = True

class DataReader:


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

        

    def ser_data_process(self):
        try:
            with serial.Serial('/dev/ttyS0', 9600, timeout = 1) as ser:  #Opens serial port
                self.line = ser.read(100).strip()
                if DEBUG:
                    ''' sudo cat /dev/ttyS0 in terminal to doublecheck input'''
                    print(self.line)
                self.linedec = self.line.decode('ascii')
                #self.idclean = re.sub('\d\.\d\d+\s+(ID):', 'ID:', self.linedec)
                #self.buzzclean = re.sub('Buzzer\s+(Off)(On)?', '', str(self.idclean))
                #self.cleanline = re.sub('\s', '', str(self.linedec))
                self.cleantemp = re.sub('\*', '˚', str(self.linedec))
                #self.cline_s = str(self.linedec)
                self.splitlist = self.cleantemp.split(":")
                self.splitList = self.cleantemp.split(":")
                self.buffer = dict(zip(self.splitlist[0::2],self.splitList[1::2]))

                if 'ID' not in self.buffer or 'TS' not in self.buffer or 'Door' not in self.buffer:
                    if DEBUG:
                        print("Poor Data retrieved, dumping and trying again...")
                        print(self.buffer)

                elif 'ID' in self.buffer and 'TS' in self.buffer and 'TF' in self.buffer and 'Door' in self.buffer:
                    # if DEBUG:
                    #     print(self.buffer)
                    #     print('Good Data received, proceeding...')
                    self.data[self.buffer['ID']] = {'ID': f"{self.buffer['ID']}", 'TF': f"{self.buffer['TF']}", 'Door': f"{self.buffer['Door']}", 'TS': f"{self.buffer['TS']}"}
                    print(self.data)
                    return self.data

        except IOError:
            print('IOError...trying again')
            pass
        except UnicodeDecodeError:
            print('Unicode Error...trying again')
            pass
        except:
            pass