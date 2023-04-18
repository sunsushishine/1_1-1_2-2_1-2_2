class Animal:
    name = ""
    def __init__(self):
        print("Родилось животное")

    def eat(self):
        print("")
        print("Ням-ням")

    def getName(self):
        return self.name

    def setName(self, new_name):
        self.name = new_name

    def makeNoise(self):
        print(f"{self.name} говорит Гррр")

class Cat(Animal):
    def __init__(self):
        print("Родился кот")

    def makeNoise(self):
        print(f"{self.name} говорит Мяу")

class Dog(Animal):
    def __init__(self):
        print("Родилась собака")

    def makeNoise(self):
        print(f"{self.name} говорит Гав")

animal_1 = Animal()
cat_1 = Cat()
dog_1 = Dog()
dog_2 = Dog()

animal_1.setName("Абатур")
cat_1.setName("Рыжик")
dog_1.setName("Шарик")
dog_2.setName("Персик")

animal_1.eat()
animal_1.makeNoise()

cat_1.eat()
cat_1.makeNoise()

dog_1.eat()
dog_1.makeNoise()

dog_2.eat()
dog_2.makeNoise()
