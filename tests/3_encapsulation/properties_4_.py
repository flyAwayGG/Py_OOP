class Mine(object):
    def __init__(self,init):
        self.__x = init

    @property
    def x(self):
        return self.__x - 1

    @x.setter
    def x(self, value):
        self.__x = value + 1

def test_():

    mine = Mine(10)
    print(mine.x)

    mine.x = 3
    print(mine.x)

