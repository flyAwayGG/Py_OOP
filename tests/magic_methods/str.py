class Account:
    def __init__(self,owner,amount):
        self.owner = owner
        self.amount = amount

    # def __repr__(self):
    #     return f'Account({self.owner}, {self.amount})'

    # def __str__(self):
    #     return f'Account of {self.owner} with starting amount: {self.amount}'

def test_():
    my_acc = Account('Nikita',5)

    print('repr() :')
    print(repr(my_acc))

    print('str() :')
    print(str(my_acc))
    print(my_acc)


class ChildAccount(Account):
    def __repr__(self):
        return f'Child account({self.owner}, {self.amount})'


def test2_():
    my_acc = ChildAccount('Nikita',5)

    print('repr() :')
    print(repr(my_acc))

    print('str() :')
    print(str(my_acc))
    print(my_acc)
