from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def talk(self):
        pass


class Cat(Animal):
    def talk(self):
        return 'Meow!'


class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'


def test_():
    animals = [Cat('Missy'),
               Cat('Mr. Mistoffelees'),
               Dog('Lassie')]

    for animal in animals:
        print(f"{animal.name} : {animal.talk()}")


    # animal = Animal('Abstract Animal')
