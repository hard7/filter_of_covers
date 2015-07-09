__author__ = 'hard7'




class GUI(object):
    def __init__(self, handler):
        assert isinstance(handler, DataHandler)
        self._handler = handler
        self._root = tk.Tk()
        self._root.minsize(300, 200)
        self._sections = list()

    def append(self, section):
        if self._sections:
            self._add_separator()

        frame = tk.Frame()
        func = section(frame, self._handler)
        if func is not None:
            self._sections.append(func)
        frame.pack()

    def _add_separator(self):
        tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=10, pady=5)

    def run(self):
        self._root.after_idle(self._run_sections)
        self._root.mainloop()

    def _run_sections(self):
        [sec() for sec in self._sections]
        print 'done'