from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_book(self):
        pass

    @abstractmethod
    def show_menu(self):
        pass