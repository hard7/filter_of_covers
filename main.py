
import Tkinter as tk

# mock
class DataHandler(object):
    def __init__(self):
        pass

    def get_42(self):
        return 42


class GUI(object):
    def __init__(self, handler):
        assert isinstance(handler, DataHandler)
        self._handler = handler
        self._root = tk.Tk()
        self._root.minsize(300, 200)
        self._sections = list()

    def append(self, section):
        self._sections.append(section(self._root, self._handler))

    def run(self):
        self._root.after_idle(self._run_sections)
        self._root.mainloop()

    def _run_sections(self):
        [sec() for sec in self._sections]
        print 'done'

# sections
def timer_section(root, handler):
    time_label = tk.Label(root, text='asd')
    time_label.pack()
    c = [0]

    def set_time():
        c[0] += 1
        time_label['text'] = str(c[0])
        root.after(1000, set_time)


    def wrapper():
        root.after_idle(set_time)
        root.after_idle(lambda: root.title('hali - gali'))
    return wrapper


if __name__ == '__main__':
    dh = DataHandler()
    gui = GUI(dh)

    gui.append(timer_section)

    gui.run()
