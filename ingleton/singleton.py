def singleton(self):
    _instances = {}

    def get_instance():
        if self not in _instances:
            _instances[self] = self()

        return _instances[self]

    return get_instance


@singleton
class Singleton:
    pass
