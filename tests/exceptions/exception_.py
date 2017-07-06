import random


class WtfException(Exception):
    pass


def test_1_():
    try:
        rnd = random_value()
        print(rnd)
        a = float(rnd)
        print(100 / a)
    except ValueError:
        print("Это не число!")
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    except:
        raise WtfException()
    else:
        print("Код выполнился без ошибок")
    finally:
        print("Я выполняюсь в любом случае!")


class Cat:
    pass


def random_value():
    list = ['str', 1, 0.1, 0, Cat()]
    return random.choice(list)
