"""
Common abstract base classes (or mixins..if we get krazy) that will be shared
across modules.
"""

class SaveLoad(object):
    """
    Objects which inherit from this class have load/ methods, which [un]pickle
    them to disk.

    Uses cPickle, so objects cannot have an attribute set to either a lambda
    function, or any function that is not defined until some class is
    initialized (classmethod).
    """
    def save(self, savefile, protocol=-1):
        """
        Pickle self to outfile.

        Parameters
        ----------
        savefile : filepath or buffer
        protocol : 0, 1, 2, -1
            0 < 1 < 2 in terms of performance.  -1 means use highest available.
        """
        with smart_open(savefile, 'w') as f:
            cPickle.dump(self, f, protocol=protocol)

    @classmethod
    def load(cls, loadfile):
        """
        Pickle SFileFilter from disk.

        Parameters
        ----------
        loadfile : filepath or buffer
        """
        with smart_open(loadfile, 'rb') as f:
            return cPickle.load(f)