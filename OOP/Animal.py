from datetime import datetime


class Animal:
    def __init__(self, name: str, age: int, birthday: datetime):
        self.name: str = name
        self._age: int = age
        self.__birthday: datetime = birthday

    # Getters
    @property
    def name(self):
        return self.name

    @property
    def age(self):
        return self._age

    @property
    def birthday(self):
        return self.__birthday

    # Setters
    @name.setter
    def name(self, name):
        self.name = name

    @age.setter
    def age(self, age):
        self._age = age

    @birthday.setter
    def birthday(self, birthday):
        self.__birthday = birthday

    # Methods
    def eat(self):
        print(self.name + " is eating")


if __name__ == "__main__":
    animal = Animal("Dog", 5, datetime.now())
    print(animal.name)
