from tkinter import *
import tkinter as tk

window = Tk()
window.configure(background='grey')

count = 0
window.counter = 0

def backgroundIndicator():
    if window.counter < 0:
        window.configure(background='red')
    elif window.counter == 0:
        window.configure(background='grey')
    else:
        window.configure(background='green')

def countUp():
    window.counter+=1
    labelCounter['text'] = str(window.counter)
    backgroundIndicator()


    
def countDown():
    window.counter-=1
    labelCounter['text'] = str(window.counter)   
    backgroundIndicator()


labelUp = Button(window, text="Up", font=("Arial", 10),  width = 25, anchor='center', command= countUp, highlightthickness = 0, bd = 0)
labelUp.pack()
labelUp.pack(padx=20, pady=10)

labelCounter = Button(window, text=0, font=("Arial", 10), width = 25, anchor='center', highlightthickness = 0, bd = 0)
labelCounter.pack()
labelCounter.pack(padx=20, pady=10)

labelDown = Button(window, text="Down", font=("Arial", 10), width = 25, anchor='center', command=countDown, highlightthickness = 0, bd = 0)
labelDown.pack()
labelDown.pack(padx=20, pady=10)


window.mainloop()
