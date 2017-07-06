class Mine(object):
    def __init__(self):
        self.__x = None

    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

    def del_x(self):
        self.__x = 'No more'

    x = property(get_x, set_x, del_x, 'Это свойство x.')


def test_():
    print(type(Mine.x))  # property

    mine = Mine()
    print(mine.x)

    mine.x = 3
    print(mine.x)

    del mine.x
    print(mine.x)

