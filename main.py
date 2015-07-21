
import Tkinter as tk

from data_handler import DataHandler
from gui import GUI
# from section.sample import *
from section import trivia
import os
import numpy as np


def main():
    # path_to_covers = '/home/anosov/data/test_covers/test_50k_covers.dump'
    # path_to_covers = '/home/anosov/data/test_covers/test_50k_covers_for_4_phases.dump'
    # path_to_covers = '/home/anosov/data/test_covers/test_10k_covers_for_4_phases_600.dump'
    path_to_covers = '/home/anosov/data/hard_base/covers/case_0.dump'
    path_to_data = os.path.splitext(path_to_covers)[0] + '__computing.dump'

    print path_to_data

    h = DataHandler(path_to_covers, path_to_data)
    gui = GUI(h)
    # gui.append(timer_section)
    # gui.append(show_42)
    # gui.append(show_count_of_covers)

    # gui.append(trivia.show_stat_rm)
    # gui.append(trivia.show_equal_stat)

    # gui.append(trivia.case_0)
    #
    # gui.run()

    d = h.distance_to_dead_ends

path_to_covers = '/home/anosov/data/hard_base/covers/case_0.dump'
h = DataHandler(path_to_covers)

def solver_profiling():
    from LG.solver import Solver as LG_Solver
    f = h.product_field(100)
    for i in xrange(45):
        s = LG_Solver(f)
        s.run()
        s.alternative_path_lens()

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
    profile()
    # main()