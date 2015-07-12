__author__ = 'hard7'

import lazy


class LazyHolder(lazy.lazy):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

    def __get__(self, inst, inst_cls):
        value = super(self.__class__, self).__get__(inst, inst_cls)
        inst.data[self.__name__] = value
        return value