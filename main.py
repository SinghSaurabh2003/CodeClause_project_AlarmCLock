#Importing required Modules
import datetime
from tkinter.ttk import *
from time import strftime 
from tkinter import *
from threading import *
import time
from pydub import AudioSegment
from pydub.playback import play

#digital time clock on top of window
def times(): 
    st = strftime('%H:%M:%S ') 
    lbl.config(text = st) 
    lbl.after(1000, times) 

def Threading():
    t1=Thread(target=alarm)#invoking Alarm function
    t1.start()
#Function to play alarm if set alarm time and current time is equal it plays the sound 
def alarm():
    while True:
        SA=f'{hour.get()}:{minute.get()}:{second.get()}'
        CT=datetime.datetime.now().strftime("%H:%M:%S")
        if(CT==SA):
            songs=AudioSegment.from_mp3("song.mp3")
            play(songs)

# creating window    
window=Tk()
window.title("ALarm Clock")
window.geometry("600x500")
window.configure(bg="Red")
#adding top most Label
Label(window,text="My Alarm clock",font="impack 15 bold",bg="black",fg="white").pack(fill="x")
lbl=Label(window,font = ('impack',25, 'bold'), bg='red', fg='white')
lbl.pack(pady=5) 
#adding another label
Label(window,text="Set Alarm time",font="impack 20 bold",bg="red").pack(pady=20)
Label(window,text="Hour     Minute     Second",font="impack 9 bold",bg="red").pack(pady=10)
frame=Frame(window)
frame.pack()
hour=StringVar(window)
hours=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
hours.sort()
hrs=OptionMenu(frame,hour,*hours)
hrs.pack(side=LEFT)

minute=StringVar(window)
minutes=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22',
        '23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43'
        ,'44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60']
minutes.sort()
minu=OptionMenu(frame,minute,*minutes)
minu.pack(side=LEFT)

second=StringVar(window)
seconds=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22',
        '23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43'
        ,'44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60']
seconds.sort()
sec=OptionMenu(frame,second,*seconds)
sec.pack(side=LEFT)
#adding set alarm button
Button(window,text="Set alarm",command=Threading).pack(pady=40)
#invoking times function for digital display watch
times() 
mainloop()
