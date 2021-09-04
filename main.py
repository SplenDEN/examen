class Tomato:
    states = {1:'small', 2:'midle', 3:'high'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._state += 1

    def is_ripe(self):
        if self._state == 3:
            print('Томат созрел')

class TomatoBush(Tomato):

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range (1, num)]

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        for i in self.tomatoes:
            i.is_ripe()
        return True

    def give_away_all(self):
        self.tomatoes.clear()
        print(self.tomatoes)

class Gardener(TomatoBush):

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print('Ещё зелёные, подожди чуть-чуть')

    @staticmethod
    def knowleadge_base():
        print('Садовнику уже 70 лет')

if __name__ == '__main__':
    Gardener.knowleadge_base()
    a=TomatoBush(5)
    ololo = Gardener('Andrey',a)
    ololo.work()
    ololo.harvest()
