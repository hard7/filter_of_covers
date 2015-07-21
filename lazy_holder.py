__author__ = 'hard7'

from lazy import lazy
import time


class LazyHolder(lazy):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

    def __get__(self, inst, inst_cls):
        start_time = time.time()
        value = super(self.__class__, self).__get__(inst, inst_cls)
        delta_time = time.time() - start_time

        time_spent = inst.data.setdefault('time_spent', dict())
        inst.data[self.__name__] = value
        time_spent[self.__name__] = delta_time
        return value
