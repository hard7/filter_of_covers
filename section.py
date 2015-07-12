
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
    button_data_to_console = tk.Button(root, text='Data to console')

    label.pack()
    button.pack()
    button_data_to_console.pack()

    def press_button_data_to_console():
        print handler.data

    def set_42():
        label['text'] = handler.get_42

    button['command'] = set_42
    button_data_to_console['command'] = press_button_data_to_console


def show_count_of_covers(root, handler):
    count_covers = len(handler.covers)
    text = 'Count of covers: ' + str(count_covers)
    tk.Label(root, text=text).pack()