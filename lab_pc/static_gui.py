import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import quiz_gui
from matplotlib import style
import csv
from quiz_gui import QGUI

class SGUI:
    def __init__(self, master, main):
        self.master = master
        self.spause = False
        self.main = main
        self.windowed = {'x':800,'y':600}
        self.full_screen = {'x':master.winfo_screenwidth(),'y':master.winfo_screenheight()}
        self.fitz_score = None
        self.type = None
        self.med_score = None
        self.cf()

    def cf(self):
        self.cf1 = tk.Frame(self.master, bg="dark grey", borderwidth=4)
        self.cf1.pack()
        self.cf1_title = tk.Label(self.cf1, bg="dark grey", width=30, text="Application Mode:")
        self.cf1_title.pack(anchor=tk.N, fill=tk.X)
        self.cb1 = tk.Button(self.cf1, text="Windowed Mode", command=lambda:self.sizesetter(0))
        self.cb1.pack(fill=tk.X, anchor=tk.N)
        self.cb2 = tk.Button(self.cf1, text="Full Screen Mode", command=lambda:self.sizesetter(1))
        self.cb2.pack(fill=tk.X, anchor=tk.N)

    def MED_Handle(self, MED, Type):
        print(len(str(MED)))
        if(len(str(MED))<2):
            self.main.MEDBuffer.append(0)
        if(len(str(MED))<3):
            self.main.MEDBuffer.append(0)
        for number in str(MED):
            self.main.MEDBuffer.append(int(number))
        self.main.skinType = Type
        self.UMED.config(state=tk.ACTIVE)

    def MED_Upload(self):
        self.main.sendMED = True
        self.main.sendTYPE = True

    def set_score(self, intscore, type_known):
        if(intscore == None):
            self.mf()
        else:
            self.mf()
            if(type_known):
                if(intscore == 0):
                    self.dt_fitzpatrick.config(text="Fitzpatrick Skin Type: Type 1")
                    self.dt_MED.config(text="MED (in units of SED): 150")
                    self.type = 1
                    self.med_score = 150
                elif(intscore == 1):
                    self.dt_fitzpatrick.config(text="Fitzpatrick Skin Type: Type 2")
                    self.dt_MED.config(text="MED (in units of SED): 220")
                    self.type = 2
                    self.med_score = 220
                elif(intscore == 2):
                    self.dt_fitzpatrick.config(text="Fitzpatrick Skin Type: Type 3")
                    self.dt_MED.config(text="MED (in units of SED): 290")
                    self.type = 3
                    self.med_score = 290
                elif(intscore == 3):
                    self.dt_fitzpatrick.config(text="Fitzpatrick Skin Type: Type 4")
                    self.dt_MED.config(text="MED (in units of SED): 370")
                    self.type = 4
                    self.med_score = 370
                elif(intscore == 4):
                    self.dt_fitzpatrick.config(text="Fitzpatrick Skin Type: Type 5")
                    self.dt_MED.config(text="MED (in units of SED): 440")
                    self.type = 5
                    self.med_score = 440
                elif(intscore == 5):
                    self.dt_fitzpatrick.config(text="Fitzpatrick Skin Type: Type 6")
                    self.dt_MED.config(text="MED (in units of SED): 440")
                    self.type = 6
                    self.med_score = 440
            else:
                self.fitz_score = intscore
                if(0<=intscore<=6):
                    self.dt_fitzpatrick.config(text="Fitzpatrick Skin Type: Type 1")
                    self.dt_MED.config(text="MED (in units of SED): 150")
                    self.type = 1
                    self.med_score = 150
                elif(7<=intscore<=13):
                    self.dt_fitzpatrick.config(text="Fitzpatrick Skin Type: Type 2")
                    self.dt_MED.config(text="MED (in units of SED): 220")
                    self.type = 2
                    self.med_score = 220
                elif(14<intscore<20):
                    self.dt_fitzpatrick.config(text="Fitzpatrick Skin Type: Type 3")
                    self.dt_MED.config(text="MED (in units of SED): 290")
                    self.type = 3
                    self.med_score = 290
                elif(21<=intscore<=27):
                    self.dt_fitzpatrick.config(text="Fitzpatrick Skin Type: Type 4")
                    self.dt_MED.config(text="MED (in units of SED): 370")
                    self.type = 4
                    self.med_score = 370
                elif(28<=intscore<=34):
                    self.dt_fitzpatrick.config(text="Fitzpatrick Skin Type: Type 5")
                    self.dt_MED.config(text="MED (in units of SED): 440")
                    self.type = 5
                    self.med_score = 440
                elif(intscore>=35):
                    self.dt_fitzpatrick.config(text="Fitzpatrick Skin Type: Type 6")
                    self.dt_MED.config(text="MED (in units of SED): 440")
                    self.type = 6
                    self.med_score = 440
            self.MED_Handle(self.med_score, self.type)
            
    def sizesetter(self, result):
        if(result == 0):
            self.x = self.windowed['x']
            self.y = self.windowed['y']
        else:
            self.x = self.full_screen['x']
            self.y = self.full_screen['y']
        
        self.cf1.destroy()
        self.mf()

    def fson(self):
        self.master.attributes('-fullscreen', True)
        self.mff.destroy()
        self.x = self.full_screen['x']
        self.y = self.full_screen['y']
        self.mf()
        
    def fsoff(self):
        self.master.attributes('-fullscreen', False)
        self.mff.destroy()
        self.x = self.windowed['x']
        self.y = self.windowed['y']
        self.mf()

    def kprogram(self):
        self.main.root_open = False
        self.master.destroy()
    
    def oquiz(self, know_skin_type):
        self.qcf.destroy()
        self.qzgui = QGUI(self.master, self, self.x, self.y, know_skin_type)
    
    def qcheck(self):
        self.mff.destroy()
        self.qcf = tk.Frame(self.master, bg="dark grey", borderwidth=4)
        self.qcf.pack()
        self.qc_title = tk.Label(self.qcf, bg="dark grey", text="Do You Know Your Fitzpatrick Skin Type?")
        self.qc_title.pack(anchor=tk.N, fill=tk.X)
        self.qcb1 = tk.Button(self.qcf, text="I know my Fitzpatrick Skin Type", command=lambda:self.oquiz(True))
        self.qcb1.pack(fill=tk.X, anchor=tk.N)
        self.qcb2 = tk.Button(self.qcf, text="I do not know my skin type (Take Quiz)", command=lambda:self.oquiz(False))
        self.qcb2.pack(fill=tk.X, anchor=tk.N)

    def dtype(self):
        self.dtf = tk.Frame(self.sf3, height=40, width=((self.x-8)/2)-4)
        self.dtf.pack_propagate(0)
        self.dtf.pack(fill=tk.X, anchor = tk.N)
        self.dt_fitzpatrick = tk.Label(self.dtf, bg = "dark grey", text = "Fitzpatrick Skin Type: Unknown", font='TkHeadingFont 12', height=2)
        self.dt_fitzpatrick.pack(fill=tk.BOTH)
        self.dtf2 = tk.Frame(self.sf3, height=40, width=((self.x-8)/2)-4)
        self.dtf2.pack_propagate(0)
        self.dtf2.pack(fill=tk.X, anchor=tk.N)
        self.dt_MED = tk.Label(self.dtf2, bg = "dark grey", text="MED (in units of SED): Unknown", font="TkHeadingFont 12", height=2)
        self.dt_MED.pack(fill=tk.BOTH)
    
    def update_connect(self):
        if(self.main.connected == True):
            self.scon.config(text = "Connected", fg = "green")
        else:
            self.scon.config(text = "Not Connected", fg = "red")

    def sport_select(self):
        item = self.nb.get()
        self.nb.delete(0,tk.END)
        self.dummy.focus()
        try:
            item = int(item)
            self.main.nport=item
            self.connect.config(state=tk.ACTIVE)
        except:
            self.nb.config(fg="grey")
            self.nb.insert(0,"Please Enter Number Value of Com Port")
            self.sb_update("Invalid Com Number Entered")

    def mf(self):
        """ sets up the main frame of the static gui which all options and boxes will be inside of """
        if(self.full_screen['x'] == self.x):
            self.master.attributes('-fullscreen', True)

        self.mff = tk.Frame(self.master, bg="black", borderwidth=4, height=self.y, width=self.x)
        self.mff.pack_propagate(0)
        self.mff.pack()

        self.dummy = tk.Entry(self.master)
        self.dummy.pack()
        self.dummy.place(height=0)

        self.tf = tk.Frame(self.mff, height=30, width=(self.x-8))
        self.tf.pack(fill=tk.X, anchor=tk.N)
        self.mf_title = tk.Label(self.tf, bg = "dark grey", text = "UV Reader PC Program", font='TkHeadingFont 12', height = 1)
        self.mf_title.pack(fill=tk.BOTH)
        
        self.sf1 = tk.Frame(self.mff, bg = "light grey", width=(self.x-8), height=self.y-60)
        self.sf1.pack_propagate(0)
        self.sf1.pack(fill=tk.BOTH)

        self.sf2 = tk.Frame(self.sf1, bg="green", width=(self.x-8)/2, height=(self.y-60)/2)
        self.sf2.grid_propagate(0)
        self.sf2.grid(column=0,row=0)
        self.sf3 = tk.Frame(self.sf1, bg="blue", width=(self.x-8)/2, height=(self.y-60)/2)
        self.sf3.grid_propagate(0)
        self.sf3.grid(column=1,row=0)
        self.dtype()
        self.sf4 = tk.Frame(self.sf1, bg="white", width=(self.x-8)/2, height=(self.y-60)/2)
        self.sf4.grid_propagate(0)
        self.sf4.grid(column=0,row=1)
        self.sf5 = tk.Frame(self.sf1, bg="yellow", width=(self.x-8)/2, height=(self.y-60)/2)
        self.sf5.grid_propagate(0)
        self.sf5.grid(column=1,row=1)

        self.gb()
        self.opts()
        self.MED_Setup()

        self.tb = tk.Frame(self.mff, bg="grey", borderwidth=4, height=30, width=(self.x-8))
        self.tb.pack_propagate(0)
        self.tb.pack(fill=tk.BOTH)

        self.tbf1 = tk.Frame(self.tb, bg="grey", height=30, width=(self.x-8)/4)
        self.tbf1.grid_propagate(0)
        self.tbf1.grid(row=0, column=0)
        self.tbf2 = tk.Frame(self.tb, bg="grey", height=30, width=(self.x-8)/4)
        self.tbf2.grid_propagate(0)
        self.tbf2.grid(row=0, column=1)
        self.tbf3 = tk.Frame(self.tb, bg="grey", height=30, width=(self.x-8)/4)
        self.tbf3.grid_propagate(0)
        self.tbf3.grid(row=0, column=2)
        self.tbf4 = tk.Frame(self.tb, bg="grey", height=30, width=(self.x-8)/4)
        self.tbf4.grid_propagate(0)
        self.tbf4.grid(row=0, column=3)

        self.tbf4g1 = tk.Frame(self.tbf4)
        self.tbf4g1.grid_propagate(0)
        self.tbf4g1.grid(column=0, row=0)
        self.tbf4g2 = tk.Frame(self.tbf4)
        self.tbf4g2.grid_propagate(0)
        self.tbf4g2.grid(column=1, row=0)

        self.tbb1f = tk.Frame(self.tbf1, bg = 'grey', width= int((self.x-8)/4), height = 30)
        self.tbb1f.pack_propagate(0)
        self.tbb1f.pack(fill=tk.BOTH)
        self.scon = tk.Label(self.tbb1f, bg = "grey", width = int((self.x-8)/4), height =30, text = "Not Connected", fg = "red", font='TkHeadingFont 12')
        self.scon.pack(fill=tk.BOTH)

        self.tbb4f = tk.Frame(self.tbf4g1, bg='grey', width=(self.x-8)/8, height=30)
        self.tbb4f.pack_propagate(0)
        self.tbb4f.pack(fill=tk.BOTH)
        self.tbb4 = tk.Button(self.tbb4f, command=lambda:self.fson(), text="Fullscreen On")
        self.tbb4.pack(fill=tk.BOTH)

        self.tbb5f = tk.Frame(self.tbf4g2, bg="grey", width=(self.x-8)/8, height=30)
        self.tbb5f.pack_propagate(0)
        self.tbb5f.pack(fill=tk.BOTH)
        self.tbb5 = tk.Button(self.tbb5f, command=lambda:self.kprogram(), text="Close")
        self.tbb5.pack(fill=tk.BOTH)

        self.tbb3f = tk.Frame(self.tbf3, bg="grey", width=(self.x-8)/4, height=30)
        self.tbb3f.pack_propagate(0)
        self.tbb3f.pack(fill=tk.BOTH)
        self.tbb3 = tk.Button(self.tbb3f, command=lambda:self.qcheck(), text="Take Skin Type Quiz")
        self.tbb3.pack(fill=tk.BOTH)

        self.sb()

        if(self.full_screen['x'] == self.x):
            self.tbb4.config(text="Fullscreen Off", command=lambda:self.fsoff())
    
    def spause_press(self):
        if(self.spause):
            self.spause = False
            self.pserial.config(text="Pause Serial")
        else:
            self.spause = True
            self.pserial.config(text="Play Seiral")

    def sb(self):
        self.serial1 = ""
        self.serial2 = ""
        self.serial3 = ""
        self.serial4 = ""
        self.serial5 = ""
        self.serial6 = ""
        self.serial7 = ""
        self.serial8 = ""
        self.serial9 = ""
        self.serial10 = ""
        self.serial11 = ""

        self.sbsf = tk.Frame(self.sf4, bg = "black", height=(self.y-64)/2, width=(self.x-12)/2)
        self.sbsf.pack_propagate(0) 
        self.sbsf.pack()
        self.sbl1 = tk.Label(self.sbsf, bg = "black", fg="white", text =self.serial1, font='TkHeadingFont 12', height=1, anchor=tk.W)
        self.sbl1.pack(fill=tk.X)
        self.sbl2 = tk.Label(self.sbsf, bg = "black", fg="white", text =self.serial2, font='TkHeadingFont 12', height=1, anchor=tk.W)
        self.sbl2.pack(fill=tk.X)
        self.sbl3 = tk.Label(self.sbsf, bg = "black", fg="white", text =self.serial3, font='TkHeadingFont 12', height=1, anchor=tk.W)
        self.sbl3.pack(fill=tk.X)
        self.sbl4 = tk.Label(self.sbsf, bg = "black", fg="white", text =self.serial4, font='TkHeadingFont 12', height=1, anchor=tk.W)
        self.sbl4.pack(fill=tk.X)
        self.sbl5 = tk.Label(self.sbsf, bg = "black", fg="white", text =self.serial5, font='TkHeadingFont 12', height=1, anchor=tk.W)
        self.sbl5.pack(fill=tk.X)
        self.sbl6 = tk.Label(self.sbsf, bg = "black", fg="white", text =self.serial6, font='TkHeadingFont 12', height=1, anchor=tk.W)
        self.sbl6.pack(fill=tk.X)
        self.sbl7 = tk.Label(self.sbsf, bg = "black", fg="white", text =self.serial7, font='TkHeadingFont 12', height=1, anchor=tk.W)
        self.sbl7.pack(fill=tk.X)
        self.sbl8 = tk.Label(self.sbsf, bg = "black", fg="white", text =self.serial8, font='TkHeadingFont 12', height=1, anchor=tk.W)
        self.sbl8.pack(fill=tk.X)
        self.sbl9 = tk.Label(self.sbsf, bg = "black", fg="white", text =self.serial9, font='TkHeadingFont 12', height=1, anchor=tk.W)
        self.sbl9.pack(fill=tk.X)
        self.sbl10 = tk.Label(self.sbsf, bg = "black", fg="white", text =self.serial10, font='TkHeadingFont 12', height=1, anchor=tk.W)
        self.sbl10.pack(fill=tk.X)
        self.sbl11 = tk.Label(self.sbsf, bg = "black", fg="white", text =self.serial11, font='TkHeadingFont 12', height=1, anchor=tk.W)
        self.sbl11.pack(fill=tk.X)
    
    def sb_update(self, text):
        self.serial1 = self.serial2
        self.serial2 = self.serial3
        self.serial3 = self.serial4
        self.serial4 = self.serial5
        self.serial5 = self.serial6
        self.serial6 = self.serial7
        self.serial7 = self.serial8
        self.serial8 = self.serial9
        self.serial9 = self.serial10
        self.serial10 = self.serial11
        self.serial11 = text

        if(self.spause == False):
            self.sbl1.config(text=self.serial1)
            self.sbl2.config(text=self.serial2)
            self.sbl3.config(text=self.serial3)
            self.sbl4.config(text=self.serial4)
            self.sbl5.config(text=self.serial5)
            self.sbl6.config(text=self.serial6)
            self.sbl7.config(text=self.serial7)
            self.sbl8.config(text=self.serial8)
            self.sbl9.config(text=self.serial9)
            self.sbl10.config(text=self.serial10)
            self.sbl11.config(text=self.serial11)
    
    def gb(self):
        matplotlib.use('TkAgg')
        with open ('Graph.txt','r') as csvfile:
            plots= csv.reader(csvfile, delimiter = ',')
            for row in plots:
                self.main.time.append(int(row[0]))
                self.main.index.append(int(row[1]))
        
        style.use("ggplot")
        self.fig = plt.figure(1)
        plt.ion()
        plt.plot(self.main.time, self.main.index)
        plt.ylabel("UV Index")
        plt.xlabel("Time")
        plt.title("UV Index Over Time")

        canvas = FigureCanvasTkAgg(self.fig, master=self.sf2)
        self.plot_widget = canvas.get_tk_widget()
        self.plot_widget.config(width=(self.x-12)/2, height=(self.y-64)/2)
        self.plot_widget.pack(fill=tk.BOTH)
    
    def gb_update(self):
        self.fig.clear()
        self.plot_widget.destroy()
        self.gb()
    
    def SED_Reset(self):
        self.main.SEDReset = True

    def handle_focus_in(self,_):
        self.nb.delete(0, tk.END)
        self.nb.config(fg='black')

    def handle_focus_in2(self,_):
        self.MEDE.delete(0, tk.END)
        self.MEDE.config(fg='black')

    def handle_focus_out(self,_):
        self.nb.delete(0, tk.END)
        self.nb.config(fg='grey')
        self.nb.insert(0,"Enter Com Port Number")
    
    def handle_focus_out2(self,_):
        self.MEDE.delete(0,tk.END)
        self.MEDE.config(fg='grey')
        self.MEDE.insert(0,"Enter MED Number")

    def Input_MED(self):
        try:
            item = self.MEDE.get()
            self.MEDE.delete(0,tk.END)
            self.dummy.focus()
            item = int(item)
            if(item>440 or item<0):
                self.MEDE.config(fg="grey")
                self.nb.delete(0,tk.END)
                self.MEDE.insert(0,"Please Enter Valid MED Number")
                self.sb_update("Invalid MED Entered")
                self.sb_update("MED Must Be Less That 440")
                self.UMED.config(state=tk.DISABLED)

            else:
                if(0<=item<=150):
                    self.dt_fitzpatrick.config(text="Fitzpatrick Skin Type: Type 1")
                    self.dt_MED.config(text=("MED (in units of SED): "+ str(item)))
                    self.type = 1
                elif(150<item<=220):
                    self.dt_fitzpatrick.config(text="Fitzpatrick Skin Type: Type 2")
                    self.dt_MED.config(text=("MED (in units of SED): "+ str(item)))
                    self.type = 2
                elif(220<item<=290):
                    self.dt_fitzpatrick.config(text="Fitzpatrick Skin Type: Type 3")
                    self.dt_MED.config(text=("MED (in units of SED): "+ str(item)))
                    self.type = 3
                elif(290<item<=370):
                    self.dt_fitzpatrick.config(text="Fitzpatrick Skin Type: Type 4")
                    self.dt_MED.config(text=("MED (in units of SED): "+ str(item)))
                    self.type = 4
                else:
                    self.dt_fitzpatrick.config(text="Fitzpatrick Skin Type: Type 5/6")
                    self.dt_MED.config(text=("MED (in units of SED): "+ str(item)))
                    self.type = 7
                self.MED_Handle(item, self.type)
        except:
            self.MEDE.config(fg="grey")
            self.nb.delete(0,tk.END)
            self.sb_update("Please Enter Valid MED Number")
            self.MEDE.insert(0,"Please Enter Valid MED Number")
            self.sb_update("Invalid MED Entered")
            self.UMED.config(state=tk.DISABLED)

    def opts(self):
        self.of = tk.Frame(self.sf5, bg = "light grey", width=(self.x-8)/2, height=(self.y-60)/10)
        self.of.pack_propagate(0)
        self.of.pack(fill=tk.X)
        self.options = tk.Label(self.of, bg="Light Grey", text="Controls", font='TkHeadingFont 12', height=2)
        self.options.pack(fill=tk.BOTH)
        self.cbf = tk.Frame(self.sf5, bg = "light grey", width=(self.x-8)/2, height=((self.y-60)/10)*4)
        self.cbf.pack_propagate(0)
        self.cbf.pack(fill=tk.X)
        self.pserial = tk.Button(self.cbf, bg = "Light Grey", text = "Pause Serial", font='TkHeadingFont 10', command= lambda:self.spause_press(), height=2)
        self.pserial.pack(fill=tk.BOTH)
        self.ccb = tk.Button(self.cbf, bg = "light grey", command=lambda:self.sport_select(), text="Choose Com", height=2)
        self.ccb.pack(fill=tk.BOTH)
        self.ewf = tk.Frame(self.cbf, bg="light grey", height=((self.y-80)/10), width=(self.x-8)/2)
        self.ewf.pack_propagate(0)
        self.ewf.pack(fill=tk.BOTH)
        self.nb = tk.Entry(self.ewf, bg="white", fg='grey')
        self.nb.pack(fill=tk.BOTH)
        self.nb.place(height=((self.y-70)/10),width=(self.x-8)/2)
        self.nb.insert(0,"Enter Com Port Number")
        self.nb.bind("<FocusIn>", self.handle_focus_in)
        self.nb.bind("<FocusOut>", self.handle_focus_out)
        self.connect = tk.Button(self.cbf, bg = "Light Grey", text = "Connect", font='TkHeadingFont 10', height=2, command=lambda:self.main.set_port(), state=tk.DISABLED)
        self.connect.pack(fill=tk.BOTH)

    def MED_Setup(self):
        self.mmf = tk.Frame(self.sf3, bg="light grey", height=((self.y-60)/3), width=(self.x-8)/4)
        self.mmf.pack_propagate(0)
        self.mmf.pack(fill=tk.BOTH)
        self.MED = tk.Button(self.mmf, bg="light grey", text="Input MED", height=2, command=lambda:self.Input_MED())
        self.MED.pack(fill=tk.BOTH)
        self.ewf2 = tk.Frame(self.mmf, bg="light grey", height=((self.y-60)/10), width=(self.x-8)/2)
        self.ewf2.pack_propagate(0)
        self.ewf2.pack(fill=tk.BOTH)
        self.MEDE = tk.Entry(self.ewf2, bg="white", fg="grey")
        self.MEDE.pack(fill=tk.BOTH)
        self.MEDE.place(height=((self.y-60)/10), width=(self.x-8)/2)
        self.MEDE.insert(0,"Enter MED Number")
        self.MEDE.bind("<FocusIn>", self.handle_focus_in2)
        self.MEDE.bind("<FocusOut>", self.handle_focus_out2)
        self.UMED = tk.Button(self.mmf, bg="light grey", text="Upload MED", state=tk.DISABLED, height=2, command=lambda:self.MED_Upload())
        self.UMED.pack(fill=tk.BOTH)
        self.SR = tk.Button(self.mmf, bg="light grey", text="Reset SED", height=2, command=lambda:self.SED_Reset())
        self.SR.pack(fill=tk.BOTH)

    #def MED_Input(self):
        
        
        
