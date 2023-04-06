class Cat:
    name = ""
    color = ""
    weight = 0
    hungry = 0
    def __init__(self, input_name, input_color, input_weight):
        self.name = input_name
        self.color = input_color
        self.weight = input_weight
    def meow(self):
        print(self.name, "Говорит мяу")
    def print(self):
        print("Кошку(Кота) зовут {0}".format(self.name))
        print("Цвет кошки(кота) {0}".format(self.color))
        print("Вес кошки(кота) {0} кг.".format(self.weight))

myCat = Cat("Барсик","Черный",3)
myCat.meow()
myCat.print()
myCat.weight = 4
myCat.print()
