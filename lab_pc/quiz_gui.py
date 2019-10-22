import tkinter as tk

class QGUI:
    def __init__(self, master, gui, x, y, known_type):
        self.master = master
        self.gui = gui
        self.x = x
        self.y = y
        self.iteration = 1
        self.vlist = []
        self.scores = [1,2,3,4,5]
        self.vtotal = None
        self.lvalue = 0
        self.known_type = known_type
        self.mf()
        self.quiz_builder()

    def back(self):
        self.qf.destroy()
        self.iteration = self.iteration - 1
        self.vlist.pop(len(self.vlist)-1)
        self.update_value()
        self.quiz_builder()
    
    def close(self):
        self.gui.set_score(None, False)
        self.mff.destroy()
    
    def bpress(self, value):
        self.qf.destroy()
        self.iteration = self.iteration + 1
        self.vlist.append(value)
        self.update_value()
        if(self.iteration > len(self.qd.keys())):
            self.gui.set_score(self.vtotal, self.known_type)
            self.mff.destroy()
        else:
            self.quiz_builder()

    def update_value(self):
        self.vtotal = 0
        for num in self.vlist:
            self.vtotal = self.vtotal + num
    
    def mf(self):
        self.mff = tk.Frame(self.master, height=self.y, width=self.x, borderwidth=4, bg="black")
        self.mff.pack_propagate(0)
        self.mff.pack(fill=tk.BOTH)

        self.mftf = tk.Frame(self.mff, bg="light grey", height=40, width=self.x-8)
        self.mftf.pack_propagate(0)
        self.mftf.pack(fill=tk.BOTH)

        self.mftfg1 = tk.Frame(self.mftf, height=40, width=(self.x-8)/6, bg="red")
        self.mftfg1.grid_propagate(0)
        self.mftfg1.grid(column=0, row=0)
        self.mftfg2 = tk.Frame(self.mftf, height=40, width=(4*self.x-8)/6, bg="blue")
        self.mftfg2.grid_propagate(0)
        self.mftfg2.grid(column=1, row=0, columnspan = 4)
        self.mftfg3 = tk.Frame(self.mftf, height=40, width=(self.x-8)/6, bg="orange")
        self.mftfg3.grid_propagate(0)
        self.mftfg3.grid(column=5, row=0)

        self.mftfg2f = tk.Frame(self.mftfg2, height=40, width=(4*self.x-8)/6)
        self.mftfg2f.pack_propagate(0)
        self.mftfg2f.pack(fill=tk.BOTH)
        self.mftt = tk.Label(self.mftfg2f, text="Fitzpatrick Skin Type Quiz", bg="light grey", height=40, width=int((4*self.x-8)/6), font="TkTitleFont 10")
        self.mftt.pack(fill=tk.BOTH)

        self.mftfg1f = tk.Frame(self.mftfg1, height=40, width=((self.x-8)/6))
        self.mftfg1f.pack_propagate(0)
        self.mftfg1f.pack(fill=tk.BOTH)
        self.mftb1 = tk.Button(self.mftfg1f, height=40, width=int((self.x-8)/6), command=lambda:self.back(), text="Back", relief=tk.SUNKEN)
        self.mftb1.pack(fill=tk.BOTH)

        self.mftfg3f = tk.Frame(self.mftfg3, height=40, width=((self.x-8)/6))
        self.mftfg3f.pack_propagate(0)
        self.mftfg3f.pack(fill=tk.BOTH)
        self.mftb3 = tk.Button(self.mftfg3f, height=40, width=int((self.x-8)/6), command=lambda:self.close(), text="Close")
        self.mftb3.pack(fill=tk.BOTH)

        self.sf = tk.Frame(self.mff, bg="dark grey", width=(self.x-8), height=(self.y-40-8))
        self.sf.pack_propagate(0)
        self.sf.pack()

    def qcreater(self, master, qdict, iteration):
        qf = tk.Frame(master, height=self.y-40-8, width=self.x-8, bg="dark grey") 
        qf.pack_propagate(0)
        qf.pack()
        
        if(self.iteration > 1):
            self.mftb1.config(state=tk.ACTIVE, relief=tk.RAISED)
        else:
            self.mftb1.config(state=tk.DISABLED, relief=tk.SUNKEN)

        n = 1
        b = 1
        itlist = qdict[iteration]
        listlen = len(itlist[1]) + 1
        afl = []

        qftf = tk.Frame(qf, bg="grey", height=int((self.y-40-8)/listlen), width=self.x-8)
        qftf.pack_propagate(0)
        qftf.pack()
        qft = tk.Label(qftf, text=itlist[0], height=int((self.y-40-8)/listlen), font="TkHeadingFont 10")
        qft.pack(fill=tk.BOTH)   

        for ans in itlist[1]:
            af = tk.Frame(qf, bg="light grey", height=int((self.y-40-8)/listlen), width=self.x-8)
            afl.append(af)

            if(n == 1):
                afb = tk.Button(afl[b-1], bg="white", text=ans, command=lambda:self.bpress(0), height=int((self.y-40-8)/listlen))
            elif(n == 2):
                afb = tk.Button(afl[b-1], bg="white", text=ans, command=lambda:self.bpress(1), height=int((self.y-40-8)/listlen))
            elif(n == 3):
                afb = tk.Button(afl[b-1], bg="white", text=ans, command=lambda:self.bpress(2), height=int((self.y-40-8)/listlen))
            elif(n == 4):
                afb = tk.Button(afl[b-1], bg="white", text=ans, command=lambda:self.bpress(3), height=int((self.y-40-8)/listlen))
            elif(n == 5):
                afb = tk.Button(afl[b-1], bg="white", text=ans, command=lambda:self.bpress(4), height=int((self.y-40-8)/listlen))
            elif(n == 6):
                afb = tk.Button(afl[b-1], bg="white", text=ans, command=lambda:self.bpress(5), height=int((self.y-40-8)/listlen))
            else:
                afb = tk.Button(afl[b-1],bg="white",text=ans, command=lambda:print("Error - Quiz Failure Reload"))
            afl.append(afb)
            n = n + 1
            b = b + 2
        m=0

        for item in afl:
            if(m%2==0):
                item.pack_propagate(0)
                item.pack()
            else:
                item.pack(fill=tk.BOTH)
            m = m + 1

    def quiz_builder(self):
        self.qf = tk.Frame(self.sf, bg="dark grey", width=(self.x-8), height=(self.y-40-8))
        self.qf.pack_propagate(0)
        self.qf.pack(fill=tk.BOTH)
        

        if(self.known_type):
            self.qd = {
                1:("What Skin Type Are You?",("Type 1 (0-6 score)","Type 2 (7-13 score)","Type 3 (14-20 score)","Type 4 (21-27 score)","Type 5 (28-34 score)","Type 6 (35+)"))
            }
        else:
            self.qd = {
            1:("What colour are your eyes?",("Light Blue, Green or Grey","Blue, Green or Grey", "Dark Blue, Green, or Light Brown","Dark Brown","Brownish Black")),
            2:("What is your natural hair colour?",("Red","Blonde","Chestnut or Dark Blonde","Dark Brown","Black")),
            3:("What colour is your skin?",("Pink","Very Pale","Light Brown or Olive","Brown","Dark Brown")),
            4:("Do you have freckles on unexposed areas?",("Many","Several","Few","Rare","None")),
            5:("What happens when you stay in the sun too long?",("Severe Burns, Blistering, Peeling","Mild Burns, Blistering, Peeling","Sometimes Burns followed by Peeling","Rare Burns","No Burns")),
            6:("Do you brown after sun exposure?",("Never","Rarely","Sometimes","Often","Always")),
            7:("How Brown do you get?",("Hardly or Not at all","Light Tan","Medium Tan","Dark Tan","Very Dark Tan")),
            8:("Is your face sentitive to sun?",("Very Sensitive","Sensitive","Mildly Sensitive","Resistant","Very Resistant")),
            9:("How often do you tan?",("Never","Rarely","Sometimes","Often","Always")),
            10:("When did you last use arteficial tanning (tanning beds)",("More than 3 months ago","In the last 2-3 months","In the last 1-2 months","In the last week","In the last day"))
            }
        self.qcreater(self.qf, self.qd, self.iteration)