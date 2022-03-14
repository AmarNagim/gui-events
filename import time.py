import tkinter as tk
import random

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

def place_label(canvas, label):
    '''place a label on a canvas in a random, non-overlapping location'''
    width = label.winfo_reqwidth()
    height = label.winfo_reqheight()

    tries = 0
    while True and tries < 1000:
        tries += 1 # failsafe, to prevent an infinite loop
        x = random.randint(0, 200-width)
        y = random.randint(0, 200-height)
        items = canvas.find_overlapping(x, y, x+width, y+height)
        if len(items) == 0:
            canvas.create_window(x, y, window=label, anchor="nw")
            break

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack(fill="both", expand=True)

for word in words:
    label = tk.Label(root, text=word)
    place_label(canvas, label)

root.mainloop()