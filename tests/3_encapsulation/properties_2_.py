class Mine(object):
    def __init__(self):
        self.__x = 'some value'

    @property
    def prop(self):
        return self.__x + ' and some value'


def test_():

    mine = Mine()
    print(mine.prop)

