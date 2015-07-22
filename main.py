
import Tkinter as tk

from data_handler import DataHandler
from gui import GUI
# from section.sample import *
from section import trivia
import os
import numpy as np

def find_distance(i_):
    path_to_covers = '/home/anosov/data/hard_base/covers/case_%i.dump' % (i_, )
    base, ext = os.path.splitext(path_to_covers)
    path_to_data = base + '__computing' + ext
    h = DataHandler(path_to_covers, path_to_data)
    tmp = h.distance_to_dead_ends
    h.dump()


def main():
    path_to_covers = '/home/anosov/data/hard_base/covers/case_0.dump'
    base, ext = os.path.splitext(path_to_covers)
    path_to_data = base + '__computing' + ext

    h = DataHandler(path_to_covers, path_to_data)
    gui = GUI(h)

    # gui.append(trivia.show_stat_rm)
    # gui.append(trivia.show_equal_stat)
    gui.append(trivia.case_0)

    gui.run()

def solver_profiling():
    path_to_covers = '/home/anosov/data/hard_base/covers/case_0.dump'
    h = DataHandler(path_to_covers)

    from LG.solver import Solver as LG_Solver

    i_ = 0
    f = h.product_field(i_)
    for i in xrange(1):
        s = LG_Solver(f)
        a = s.run()
        b = s.alternative_path_lens()
        print a
        print [h.cells[i] for i in h.finished_packed_paths[i_]]
        print b

def profile():
    import cProfile
    from pstats import Stats

    path_to_stat_file = '/tmp/_profiling_'
    cProfile.run('solver_profiling()', path_to_stat_file)
    s = Stats(path_to_stat_file)
    # s.strip_dirs()
    s.sort_stats('time')
    # s.sort_stats('cum')
    s.print_stats(20)

    times = [v[2] for v in s.stats.values()]
    times.sort(reverse=True)
    # times = times[:N]
    sum_of_times = sum(times)
    print sum_of_times, [round(t / sum_of_times * 100, 2) for t in times][:10]


if __name__ == '__main__':
    # profile()
    main()
