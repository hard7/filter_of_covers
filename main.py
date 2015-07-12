
import Tkinter as tk

from data_handler import DataHandler
from gui import GUI
from section import *



if __name__ == '__main__':
    dh = DataHandler('../test_10k_covers.dump', '../data.dump')
    gui = GUI(dh)
    gui.append(timer_section)
    gui.append(show_42)
    gui.append(show_count_of_covers)

    gui.run()
