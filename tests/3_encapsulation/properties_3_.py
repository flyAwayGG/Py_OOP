class Mine(object):
    def __init__(self):
        self.__x = None

    x = property()

    @x.getter
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @x.deleter
    def x(self):
        self.__x = 'No more'

def test_():

    mine = Mine()
    print(mine.x)

    mine.x = 3
    print(mine.x)

    del mine.x
    print(mine.x)
