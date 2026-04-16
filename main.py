# 1-mashq
class LogMixin:
    def log(self, msg):
        print(msg)

class Service(LogMixin):
    pass

s = Service()
s.log("Hello")
# 2-mashq
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
# 3-mashq
class User:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age
# 4-mashq
class Descriptor:
    def __get__(self, obj, objtype):
        return obj._value

    def __set__(self, obj, value):
        obj._value = value

class Test:
    x = Descriptor()

    def __init__(self):
        self._value = 0
# 5-mashq
class Event:
    def __init__(self):
        self.handlers = []

    def register(self, h):
        self.handlers.append(h)

    def trigger(self):
        for h in self.handlers:
            h()
