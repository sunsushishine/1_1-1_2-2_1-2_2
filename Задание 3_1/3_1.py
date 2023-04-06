class Animal:
    name = ""
    def __init__(self):
        print("Родилось животное")

    def eat(self):
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

# Создаем животных
animal1 = Animal()
cat1 = Cat()
dog1 = Dog()
dog2 = Dog()
dog3 = Dog()

# Даем имена животным
animal1.setName("Стив")
cat1.setName("Барсик")
dog1.setName("Шарик")
dog2.setName("Бобик")
dog3.setName("Тузик")
# Вызываем методы eat и makeNoise для каждого животного
animal1.eat()
animal1.makeNoise()

cat1.eat()
cat1.makeNoise()

dog1.eat()
dog1.makeNoise()

dog2.eat()
dog2.makeNoise()

dog3.eat()
dog3.makeNoise()
