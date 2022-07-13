from abc import ABC, abstractmethod


# Observer Pattern

class Subject(ABC):

    @abstractmethod
    def subscribe(self, observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer):
        pass

    @abstractmethod
    def notify_all(self):
        pass

class ConcreteSubject(Subject):

    _status = 0

    _observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify_all(self):
        for observer in self._observers:
            observer.update(self)

    def business_logic(self):
        self._status = 2

        self.notify_all()

class Observer(ABC):

    @abstractmethod
    def update(self, subject):
        pass

class ConcreteObserver(Observer):

    def update(self, subject):
        if subject._status == 2:
            print('Got message')

# Strategy Pattern
class Strategy(ABC):
    @abstractmethod
    def execute():
        pass

class StrategyOne(Strategy):
    def execute():
        pass

class Context:

    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy


# Singleton Pattern
def singleton(cls):

    instances = {}

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return wrap

@singleton
class User:
    def __init__(self, username):
        self.username = username


    def __str__(self):
        return f'Username: {self.username}'