__author__ = 'hard7'

import cPickle
import os.path
from lazy_holder import LazyHolder


# Covers dump description
# of format https://goo.gl/Td4FmA


class DataHandler(object):
    def __init__(self, path_to_covers, path_to_data=None):
        with open(path_to_covers) as f:
            loaded_covers = cPickle.load(f)
        self.base = loaded_covers['base']
        self.periods = loaded_covers['periods']
        self.cells = loaded_covers['cells']
        self.paths = loaded_covers['paths']
        self.covers = loaded_covers['covers']
        self.cover_paths = loaded_covers['cover_paths']

        self._path_to_calculated_data = path_to_data
        if path_to_data and os.path.isfile(path_to_data):
            with open(path_to_data) as f:
                pass
        self.data = dict()

    @LazyHolder
    def get_42(self):
        print '42'
        return 42

