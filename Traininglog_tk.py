#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright 2019, Axel Zedigh, All rights reserved.
import time, csv, sys,string#, PIL.Image, PIL.ImageTk

def version():
    """Kolla vilken version av Python vi har"""
    import sys
    datatyp = type(sys.version_info)
    if datatyp == type(()):
        version = sys.version_info[0]
    else:
        version = sys.version_info.major
    return version

if version() == 3:
    from tkinter import *
else:
    from Tkinter import *

class T_Bok():

	def __init__(self):#,dateE,weekE,dayE,sTimeE,morningHRE,weightE,eTimeE,sleepE,warmupE,wDurationE,trainingProgE,tDurationE,t1E,t1set1E,t1set2E,t1set3E,t1set4E,t1set5E,t2E,t2set1E,t2set2E,t2set3E,t2set4E,t2set5E,t3E,t3set1E,t3set2E,t3set3E,t3set4E,t3set5E,t4E,t4set1E,t4set2E,t4set3E,t4set4E,t4set5E,t5E,t5set1E,t5set2E,t5set3E,t5set4E,t5set5E,t6E,t6set1E,t6set2E,t6set3E,t6set4E,t6set5E,t7E,t7set1E,t7set2E,t7set3E,t7set4E,t7set5E,t8E,t8set1E,t8set2E,t8set3E,t8set4E,t8set5E,t9E,t9set1E,t9set2E,t9set3E,t9set4E,t9set5E,t10E,t10set1E,t10set2E,t10set3E,t10set4E,t10set5E,otherE,oDurationE,distanceE,speedE,HRIE,coolDownE,cDurationE,sDurationE,sE1,sE1sec1E,sE1sec2E,sE2,sE2sec1E,sE2sec2E,commentsE):
		pass
		#self.dateE = dateE
		#self.weekE = weekE
		#self.dayE = dayE
		#self.sTimeE = sTimeE
		#self.morningHRE = morningHRE
		#self.weightE = weightE
		#self.eTimeE = eTimeE
		#self.sleepE = sleepE
		#self.warmupE = warmupE
		#self.wDurationE = wDurationE
		#self.trainingProgE = trainingProgE
		#self.tDurationE = tDurationE
		#self.t1E = t1E
		#self.t1set1E = t1set1E
		#self.t1set2E = t1set2E
		#self.t1set3E = t1set3E
		#self.t1set4E = t1set4E
		#self.t1set5E = t1set5E
		#self.t2E = t2E
		#self.t2set1E = t2set1E
		#self.t2set2E = t2set2E
		#self.t2set3E = t2set3E
		#self.t2set4E = t2set4E
		#self.t2set5E = t2set5E
		#self.t3E = t3E
		#self.t3set1E = t3set1E
		#self.t3set2E = t3set2E
		#self.t3set3E = t3set3E
		#self.t3set4E = t3set4E
		#self.t3set5E = t3set5E
		#self.t4E = t4E
		#self.t4set1E = t4set1E
		#self.t4set2E = t4set2E
		#self.t4set3E = t4set3E
		#self.t4set4E = t4set4E
		#self.t4set5E = t4set5E
		#self.t5E = t5E
		#self.t5set1E = t5set1E
		#self.t5set2E = t5set2E
		#self.t5set3E = t5set3E
		#self.t5set4E = t5set4E
		#self.t5set5E = t5set5E
		#self.t6E = t6E
		#self.t6set1E = t6set1E
		#self.t6set2E = t6set2E
		#self.t6set3E = t6set3E
		#self.t6set4E = t6set4E
		#self.t6set5E = t6set5E
		#self.t7E = t7E
		#self.t7set1E = t7set1E
		#self.t7set2E = t7set2E
		#self.t7set3E = t7set3E
		#self.t7set4E = t7set4E
		#self.t7set5E = t7set5E
		#self.t8E = t8E
		#self.t8set1E = t8set1E
		#self.t8set2E = t8set2E
		#self.t8set3E = t8set3E
		#self.t8set4E = t8set4E
		#self.t8set5E = t8set5E
		#self.t9E = t9E
		#self.t9set1E = t9set1E
		#self.t9set2E = t9set2E
		#self.t9set3E = t9set3E
		#self.t9set4E = t9set4E
		#self.t9set5E = t9set5E
		#self.t10E = t10E
		#self.t10set1E = t10set1E
		#self.t10set2E = t10set2E
		#self.t10set3E = t10set3E
		#self.t10set4E = t10set4E
		#self.t10set5E = t10set5E
		#self.otherE = otherE
		#self.oDurationE = oDurationE
		#self.distanceE = distanceE
		#self.speedE = speedE
		#self.HRIE = HRIE
		#self.coolDownE = coolDownE
		#self.cDurationE = cDurationE
		#self.sDurationE = sDurationE
		#self.sE1 = sE1
		#self.sE1sec1E = sE1sec1E
		#self.sE1sec2E = sE1sec2E
		#self.sE2 = sE2
		#self.sE2sec1E = sE2sec1E
		#self.sE2sec2E = sE2sec2E
		#self.commentsE = commentsE

def main():
	master = Tk()
	#master.attributes("-alpha", 0.4)
	x = 1
	color = "#ffaa7c"
	master.title("Träningsbok v1.0 (by Axel Zedigh)")
	Cframe = Frame(master, bg=color, padx=40)
	Cframe.pack(side = LEFT)
	#Rframe = Frame(master, bg=color, width=400)
	#Rframe.pack(side=RIGHT)
	

	#bild1 = PIL.Image.open("enter_the_dragon_poster_001.jpg")
	#bild2 = PIL.ImageTk.PhotoImage(bild1)
	#bakBild = Label(Cframe,image=bild2)
	#bakBild.place(x=0, y=0, relwidth=1, relheight=1)

	#timeinfo
	tObj = time.localtime()
	yr = tObj[0]
	mon = tObj[1]
	day = tObj[2]
	#Lägga till 0:a framför 
	if yr//10 ==0: yr = str("0")+str(yr)
	else: yr = str(yr)
	if mon//10 ==0: mon = str("0")+str(mon)
	else: mon = str(mon)
	if day//10 ==0: day = str("0")+str(day)
	else: day = str(day)
	todayDate = str(yr[2:]+mon+day)

	#infoFrame
	infoFrame = Frame(Cframe, bg=color, pady=10,width=(25))

	infoLabel = Label(infoFrame, text="", fg="red",bd=4)
	infoLabel.grid(row=2, column=4, columnspan=2,  sticky="wens")
	
	dateLabel = Label(infoFrame, text="Date:").grid(row=0, column=0, sticky="wens")
	dateE = Entry(infoFrame, width=6)
	dateE.grid(row=0, column=1, sticky="w")
	dateE.focus()
	dateE.bind("<Enter>",lambda: infoLabel.configure(text="EJ sparad!", fg="red"))
	dateE.insert(1,todayDate)

	weekLabel = Label(infoFrame, text="Week:").grid(row=0, column=2, sticky="wens")
	weekE = Entry(infoFrame, width=3)
	weekE.grid(row=0, column=3, sticky="w")

	dayLabel = Label(infoFrame, text="Day:").grid(row=0, column=4, sticky="wens")
	dayE = Entry(infoFrame, width=7)
	dayE.grid(row=0, column=5, sticky="w")

	sTimeLabel = Label(infoFrame, text="Start Time:").grid(row=1, column=0, sticky="wens")
	sTimeE = Entry(infoFrame, width=6)
	sTimeE.grid(row=1, column=1, sticky="w")

	morningHRLabel = Label(infoFrame, text="Morning HR:").grid(row=1, column=2, sticky="wens")
	morningHRE = Entry(infoFrame, width=3)
	morningHRE.grid(row=1, column=3, sticky="w")

	weightLabel = Label(infoFrame, text="Weight(kg):").grid(row=1, column=4, sticky="wens")
	weightE = Entry(infoFrame, width=7)
	weightE.grid(row=1, column=5, sticky="w")

	eTimeLabel = Label(infoFrame, text="End Time:").grid(row=2, column=0, sticky="wens")
	eTimeE = Entry(infoFrame, width=6)
	eTimeE.grid(row=2, column=1, sticky="w")

	sleepLabel = Label(infoFrame, text="Sleep(1-10):").grid(row=2, column=2, sticky="wens")
	sleepE = Entry(infoFrame, width=3)
	sleepE.grid(row=2, column=3, sticky="w")

	infoFrame.pack(fill=X)

	#warmupFrame
	warmupFrame = Frame(Cframe, bg = color,width=(25), pady=10)
	warmupLabel = Label(warmupFrame, text="Warmup:").grid(row=0, column=0, sticky="wens")
	warmupE = Entry(warmupFrame, width=18)
	warmupE.grid(row=0, column=1, sticky="w")

	wDurationLabel = Label(warmupFrame, text="Duration(min):").grid(row=0, column=2, sticky="wens")
	wDurationE = Entry(warmupFrame, width=3)
	wDurationE.grid(row=0, column=3, sticky="w")

	trainingProgLabel = Label(warmupFrame, text="Training Program:").grid(row=1,column=0, sticky="wens")
	trainingProgE = Entry(warmupFrame, width=18)
	trainingProgE.grid(row=1,column=1, sticky="w")

	tDurationLabel = Label(warmupFrame, text="Duration(min):").grid(row=1,column=2, sticky="wens")
	tDurationE = Entry(warmupFrame, width=3)
	tDurationE.grid(row=1,column=3, sticky="w")

	warmupFrame.pack(fill=X)

	#trainingProgFrame
	trainingProgFrame = Frame(Cframe, bg=color, width=(25), pady=10)

	tExerciseLabel = Label(trainingProgFrame, text="Exercise").grid(row=1,column=0, sticky="wens")
	kgrep1Label = Label(trainingProgFrame, text="kg/rep").grid(row=1,column=1, sticky="wens")
	kgrep2Label = Label(trainingProgFrame, text="kg/rep").grid(row=1,column=2, sticky="wens")
	kgrep3Label = Label(trainingProgFrame, text="kg/rep").grid(row=1,column=3, sticky="wens")
	kgrep4Label = Label(trainingProgFrame, text="kg/rep").grid(row=1,column=4, sticky="wens")
	kgrep5Label = Label(trainingProgFrame, text="kg/rep").grid(row=1,column=5, sticky="wens")

	#for i in range(10):
	#	
	#	for j in range(5):


	t1E = Entry(trainingProgFrame, width=15);t1E.grid(row=2,column=0)
	t1set1E = Entry(trainingProgFrame, width=5);t1set1E.grid(row=2,column=1)
	t1set2E = Entry(trainingProgFrame, width=5);t1set2E.grid(row=2,column=2)
	t1set3E = Entry(trainingProgFrame, width=5);t1set3E.grid(row=2,column=3)
	t1set4E = Entry(trainingProgFrame, width=5);t1set4E.grid(row=2,column=4)
	t1set5E = Entry(trainingProgFrame, width=5);t1set5E.grid(row=2,column=5)

	t2E = Entry(trainingProgFrame, width=15);t2E.grid(row=3,column=0)
	t2set1E = Entry(trainingProgFrame, width=5);t2set1E.grid(row=3,column=1)
	t2set2E = Entry(trainingProgFrame, width=5);t2set2E.grid(row=3,column=2)
	t2set3E = Entry(trainingProgFrame, width=5);t2set3E.grid(row=3,column=3)
	t2set4E = Entry(trainingProgFrame, width=5);t2set4E.grid(row=3,column=4)
	t2set5E = Entry(trainingProgFrame, width=5);t2set5E.grid(row=3,column=5)

	t3E = Entry(trainingProgFrame, width=15);t3E.grid(row=4,column=0)
	t3set1E = Entry(trainingProgFrame, width=5);t3set1E.grid(row=4,column=1)
	t3set2E = Entry(trainingProgFrame, width=5);t3set2E.grid(row=4,column=2)
	t3set3E = Entry(trainingProgFrame, width=5);t3set3E.grid(row=4,column=3)
	t3set4E = Entry(trainingProgFrame, width=5);t3set4E.grid(row=4,column=4)
	t3set5E = Entry(trainingProgFrame, width=5);t3set5E.grid(row=4,column=5)

	t4E = Entry(trainingProgFrame, width=15);t4E.grid(row=5,column=0)
	t4set1E = Entry(trainingProgFrame, width=5);t4set1E.grid(row=5,column=1)
	t4set2E = Entry(trainingProgFrame, width=5);t4set2E.grid(row=5,column=2)
	t4set3E = Entry(trainingProgFrame, width=5);t4set3E.grid(row=5,column=3)
	t4set4E = Entry(trainingProgFrame, width=5);t4set4E.grid(row=5,column=4)
	t4set5E = Entry(trainingProgFrame, width=5);t4set5E.grid(row=5,column=5)

	t5E = Entry(trainingProgFrame, width=15);t5E.grid(row=6,column=0)
	t5set1E = Entry(trainingProgFrame, width=5);t5set1E.grid(row=6,column=1)
	t5set2E = Entry(trainingProgFrame, width=5);t5set2E.grid(row=6,column=2)
	t5set3E = Entry(trainingProgFrame, width=5);t5set3E.grid(row=6,column=3)
	t5set4E = Entry(trainingProgFrame, width=5);t5set4E.grid(row=6,column=4)
	t5set5E = Entry(trainingProgFrame, width=5);t5set5E.grid(row=6,column=5)

	t6E = Entry(trainingProgFrame, width=15);t6E.grid(row=7,column=0)
	t6set1E = Entry(trainingProgFrame, width=5);t6set1E.grid(row=7,column=1)
	t6set2E = Entry(trainingProgFrame, width=5);t6set2E.grid(row=7,column=2)
	t6set3E = Entry(trainingProgFrame, width=5);t6set3E.grid(row=7,column=3)
	t6set4E = Entry(trainingProgFrame, width=5);t6set4E.grid(row=7,column=4)
	t6set5E = Entry(trainingProgFrame, width=5);t6set5E.grid(row=7,column=5)

	t7E = Entry(trainingProgFrame, width=15);t7E.grid(row=8,column=0)
	t7set1E = Entry(trainingProgFrame, width=5);t7set1E.grid(row=8,column=1)
	t7set2E = Entry(trainingProgFrame, width=5);t7set2E.grid(row=8,column=2)
	t7set3E = Entry(trainingProgFrame, width=5);t7set3E.grid(row=8,column=3)
	t7set4E = Entry(trainingProgFrame, width=5);t7set4E.grid(row=8,column=4)
	t7set5E = Entry(trainingProgFrame, width=5);t7set5E.grid(row=8,column=5)

	t8E = Entry(trainingProgFrame, width=15);t8E.grid(row=9,column=0)
	t8set1E = Entry(trainingProgFrame, width=5);t8set1E.grid(row=9,column=1)
	t8set2E = Entry(trainingProgFrame, width=5);t8set2E.grid(row=9,column=2)
	t8set3E = Entry(trainingProgFrame, width=5);t8set3E.grid(row=9,column=3)
	t8set4E = Entry(trainingProgFrame, width=5);t8set4E.grid(row=9,column=4)
	t8set5E = Entry(trainingProgFrame, width=5);t8set5E.grid(row=9,column=5)

	t9E = Entry(trainingProgFrame, width=15);t9E.grid(row=10,column=0)
	t9set1E = Entry(trainingProgFrame, width=5);t9set1E.grid(row=10,column=1)
	t9set2E = Entry(trainingProgFrame, width=5);t9set2E.grid(row=10,column=2)
	t9set3E = Entry(trainingProgFrame, width=5);t9set3E.grid(row=10,column=3)
	t9set4E = Entry(trainingProgFrame, width=5);t9set4E.grid(row=10,column=4)
	t9set5E = Entry(trainingProgFrame, width=5);t9set5E.grid(row=10,column=5)

	t10E = Entry(trainingProgFrame, width=15);t10E.grid(row=11,column=0)
	t10set1E = Entry(trainingProgFrame, width=5);t10set1E.grid(row=11,column=1)
	t10set2E = Entry(trainingProgFrame, width=5);t10set2E.grid(row=11,column=2)
	t10set3E = Entry(trainingProgFrame, width=5);t10set3E.grid(row=11,column=3)
	t10set4E = Entry(trainingProgFrame, width=5);t10set4E.grid(row=11,column=4)
	t10set5E = Entry(trainingProgFrame, width=5);t10set5E.grid(row=11,column=5)

	trainingProgFrame.pack(fill=X)

	#otherFrame
	otherFrame = Frame(Cframe, bg=color, width=(25), pady=10)
	otherLabel = Label(otherFrame, text="Other activity:").grid(row=0,column=0, sticky="wens")
	otherE = Entry(otherFrame, width=11);otherE.grid(row=0,column=1)
	oDurationLabel = Label(otherFrame, text="Duration:").grid(row=0,column=2, sticky="wens")
	oDurationE = Entry(otherFrame, width=3);oDurationE.grid(row=0,column=3)
	distanceLabel = Label(otherFrame, text="Distance(km):").grid(row=1,column=0, sticky="wens")
	distanceE = Entry(otherFrame, width=11);distanceE.grid(row=1,column=1)
	speedLabel = Label(otherFrame, text="Speed(km/h):").grid(row=1,column=2, sticky="wens")
	speedE = Entry(otherFrame, width=3);speedE.grid(row=1,column=3)
	HRILabel = Label(otherFrame, text="HR/I:").grid(row=1,column=4, sticky="wens")
	HRIE = Entry(otherFrame, width=3);HRIE.grid(row=1,column=5)
	cooldownFrame = Frame(Cframe, bg=color, width=(25*x), pady=10)
	coolDownLabel = Label(otherFrame, text="Cool down:").grid(row=2,column=0, sticky="wens")
	coolDownE = Entry(otherFrame, width=11);coolDownE.grid(row=2,column=1)
	cDurationLabel = Label(otherFrame, text="Duration:").grid(row=2,column=2, sticky="wens")
	cDurationE = Entry(otherFrame, width=3);cDurationE.grid(row=2,column=3)
	stretchDurationLabel = Label(otherFrame, text="Stretch Duration:").grid(row=3,column=0, sticky="wens")
	sDurationE = Entry(otherFrame, width=3);sDurationE.grid(row=3,column=1, sticky="wens")
	#GridPads
	padRow0 = Label(otherFrame).grid(row=0,column=4,columnspan=2,sticky="wens")
	padRow2 = Label(otherFrame).grid(row=2,column=4,columnspan=2,sticky="wens")
	padRow3 = Label(otherFrame).grid(row=3,column=2,columnspan=4,sticky="wens")
	otherFrame.pack(fill=X)

	#stretchFrame
	stretchFrame = Frame(Cframe, bg=color, width=(25), pady=10)
	sE1Label = Label(stretchFrame, text="Exercise").grid(row=1,column=0, sticky="wens")
	sE1sec1Label = Label(stretchFrame, text="sec").grid(row=1,column=1, sticky="wens")
	sE1ec2Label = Label(stretchFrame, text="sec").grid(row=1,column=2, sticky="wens")
	sE2Label = Label(stretchFrame, text="Exercise").grid(row=1,column=3, sticky="wens")
	sE2sec1Label = Label(stretchFrame, text="sec").grid(row=1,column=4, sticky="wens")
	sE2sec2Label = Label(stretchFrame, text="sec").grid(row=1,column=5, sticky="wens")

	sE1 = Entry(stretchFrame, width=14);sE1.grid(row=2,column=0)
	sE1sec1E = Entry(stretchFrame, width=3);sE1sec1E.grid(row=2,column=1)
	sE1sec2E = Entry(stretchFrame, width=3);sE1sec2E.grid(row=2,column=2)
	sE2 = Entry(stretchFrame, width=14);sE2.grid(row=2,column=3)
	sE2sec1E = Entry(stretchFrame, width=3);sE2sec1E.grid(row=2,column=4)
	sE2sec2E = Entry(stretchFrame, width=3);sE2sec2E.grid(row=2,column=5)
	stretchFrame.pack(fill=X)

	#commentsFrame
	commentsFrame = Frame(Cframe, bg=color, width=(25), pady=10)
	commentsLabel = Label(commentsFrame, text="Comments:");commentsLabel.grid(row=0,column=0, sticky="wens")
	commentsE = Entry(commentsFrame, width=20);commentsE.grid(row=0,column=1, sticky="w")
	
	Entries = [dateE,weekE,dayE,sTimeE,morningHRE,weightE,eTimeE,sleepE,warmupE,wDurationE,trainingProgE,tDurationE,t1E,t1set1E,t1set2E,t1set3E,t1set4E,t1set5E,t2E,t2set1E,t2set2E,t2set3E,t2set4E,t2set5E,t3E,t3set1E,t3set2E,t3set3E,t3set4E,t3set5E,t4E,t4set1E,t4set2E,t4set3E,t4set4E,t4set5E,t5E,t5set1E,t5set2E,t5set3E,t5set4E,t5set5E,t6E,t6set1E,t6set2E,t6set3E,t6set4E,t6set5E,t7E,t7set1E,t7set2E,t7set3E,t7set4E,t7set5E,t8E,t8set1E,t8set2E,t8set3E,t8set4E,t8set5E,t9E,t9set1E,t9set2E,t9set3E,t9set4E,t9set5E,t10E,t10set1E,t10set2E,t10set3E,t10set4E,t10set5E,otherE,oDurationE,distanceE,speedE,HRIE,coolDownE,cDurationE,sDurationE,sE1,sE1sec1E,sE1sec2E,sE2,sE2sec1E,sE2sec2E,commentsE]
	
	saveButton = Button(commentsFrame,text="Save",command=lambda: opensavefile(Entries, todayDate),cursor="trek")#, bitmap="gray12")
	saveButton.grid(row=0,column=3,sticky="e")
	clearButton = Button(commentsFrame,text="Clear",command=lambda: clearAll(Entries))
	clearButton.grid(row=0,column=4,sticky="e")
	quitButton = Button(commentsFrame,text="Quit",command=lambda: close_window(master, Entries))
	quitButton.grid(row=0,column=5,sticky="e")
	commentsFrame.pack(fill=X)

	#canvasFrame = Canvas(Rframe, bg=color)
	#canvasFrame.grid(row=0,column=0)
	##arc = canvasFrame.create_arc(0,100,200,200, width=4, activedash=2)
	#rec = canvasFrame.create_rectangle(0,0,100,100, width=2, activedash=2)
	#poly = canvasFrame.create_polygon(0,100,200,200,10,40, width=2, activefill="yellow", fill="")

	master.mainloop()

def noSaveInfo(infoLabel):
	infoLabel.configure(text="EJ sparad!", fg="red")

def close_window(root, Entries):
	#global j
	#j = callback(Entries)
	#print(j)
	root.destroy()

def clearAll(listOfEntries):
	for i in listOfEntries:
		info = i.delete(0,END)

def callback(listOfEntries):
	storedEntries = []
	for i in listOfEntries:
		info = i.get()
		storedEntries.append(info)
	#print(storedEntries)
	return storedEntries

def saveFile(storedEntries):
	try:
		#opensavefile(storedEntries)
		pass
	except:
		#createsavefile(storedEntries)
		pass

def opensavefile(storedEntries, date):
	#with open("log.csv") as fil:
	if getattr(sys,'frozen', False):
		fil = open(os.path.join(sys._MEIPASS,"log.csv"))
	else:
		fil = open("log.csv")
	filreader = csv.reader(fil)

	#Kollar om datumet är i ok format
	daterow = []
	k = callback(storedEntries)
	for i in k:
		i = i.encode('utf-8')
	M = ["0","1"]; D = ["0","1","2","3"]
	if len(k[0]) != 6:
		print("Bad length, should be YYMMDD!")
		return
	if str(k[0][2:3]) not in M:
		print("Bad monthdate, should be YYMMDD!")
		return
	if str(k[0][4:5]) not in D:
		print("Bad daydate, should be YYMMDD!")
		return
	#Kolla om datumet finns sen tidigare (*ersätt entryt om möjligt)
	for row in filreader:
		daterow.append(row[0])
	if k[0] in daterow:
		print("Datumet "+k[0]+" finns redan i loggen!")
		#infoLabel.configure(text=("Datum "+str(k[0]+"finns redan!")), fg="red")
		#time.sleep(3)
		#infoLabel.configure(text=(""), fg="red")
		return
	fil.close()
	#Lägg till entry i loggen
	if getattr(sys,'frozen', False):
		fil = open(os.path.join(sys._MEIPASS,"log.csv"), "a")
	else:
		fil = open("log.csv", "a")
	writer = csv.writer(fil)
	writer.writerow(k)
	print("Saved!")
	fil.close()
	#Backup på loggen
	if getattr(sys,'frozen', False):
		fil = open(os.path.join(sys._MEIPASS,"logbk.csv"), "a")
	else:
		fil = open("logbk.csv", "a")
	writer = csv.writer(fil)
	writer.writerow(callback(storedEntries))
	fil.close()

def show_list_of_exercises():
	Entries = ["dateE","weekE","dayE","sTimeE","morningHRE","weightE","eTimeE","sleepE","warmupE","wDurationE","trainingProgE","tDurationE","t1E","t1set1E","t1set2E","t1set3E","t1set4E","t1set5E","t2E","t2set1E","t2set2E","t2set3E","t2set4E","t2set5E","t3E","t3set1E","t3set2E","t3set3E","t3set4E","t3set5E","t4E","t4set1E","t4set2E","t4set3E","t4set4E","t4set5E","t5E","t5set1E","t5set2E","t5set3E","t5set4E","t5set5E","t6E","t6set1E","t6set2E","t6set3E","t6set4E","t6set5E","t7E","t7set1E","t7set2E","t7set3E","t7set4E","t7set5E","t8E","t8set1E","t8set2E","t8set3E","t8set4E","t8set5E","t9E","t9set1E","t9set2E","t9set3E","t9set4E","t9set5E","t10E","t10set1E","t10set2E","t10set3E","t10set4E","t10set5E","otherE","oDurationE","distanceE","speedE","HRIE","coolDownE","cDurationE","sDurationE","sE1","sE1sec1E","sE1sec2E","sE2","sE2sec1E","sE2sec2E","commentsE"]
	if getattr(sys,'frozen', False):
		fil = open(os.path.join(sys._MEIPASS,"log.csv"))
	else:
		fil = open("log.csv")
	filreader = csv.reader(fil)
	#Skapa lista med bokobjekt
	i=0
	objlist = []
	for row in filreader:
		s = T_Bok()
		if i == 0:
			i+=1
			continue
		j=0
		for y in Entries:
			setattr(s,y,row[j])
			j+=1
		objlist.append(s)
	#Skapa lista med olika exercises
	exercises = []
	nr = range(1,11)
	for s in objlist:
		for n in nr:
			f = ("t"+str(n)+"E")
			if getattr(s,f) not in exercises:
				if getattr(s,f) != "":
					exercises.append(getattr(s,f).lower())
	#print(exercises)
	#Skapa lista med övningar och hur många gånger de förekommer
	nyElist = []; besokta = []
	for h in exercises:
		i = 0; 
		if h not in besokta:
			for k in exercises:
				if h ==k:
					i+=1
			besokta.append(h)
			nyElist.append((i,h))
	for u in nyElist:
		print(u)
	return nyElist


def createsavefile(storedEntries):
	pass

if __name__ == "__main__":
	#show_list_of_exercises()
	main()