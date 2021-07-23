class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("wee, this is fun")
        elif self.ratio == 1:
            print("TRhis is hard work but Im flying")
        else:
            print("I think Ill just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on it, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()

class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("come on in but it's bit chilly this far south")

    def quack(self):
        print("A don't quack I'm a penguin")


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
    # test_duck(donald)
    #
    # percy = Penguin()
    # test_duck(percy)