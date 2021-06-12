from container import Container
from iterator import Iterator


class NameRepository(Container):

    _names = ["Ivan", "Peter", "Georgi"]

    def get_iterator(self):
        return self._NameIterator(self)

    def get_names(self):
        return self._names

    class _NameIterator(Iterator):

        # _index = None
        _index = 0
        _current = None
        _name_repository = None

        def __init__(self, name_repository):
            self._name_repository = name_repository

        def has_next(self):
            if self._index < len(self._name_repository.get_names()):
                # return True
                return self._name_repository.get_names()

            return False

        def next(self):
            if self.has_next():
                self._current = self._name_repository.get_names()[self._index]
                self._index = self._index + 1

                return self._current

            return None
