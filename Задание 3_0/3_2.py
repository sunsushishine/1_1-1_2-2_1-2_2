class Cat:
    name = ""
    color = ""
    weight = 0
    hungry = 0
    def __init__(self):
        print("Родилась кошка ... без имени")
    def meow(self):
        print("Кошку зовут", self.name)
        if self.hungry == 0: print("Кошка проголодалась")
    def print(self):
        print("Кошку(Кота) зовут {0}".format(self.name))
        print("Цвет кошки(кота) {0}".format(self.color))
        print("Вес кошки(кота) {0} кг.".format(self.weight))
    def set_name(self, input_name):
        self.name = input_name
    def eating(self):
        self.hungry +=1
        print("Кошка ест...")
    def gaming(self):
        if self.hungry != 0:
            self.hungry -= 1
            print("Кошка играет...")
        else: print("Нет сил играть...")

myCat = Cat()
myCat.set_name("Котик")
myCat.gaming()
myCat.meow()
myCat.eating()
myCat.gaming()
myCat.gaming()
myCat.eating()
myCat.gaming()
