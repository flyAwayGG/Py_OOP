import time


class Human:
    def __init__(self, name: str):
        self.name = name

    def you_goddam_right(self) -> None:
        print("You're God damn right")

    def is_heisenberg(self,name) -> bool:
        return name.lower() == 'heisenberg'


def test_():
    ww = Human('Heisenberg')

    print ('Say my name')

    time.sleep(1)

    name = input()

    if ww.is_heisenberg(name):
        time.sleep(3)
        ww.you_goddam_right()
        time.sleep(10)

    else:
        print('Game over. You die.')


