class Hiding:
    def __init__(self):
        self.public = 'public'
        self.__private = 'private'

    def public_mtd(self):
        return 'public_mtd'

    def __private_mtd(self):
        return 'private_mtd'


class Child(Hiding):
    def private_mtd(self):
        return self.__private_mtd()

    def private(self):
        return self.__private()

def test_():
    hiding = Hiding()

    print(f"Public: {hiding.public}")
    # print(f"Private: {hiding.__private}")

    print(f"Public: {hiding.public_mtd()}")
    # print(f"Private: {hiding.__private()}")

    child = Child()
    # child.private_mtd()
    # child.private()