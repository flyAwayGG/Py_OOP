class Car(object):
    wheels = 4

    def __init__(self, brand, model):
        self.name = brand
        self.model = model

    def move(self):
        return f'{self.name} {self.model} заведена'

    @staticmethod
    def static_method():
        return "Статический метод"

    @classmethod
    def bmw(cls,series):
        return cls('BMW', series)


def class_test_():
    tesla = Car('Tesla','X')
    assert tesla.move() == "Tesla X заведена"
    assert tesla.name == 'Tesla'
    assert tesla.model == 'X'
    assert tesla.wheels == 4

    ferrari = Car('Ferrari','488')
    assert ferrari.name == 'Ferrari'
    assert ferrari.model == '488'
    assert ferrari.wheels == 4


def static_():
    assert Car.static_method() == "Статический метод"
    assert Car.wheels == 4

    audi = Car('Audi', 'A8')
    assert audi.wheels == 4

    audi.wheels = 5
    assert audi.wheels == 5
    assert Car.wheels == 4

    Car.wheels == 6
    assert audi.wheels == 5
    assert Car.wheels == 4


def class_method_():
    bmw = Car.bmw('I7')
    assert bmw.move() == "BMW I7 заведена"

