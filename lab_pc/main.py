import os
import tkinter as tk
import csv
import time

import threading
import serial
from static_gui import SGUI
class MFUNC:
    def __init__(self):
        self.stime = time.time()
        self.nport = None
        self.sport = None
        self.serial_door = False
        self.root_open = False
        self.serial_connect = False
        self.reading = False
        self.toWrite = False
        self.sentStart = False
        self.SEDReset = False
        self.sendMED = False
        self.sendTYPE = False
        self.skinType = None
        self.connected = False
        self.toSend = []
        self.MEDBuffer = []
        self.time = []
        self.index = []

        self.multi_setup()
    
    def multi_setup(self):
        self.tsk1 = threading.Thread(name="GUI Thread", target=self.root_build)
        self.tsk2 = threading.Thread(name="Serial Thread", target=self.serial_checking)
        self.tsk1.start()
        self.tsk2.start()

    def root_build(self):
        self.root = tk.Tk()
        self.root.title("UV Index Lanyard")
        self.gui = SGUI(self.root, self)
        self.root_open = True
        self.root.mainloop()

    def set_port(self):
        if(self.sport != None):
            self.serial_close()
            self.gui.connect.config(text="Connect")
        else:
            scom = ("COM" + str(self.nport))
            try:
                self.sport = serial.Serial(port=scom, baudrate=9600, bytesize=8, timeout=None, stopbits=serial.STOPBITS_ONE)
                self.gui.sb_update("Serial Port Connected: " + scom)
                self.gui.connect.config(text="Disconnect")
                self.serial_door = True
                self.connected = True
                self.gui.update_connect()
            except:
                self.sport=None
                self.nport=None
                self.gui.sb_update("Com Port Not Avaliable")
                self.gui.nb.config(fg='grey')
                self.gui.nb.delete(0,tk.END)
                self.gui.nb.insert(0,"Enter Com Port Number")
                self.gui.connect.config(text="Connect")
                self.gui.connect.config(state=tk.DISABLED)
    
    def serial_close(self):
        self.sport.close()
        self.connected = False
        self.gui.update_connect()
        self.serial_door = False

    def serial_open(self):
        self.sport.open()
        self.connected = True
        self.gui.update_connect()
        self.serial_door = True

    def serial_write(self, wstring):
        wstring = wstring.encode('Ascii')
        try:
            self.sport.write(wstring)
        except:
            self.connected = False
            self.gui.update_connect()
            self.gui.sb_update("Port Disconnected")
            self.gui.connect.config(text="Connect")
            self.sport = None
            self.serial_door = False

    def serial_read(self):
        lineread = ""
        i=0
        while(True):
            try:
                read = self.sport.read()
                read = read.decode('Ascii')
                if(read == '*'):
                    if(i>0):
                        break
                lineread = lineread + read
                i += 1
            except:
                self.connected = True
                self.gui.update_connect()
                self.gui.sb_update("Port Disconnected")
                self.gui.connect.config(text="Connect")
                self.sport = None
                self.serial_door = False
                break
        return lineread
    
    def serial_test(self, string):
        self.serial_write(string)
        self.serial_read()
    
    def serial_checking(self):
        while(True):
            if(self.sport == None):
                pass
            elif(self.serial_door == False):
                pass
            elif(self.root_open == False):
                break
            else:
                read = self.serial_read()
                if(read == ""):
                    pass
                elif(read[0] == '*'):
                    read = read.replace("*","")
                    self.gui.sb_update(read)
                elif(read == '1'):
                    if(self.SEDReset):
                        self.serial_write('2')
                        self.serial_read()
                        self.SEDReset = False
                        self.toSend = []
                    elif(self.sendMED):
                        self.gui.sb_update("Uploading MED/Type")
                        self.serial_write("0")
                        for numb in self.MEDBuffer:
                            print(numb)
                            self.serial_read()
                            self.serial_write(str(numb))
                        self.serial_read()
                        self.sendMED = False
                        self.MEDBuffer = []
                    elif(self.sendTYPE):
                        self.gui.sb_update("Uploading Skin Type")
                        self.serial_write('3')
                        self.serial_write(str(self.skinType))
                        self.serial_read()
                        self.sendTYPE = False
                    else:
                        self.serial_write('1')

MFUNC()