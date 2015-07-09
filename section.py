
import Tkinter as tk

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
        # root.after_idle(lambda: root.title('hali - gali'))
    return wrapper

def show_42(root, handler):
    label = tk.Label(root, text='No Number')
    button = tk.Button(root, text='Press')

    label.pack()
    button.pack()

    def set_42():
        label['text'] = handler.get_42()

    button['command'] = set_42