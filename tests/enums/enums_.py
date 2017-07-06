from enum import Enum


class Fruits(Enum):
    PINEAPPLE = 'Pineapple'
    APPLE = 'Apple'


class Pen:
    def __str__(self):
        return 'Pen'

def test_1_():
    print ('I have')
    print(f'{Pen()} {Fruits.PINEAPPLE.value} {Fruits.APPLE.value} {Pen()}')

def test_2_():
    for fruit in Fruits:
        print(f'Value of fruit {fruit} is {fruit.value}')

def test_3_():
    assert Fruits.APPLE == Fruits.APPLE
    assert Fruits.APPLE != Fruits.PINEAPPLE

