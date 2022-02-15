from tkinter import *
import random

window = Tk()
window.geometry("150x150")

colorBackground = random.choice(['green', 'grey', 'red'])
window.configure(background=colorBackground)


def onHover(self):
    window.configure(background='yellow')
    
def onLeave(self):
    window.configure(background=colorBackground)

    
label = Label(window, text="Kleur veranderen", font=("Arial", 10), anchor='center')

label.bind("<Enter>", onHover)
label.bind("<Leave>", onLeave)
label.pack()

window.mainloop()