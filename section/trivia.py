__author__ = 'anosov'

import Tkinter as tk
from data_handler import DataHandler

def show_stat(root, handle):
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

        print 'Unique', len(set(handle.finished_paths[i] for i in idx_of_max))

    return action

def show_equal_stat(root, handle):
    lb_0 = tk.Label(root, text='Different finished paths: ' + str(len(handle.paths)))
    lb_0.pack()

    fpaths = map(set, handle.paths)

    stored = range(len(fpaths))
    for i, fi in enumerate(fpaths):
        for j, fj in enumerate(fpaths[i+1:]):
            if i not in stored or j+i+1 not in stored:
                continue
            n = fi ^ fj
            if len(n) < 10:
                stored.remove(j+i+1)

    filtered = [handle.paths[i] for i in stored]
    print '>', len(filtered)

    path_ids = map(handle.paths.index, filtered)

    a = map(handle.finished_paths.index, path_ids)

    def press_btn0():
        with open('/ExternalLevels/lvl.txt', 'w') as f:
            f.write(handle.product(a.pop(0)))

    tk.Button(text='SSAD', command=press_btn0).pack()


