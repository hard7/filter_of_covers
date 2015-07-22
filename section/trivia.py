__author__ = 'anosov'

import Tkinter as tk
from data_handler import DataHandler
from LG.field import Field as LG_Field
from LG.solver import solve as LG_solve
from LG.solver import Solver as LG_Solver
import numpy as np
import itertools
import random
from functools import partial

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

def make_scales(root, name, array, allowed, index, refrash):
    tk.Label(root, text=name+':  ').grid(row=index, column=0)

    make_scale = partial(tk.Scale, root, orient=tk.HORIZONTAL, length=250)
    scales = [make_scale(), make_scale()]
    state = [min(array), max(array)]

    for i, scale in enumerate(scales):
        scale.config(sliderlength=20, tickinterval=(state[1] - state[0]) / 6)
        scale.config(showvalue=False, from_=state[0], to=state[1])
        scale.set(state[i])
        scale.grid(row=index, column=i+1)

    btn = tk.Button(root, text='Filter')
    btn.grid(row=index, column=3)

    # ~ color #d6d2d0 is standard for activebackground
    button_set_normal = lambda btn: btn.config(bg='gray', activebackground='#d6d2d0')
    button_set_gold = lambda btn: btn.config(bg='gold2', activebackground='gold')

    def cmd(index):
        assert index in [0, 1]
        cur_scale = scales[index]
        other_scale = scales[1 - index]

        def wrapper(var):
            button_set_normal(btn)

            vars = [s.get() for s in scales]
            if vars[0] > vars[1]:
                cur_scale.set(other_scale.get())
            if vars != state:
                button_set_gold(btn)

        return wrapper

    def cmd_btn():
        state[:] = [s.get() for s in scales]
        button_set_normal(btn)

        for i, c in enumerate(array):
            allowed[index, i] = (state[0] <= c <= state[1])
        refrash()

    btn.config(command=cmd_btn)
    [scale.config(command=cmd(i)) for i, scale in enumerate(scales)]


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

