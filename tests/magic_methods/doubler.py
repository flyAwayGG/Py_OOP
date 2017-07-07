class DOUBLER_5000:
    def __init__(self, list):
        self.__list = [x*2 for x in list]

    def __len__(self):
        return len(self.__list)

    def __getitem__(self, position):
        return self.__list[position]

    def __reversed__(self):
        return self.__list[::-1]

    # Операторы сравнения
    def __eq__(self, other): # ==
        pass

    def __le__(self, other): # <=
        pass

    def __lt__(self, other): # <
        pass

    def __ge__(self, other): # >=
        pass

    def __gt__(self, other): # >
        pass

    # Арифметические операторы
    def __add__(self, other): # +
        pass

    # Объект можно выполнять как функцию
    def __call__(self):
        return "Call me any way you want"



def test_():
    l = DOUBLER_5000([1, 2, 3, 4, 5])
    print('len(): '+ str(len(l)))
    print('get by index: '+ str(l[2]))
    print('reversed(): '+ str(reversed(l)))
    print('callable '+ l())



