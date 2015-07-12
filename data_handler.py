__author__ = 'hard7'

import cPickle

# Covers dump description
# of format https://goo.gl/Td4FmA


class DataHandler(object):
    def __init__(self, path_to_covers):
        with open(path_to_covers) as f:
            loaded_covers = cPickle.load(f)
        base_json = loaded_covers['base']
        self.periods = loaded_covers['periods']
        self.cells = loaded_covers['cells']
        self.paths = loaded_covers['paths']
        self.covers = loaded_covers['covers']
        self.cover_paths = loaded_covers['cover_paths']

    def get_42(self):
        return 42

