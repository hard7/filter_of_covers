
import Tkinter as tk

from data_handler import DataHandler
from gui import GUI
# from section.sample import *
from section import trivia


if __name__ == '__main__':
    # path_to_covers = '/home/anosov/data/test_covers/test_50k_covers.dump'
    # path_to_covers = '/home/anosov/data/test_covers/test_50k_covers_for_4_phases.dump'
    path_to_covers = '/home/anosov/data/test_covers/test_10k_covers_for_4_phases_600.dump'
    path_to_covers = '/home/anosov/data/hard_base/covers/case_0.dump'

    path_to_data = '/home/anosov/data/test_covers/data.dump'

    dh = DataHandler(path_to_covers, path_to_data)
    gui = GUI(dh)
    # gui.append(timer_section)
    # gui.append(show_42)
    # gui.append(show_count_of_covers)

    # gui.append(trivia.show_stat_rm)
    # gui.append(trivia.show_equal_stat)

    gui.append(trivia.case_0)

    gui.run()
