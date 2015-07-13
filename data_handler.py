__author__ = 'hard7'

import cPickle
import os.path
from lazy_holder import LazyHolder
from itertools import *
from LG.field import Field as LG_Filed
import StringIO

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
        self.finished_paths = loaded_covers['cover_paths']

        self.data = dict()
        self._path_to_data = path_to_data
        self.load(path_to_data)

    @property
    def finished_packed_paths(self):
        return [self.paths[i] for i in self.finished_paths]

    @property
    def covers_count(self):
        return len(self.covers)

    def product(self, cover_i):
        assert isinstance(cover_i, int)
        cover = self.covers[cover_i]
        unpacked_cover = [(self.cells[c_id], self.periods[p_id]) for (c_id, p_id) in cover]
        unpacked_unwrapped_cover = [tuple(chain(*c)) for c in unpacked_cover]

        field = LG_Filed.loads(self.base)
        map(field.add_spear, unpacked_unwrapped_cover)
        return field.take_json()

    def load(self, path=None):
        if path and os.path.isfile(path):
            with open(path) as f:
                loaded_data = cPickle.load(f)
            self.data.update(loaded_data)
            for key, value in self.data.iteritems():
                self.__dict__[key] = value

    def dump(self, path=None):
        path_for_save = path if path else self._path_to_data
        if path_for_save is None:
            raise Exception('Path for save should be set')
        with open(path_for_save, 'w') as f:
            cPickle.dump(self.data, f)