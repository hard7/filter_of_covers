__author__ = 'hard7'

import cPickle
import os.path
from lazy_holder import LazyHolder
from itertools import *
from LG.field import Field as LG_Filed
import StringIO
import numpy as np
import itertools

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

    @property
    def spear_cells(self):
        return [zip(*cover)[0] for cover in self.covers]

    @property
    def spear_walked_count(self):
        return map(len, self.spear_walked)

    @property
    def spear_walked(self):
        spear_coords = map(set, self.spear_cells)
        fp = map(set, self.finished_packed_paths)
        return map(lambda a, b: tuple(a & b), spear_coords, fp)

    def product(self, cover_i):
        assert isinstance(cover_i, int)
        cover = self.covers[cover_i]
        unpacked_cover = [(self.cells[c_id], self.periods[p_id]) for (c_id, p_id) in cover]
        unpacked_unwrapped_cover = [tuple(chain(*c)) for c in unpacked_cover]

        field = LG_Filed.loads(self.base)
        map(field.add_spear, unpacked_unwrapped_cover)
        return field.take_json()

    def make_unwrapped_spears(self, id):
        cover = self.covers[id]
        unpacked_cover = [(self.cells[c_id], self.periods[p_id]) for (c_id, p_id) in cover]
        unpacked_unwrapped_cover = [tuple(chain(*c)) for c in unpacked_cover]
        return unpacked_unwrapped_cover


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

    def choose_unique_covers(self, allowed, percent):
        def _calc_similarity(first_path, second_path):
            counter = 0
            previous_index = None
            for i in first_path:
                if i in second_path:
                    if previous_index is not None:
                        counter += (i == second_path[previous_index + 1])
                    previous_index = second_path.index(i)
                else:
                    previous_index = None
            return counter


        result, ignored = set(), set()
        indies = np.where(allowed)[0]
        indies = np.random.shuffle(indies)
        for i in indies:
            new_path_index = self.finished_paths[i]
            new_path = self.paths[new_path_index]
            if new_path_index in ignored:
                continue
            for j in result:
                cur_path = self.paths[self.finished_paths[j]]

















