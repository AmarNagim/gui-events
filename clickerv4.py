from tkinter import *
import random

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

test1 = None

def countUp(event):
    global test1
    window.counter+=1
    labelCounter['text'] = str(round(window.counter, 2))
    backgroundIndicator()
    test1 = True

    
def countDown(event):
    global test1
    window.counter-=1
    labelCounter['text'] = str(round(window.counter, 2))   
    backgroundIndicator()
    test1 = False

def calc(event):
    print('doubleclick')
    print(test1)
    if test1 == False:
        window.counter/=3
        print(window.counter)
        labelCounter['text'] = str(round(window.counter, 2))   
        backgroundIndicator()
    elif test1 == True:
        window.counter*=3
        print(window.counter)
        labelCounter['text'] = str(round(window.counter, 2))   
        backgroundIndicator() 
    else:
        pass               


colorBackground = random.choice(['green', 'grey', 'red'])


def onHover(self):
    window.configure(background='yellow')
    
def onLeave(self):
    backgroundIndicator()


labelUp = Button(window, text="Up", font=("Arial", 10), width = 25, anchor='center', highlightthickness = 0, bd = 0)
labelUp.bind('<Button-1>', countUp)
window.bind('+', countUp)
labelUp.pack(padx=20, pady=10)

labelCounter = Label(window, text=0, font=("Arial", 10), width = 25, anchor='center')
labelCounter.bind("<Enter>", onHover)
labelCounter.bind("<Leave>", onLeave)
labelCounter.bind('<Double-1>', calc)
window.bind("<space>", calc)
labelCounter.pack(padx=20, pady=10)

labelDown = Button(window, text="Down", font=("Arial", 10), width = 25, anchor='center', highlightthickness = 0, bd = 0)
labelDown.bind('<Button-1>', countDown)
window.bind('-', countDown)

labelDown.pack()
labelDown.pack(padx=20, pady=10)


window.mainloop()