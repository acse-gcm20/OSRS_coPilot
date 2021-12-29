import tkinter as tk
import pyautogui as pg
from time import sleep

template = tk.Tk()
template.geometry('1000x505+5+10')
template.mainloop()

coPilot = tk.Tk()

width = 230
height = 620
x = 1010
y = 10

buffer_x = 15
buffer_y = 40

inv_x = 1205 #- buffer_x
inv_y = 400 #- buffer_y
dx = 65
dy = 54

window_x = coPilot.winfo_screenwidth()
window_y = coPilot.winfo_screenheight()
print(f'{window_x} x {window_y}')

coPilot.geometry(f'{width}x{height}+{x}+{y}')

val_entry = tk.Entry(coPilot)
val_entry.pack()

def calibrate():
    pg.move(inv_x, inv_y)
    sleep(3)
    pg.move(inv_x + 3*dx, inv_y + 6*dy)

def click_border():
    pg.click(200, 20)

def drop_items():
    num = int(val_entry.get())
    click_border()
    print(f'Dropping {num}')
    pg.keyDown('shift')
    sleep(0.5)

    rows = int(num / 4)
    cols = num % 4
    print(rows, cols)

    for y in range(rows):
        pos_y = inv_y + y*dy
        for x in range(4):
            print(f'({x}, {y})')
            pos_x = inv_x + x*dx
            pg.click(pos_x, pos_y)
            sleep(0.4)

    for x in range(cols):
        pos_x = inv_x + x*dx
        pos_y = inv_y + (rows-1)*dy
        pg.click(pos_x, pos_y)
        sleep(0.4)

    sleep(0.5)
    pg.keyUp('shift')

def trace_inv():
    print('Tracing')

    for y in range(7):
        pos_y = inv_y + y*dy
        for x in range(4):
            pos_x = inv_x + x*dx
            pg.moveTo(pos_x, pos_y)
            sleep(0.4)

class Button:

    def __init__(self, text, command):
        self.text = text
        self.command = command

        self.btn = tk.Button(coPilot, text=self.text, command=self.command)
        self.btn.pack()


trace_btn = Button('Trace Inv', trace_inv)
drop_btn = Button('Drop Inv', drop_items)
calibrate_btn = Button('Calibrate', calibrate)

coPilot.mainloop()