# -*- coding: utf-8 -*-

__author__ = 'anosov'

import Tkinter
import time
import math
import datetime

def pack(callable_, *args, **kwargs):
    result = callable_(*args, **kwargs)
    result.pack()
    return result

def button_pressed():
    print var.get()

def window_deleted(*args, **kwargs):
    print 'window deleted', args, kwargs
    root.quit()

def current_time():
    return datetime.datetime.now().time().isoformat()

def set_time():
    label_0['text'] = 'Now ' + current_time()
    root.after(50, set_time)

root = Tkinter.Tk()
root.geometry('500x300')
root.title('Пример')
root.resizable(False, False)

label_0 = Tkinter.Label()
label_0.pack()

conf = {'text': 'Press button', 'command' : button_pressed, 'height': 2, 'width': 15}
btn = pack(Tkinter.Button, **conf)

var = Tkinter.IntVar()
pack(Tkinter.Checkbutton, text='Do you Russian?', variable=var, onvalue=12, offvalue=45)

var2 = Tkinter.IntVar()
pack(Tkinter.Radiobutton, text='Russian', variable=var2, value=1)
pack(Tkinter.Radiobutton, text='American', variable=var2, value=2)
pack(Tkinter.Radiobutton, text='Polish', variable=var2, value=3)

pack(Tkinter.Scale, orient=Tkinter.HORIZONTAL, from_=10, to=50, tickinterval=10, length=300)

root.after_idle(set_time)
root.after_idle(lambda: root.title('hali - gali'))
root.mainloop()

