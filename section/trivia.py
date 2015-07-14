__author__ = 'anosov'

import Tkinter as tk
from data_handler import DataHandler
from LG.field import Field as LG_Field
from LG.solver import solve as LG_solve
from LG.solver import Solver as LG_Solver

def write(path, str_):
    with open(path, 'w') as f:
        f.write(str_)

EXTERNAL_PATH = '/ExternalLevels/'


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

    def press_button_out_level():
        print len(idx_of_max)

        with open('/ExternalLevels/lvl.txt', 'w') as f:
            f.write(handle.product(idx_of_max.pop(0)))

    tk.Button(root, text='Out level', command=press_button_out_level).pack()

    def action():
        # average_len_of_finished_path
        lens_of_finished_paths = map(len, handle.finished_packed_paths)
        average = float(sum(lens_of_finished_paths)) / len(lens_of_finished_paths)
        label__average_len_of_finished_path['text'] = 'Average len of finished paths: ' + str(average)
        label_min_max['text'] = 'Min: %i; Max %i' % (min(lens_of_finished_paths), max(lens_of_finished_paths))

    return action

def case_0(root, handle):
    import numpy as np

    lbl_count = tk.Label(text='Count: ')
    lbl_count.pack()

    tk.Label(root, text='Spear walked:  ').pack(side=tk.LEFT)
    scale_1 = tk.Scale(root, orient=tk.HORIZONTAL, length=200)

    min_ = min(handle.spear_walked_count)
    max_ = max(handle.spear_walked_count)

    scale_1['showvalue'] = False
    scale_1['sliderlength'] = 20
    scale_1['tickinterval'] = 1
    scale_1['from'] = min_
    scale_1['to'] = max_
    scale_1.set(min_)
    scale_1.pack(side=tk.LEFT)

    scale_2 = tk.Scale(root, orient=tk.HORIZONTAL, length=200)
    scale_2['showvalue'] = False
    scale_2['sliderlength'] = 20
    scale_2['tickinterval'] = 1
    scale_2['from'] = min_
    scale_2['to'] = max_
    scale_2.set(max_)
    scale_2.pack(side=tk.LEFT)

    btn = tk.Button(root, text='Filter')
    btn.pack(side=tk.LEFT)

    allowed = np.ones((1, len(handle.covers)), dtype=np.bool)

    def cmd_1(var_1):
        if int(var_1) > scale_2.get():
            scale_1.set(scale_2.get())

    def cmd_2(var_2):
        if int(var_2) < scale_1.get():
            scale_2.set(scale_1.get())

    def cmd_btn():
        a, b = scale_1.get(), scale_2.get()
        for i, c in enumerate(handle.spear_walked_count):
            allowed[0, i] = (a <= c <= b)
        lbl_count['text'] = 'Count: ' + str(np.sum(allowed))

    btn['command'] = cmd_btn
    scale_1['command'] = cmd_1
    scale_2['command'] = cmd_2