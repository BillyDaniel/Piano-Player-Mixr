from Tkinter import *
from pyaudio import *
from wave import *
from sys import *

import winsound


window = Tk()
#List that sounds will be appended too
Beats = []

#Play Functions
def Play1(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\Snare and Kick.wav', winsound.SND_FILENAME)
def Play2(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-c.wav', winsound.SND_FILENAME)
def Play3(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\Piano C.wav', winsound.SND_FILENAME)
def Play4(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-d.wav', winsound.SND_FILENAME)
def Play5(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-e.wav', winsound.SND_FILENAME)
def Play6(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-eb.wav', winsound.SND_FILENAME)
def Play7(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-f.wav', winsound.SND_FILENAME)
def Play8(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\Piano F.wav', winsound.SND_FILENAME)
def Play9(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-g.wav', winsound.SND_FILENAME)
def Play10(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\Piano G.wav', winsound.SND_FILENAME)
def Play11(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-a.wav', winsound.SND_FILENAME)
def Play12(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-b.wav', winsound.SND_FILENAME)
def Play13(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-bb.wav', winsound.SND_FILENAME)

#Functions for appending
def Bind1(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\Snare and Kick.wav')
def Bind2(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-c.wav')
def Bind3(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\Piano C.wav')
def Bind4(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-d.wav')
def Bind5(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-e.wav')
def Bind6(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-eb.wav')
def Bind7(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-f.wav')
def Bind8(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\Piano F.wav')
def Bind9(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-g.wav')
def Bind10(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\Piano G.wav')
def Bind11(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-a.wav')
def Bind12(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-b.wav')
def Bind13(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-bb.wav')

#Play Function and Loop function
def Loop(event):
    #for x in range(0,4):
        for player in Beats:
            winsound.PlaySound(player,winsound.SND_FILENAME)
#Clear function to make a different combination
def Clear(event):
    del Beats[:]

play = winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\Snare and Kick.wav', winsound.SND_FILENAME)


#window.geometry("1000x600")
#Frames for Spacing Grid
a=Frame(width=20, height=20)
b=Frame(width=20, height=20)
c=Frame(width=20, height=20)
d=Frame(width=20, height=20)
e=Frame(width=20, height=20)
f=Frame(width=20, height=20)
g=Frame(width=20, height=20)
h=Frame(width=20, height=20)
i=Frame(width=20, height=20)
j=Frame(width=20, height=20)
k=Frame(width=20, height=20)
l=Frame(width=20, height=20)
m=Frame(width=20, height=20)
n=Frame(width=20, height=20)
o=Frame(width=20, height=20)
p=Frame(width=20, height=20)
q=Frame(width=20, height=20)
r=Frame(width=20, height=20)
s=Frame(width=20, height=20)
t=Frame(width=20, height=20)
u=Frame(width=20, height=20)

#Declaring Buttons
button1=Button(window,text= "13",  fg="navy blue")
button2=Button(window,text= "Piano c", fg="navy blue")
button3=Button(window,text= "Piano C", fg="navy blue")
button4=Button(window,text= "Piano d", fg="navy blue")
button5=Button(window,text= "Piano e", fg="navy blue")
button6=Button(window,text= "Piano eb", fg="navy blue")
button7=Button(window,text= "Piano F", fg="navy blue")
button8=Button(window,text= "Piano f", fg="navy blue")
button9=Button(window,text= "Piano g", fg="navy blue")
button10=Button(window,text= "Piano G", fg="navy blue")
button11=Button(window,text= "Piano a", fg="navy blue")
button12=Button(window,text= "Piano b", fg="navy blue")
button13=Button(window,text= "Piano bb", fg="navy blue")
button14=Button(window,text= "Play", fg="navy blue")
button15=Button(window,text= "Clear", fg = "navy blue")

#binding Left Click to play sounds
button1.bind("<Button-1>",Play1)
button2.bind("<Button-1>",Play2)
button3.bind("<Button-1>",Play3)
button4.bind("<Button-1>",Play4)
button5.bind("<Button-1>",Play5)
button6.bind("<Button-1>",Play6)
button7.bind("<Button-1>",Play7)
button8.bind("<Button-1>",Play8)
button9.bind("<Button-1>",Play9)
button10.bind("<Button-1>",Play10)
button11.bind("<Button-1>",Play11)
button12.bind("<Button-1>",Play12)
button13.bind("<Button-1>",Play13)

#binding right click to create a loop
button1.bind("<Button-3>",Bind1)
button2.bind("<Button-3>",Bind2)
button3.bind("<Button-3>",Bind3)
button4.bind("<Button-3>",Bind4)
button5.bind("<Button-3>",Bind5)
button6.bind("<Button-3>",Bind6)
button7.bind("<Button-3>",Bind7)
button8.bind("<Button-3>",Bind8)
button9.bind("<Button-3>",Bind9)
button10.bind("<Button-3>",Bind10)
button11.bind("<Button-3>",Bind11)
button12.bind("<Button-3>",Bind12)
button13.bind("<Button-3>",Bind13)


button14.bind("<Button-1>",Loop)
button15.bind("<Button-1>",Clear)

#Laying out the grid
button2.grid(row=0, column=0)
a.grid(row=0,column=1)
button3.grid(row=0, column=2)
b.grid(row=1,column=0)
button4.grid(row=2,column=0)
c.grid(row=1, column=1)
button5.grid(row=2, column=2)
d.grid(row=3,column=0)
button6.grid(row=4,column=0)
e.grid(row=3,column=1)
button7.grid(row=4,column=2)
f.grid(row=5,column=0)
button8.grid(row=6,column=0)
g.grid(row=5,column=1)
button9.grid(row=6,column=2)
h.grid(row=7,column=0)
button10.grid(row=8,column=0)
i.grid(row=7,column=1)
button11.grid(row=8,column=2)
j.grid(row=9,column=0)
button12.grid(row=10,column=0)
k.grid(row=9,column=1)
button13.grid(row=10,column=2)
l.grid(row=11,column=0)
m.grid(row=11,column=2)
button14.grid(row=12,column=1)
n.grid(row=13,column=0)
o.grid(row=13,column=2)
button15.grid(row=14, column=1)




window.mainloop()