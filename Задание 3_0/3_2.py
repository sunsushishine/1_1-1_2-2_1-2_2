class Cat:
    name = ""
    hungry = 0
    def __init__(self):
        print("Родилась новая кошка ... без имени")
    def meow(self):
        print("Кошка говорит:", self.name)
        if self.hungry == 0: print("Кошка проголодалась...")
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
myCat.set_name("меня зовут Котик")
myCat.gaming()
myCat.meow()
myCat.eating()
