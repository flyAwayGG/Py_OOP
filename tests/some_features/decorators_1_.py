def wrap(func):
    def wrapped():
        print("Before wrap")
        print (func())
        print("After wrap")

    return wrapped


def wrapable():
    return 'Wrapable'


def test_1_():
    wrapabl = wrap(wrapable)
    wrapabl()

