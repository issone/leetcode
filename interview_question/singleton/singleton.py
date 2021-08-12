from threading import Lock


class Singleton:
    lock = Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with cls.lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = object.__new__(cls)
        return cls._instance


if __name__ == '__main__':
    a1 = Singleton()
    a2 = Singleton()
    print(id(a1) == id(a2))