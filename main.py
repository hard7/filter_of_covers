
import Tkinter as tk

from data_handler import DataHandler
from gui import GUI
from section import *



if __name__ == '__main__':
    dh = DataHandler()
    gui = GUI(dh)
    gui.append(timer_section)
    gui.append(show_42)

    gui.run()
