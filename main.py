
# mock
class DataHandler(object):
    def __init__(self):
        pass


class GUI(object):
    def __init__(self, handler):
        assert isinstance(handler, DataHandler)
        self.handler = handler

if __name__ == '__main__':
    dh = DataHandler()
    gui = GUI(dh)