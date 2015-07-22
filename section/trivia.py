__author__ = 'anosov'

import Tkinter as tk
from data_handler import DataHandler
from LG.field import Field as LG_Field
from LG.solver import solve as LG_solve
from LG.solver import Solver as LG_Solver
import numpy as np
import itertools
import random

def write(path, str_):
    with open(path, 'w') as f:
        f.write(str_)

EXTERNAL_PATH = '/ExternalLevels/'


def dec_button(root, *ar, **kw):
    btn = tk.Button(root)
    def decorator(fn):
        btn['text'] = fn.__name__
        btn['command'] = fn
        btn.grid(*ar, **kw)
        return fn
    return decorator

def dec_freak(fn):    # button decorator off switcher
    pass


def show_stat_rm(root, handle):
    assert isinstance(handle, DataHandler)

    tk.Label(root, text='Count of covers: %i' % (handle.covers_count, )).pack()

    label_min_max = tk.Label(root)
    label_min_max.pack()

    label__average_len_of_finished_path = tk.Label(root)
    label__average_len_of_finished_path.pack()

    lens_of_finished_paths = map(len, handle.finished_packed_paths)
    max_ = max(lens_of_finished_paths)

    max_finished_paths_with_indexes = filter(lambda (i, len_): len_ == max_, enumerate(lens_of_finished_paths))
    idx_of_max = list(zip(*max_finished_paths_with_indexes)[0])

    @dec_button(root)
    def press_button_out_level():
        print len(idx_of_max)
        with open('/ExternalLevels/lvl.txt', 'w') as f:
            f.write(handle.product(idx_of_max.pop(0)))

    def action():
        # average_len_of_finished_path
        lens_of_finished_paths = map(len, handle.finished_packed_paths)
        average = float(sum(lens_of_finished_paths)) / len(lens_of_finished_paths)
        label__average_len_of_finished_path['text'] = 'Average len of finished paths: ' + str(average)
        label_min_max['text'] = 'Min: %i; Max %i' % (min(lens_of_finished_paths), max(lens_of_finished_paths))

    return action

def make_scales(root, name, array, allowed, i_, refrash):
    tk.Label(root, text=name+':  ').grid(row=i_, column=0)
    min_ = min(array)
    max_ = max(array)

    state = [min_, max_]

    scale_1 = tk.Scale(root, orient=tk.HORIZONTAL, length=250)
    scale_1['showvalue'] = False
    scale_1['sliderlength'] = 20
    scale_1['tickinterval'] = (max_ - min_) / 6
    scale_1['from'] = min_
    scale_1['to'] = max_
    scale_1.set(min_)
    scale_1.grid(row=i_, column=1)

    scale_2 = tk.Scale(root, orient=tk.HORIZONTAL, length=250)
    scale_2['showvalue'] = False
    scale_2['sliderlength'] = 20
    scale_2['tickinterval'] = (max_ - min_) / 6
    scale_2['from'] = min_
    scale_2['to'] = max_
    scale_2.set(max_)
    scale_2.grid(row=i_, column=2)

    btn = tk.Button(root, text='Filter')
    btn.grid(row=i_, column=3)

    def cmd_1(var_1):
        btn['bg'] = 'gray'
        btn['activebackground'] = abg
        if [scale_1.get(), scale_2.get()] != state:
            btn['bg'] = 'gold2'
            btn['activebackground'] = 'gold'

        if int(var_1) > scale_2.get():
            scale_1.set(scale_2.get())

    def cmd_2(var_2):
        btn['bg'] = 'gray'
        btn['activebackground'] = abg
        if [scale_1.get(), scale_2.get()] != state:
            btn['bg'] = 'gold2'
            btn['activebackground'] = 'gold'

        if int(var_2) < scale_1.get():
            scale_2.set(scale_1.get())

    abg = btn['activebackground']

    def cmd_btn():
        a, b = scale_1.get(), scale_2.get()
        state[:] = [a, b]
        btn['bg'] = 'gray'
        btn['activebackground'] = abg

        for i, c in enumerate(array):
            allowed[i_, i] = (a <= c <= b)
        refrash()

    btn['command'] = cmd_btn
    scale_1['command'] = cmd_1
    scale_2['command'] = cmd_2


def allowed_to_indices(allowed):
    return np.where(np.all(allowed, axis=0))[0]

def case_0(root, handle):
    lbl_count = tk.Label(text='Count: ')
    lbl_count.pack()

    v0 = tk.IntVar()
    allowed = np.ones((4, len(handle.covers)), dtype=np.bool)
    unique_var = tk.IntVar()

    def refrash():
        if unique_var.get():
            indies = handle.choose_unique_covers(allowed[1:], 0.60)
            allowed[0] &= False
            for i in indies:
                allowed[0, i] = True
        else:
            allowed[0] |= True

        n = np.sum(np.all(allowed, axis=0))
        lbl_count['text'] = 'Count: ' + str(n)

    c = itertools.count()

    tk.Checkbutton(root, text='Unique', command=refrash, variable=unique_var).grid(row=c.next(), column=1)

    make_scales(root, 'spear_walked_count', handle.spear_walked_count, allowed, c.next(), refrash)
    make_scales(root, 'finished_packed_paths', map(len, handle.finished_packed_paths), allowed, c.next(), refrash)
    make_scales(root, 'max_distance_to_dead_ends', handle.max_distance_to_dead_ends, allowed, c.next(), refrash)

    @dec_button(root)
    def push_all():
        al = np.all(allowed, axis=0)
        indies = np.where(al)[0]
        assert len(indies) < 100
        for i, id_ in enumerate(indies):
            write(EXTERNAL_PATH + 'lvl_%i.txt' % (i, ), handle.product(id_))

    # @dec_button(root)
    def something():
        pass

