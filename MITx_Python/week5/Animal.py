import random

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

    def setAge(self, newage):
        self.age = newage

    def setName(self, newname=""):
        self.name = newname

    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)

class Cat(Animal):
    ##__init__ heredado de Animal
    def speak(self):
        print("meow")

    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)

class Rabbit(Animal):
    def speak(self):
        print("meep")

    def __str__(self):
        return "rabbit:" + str(self.name) + ":" + str(self.age)

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.setName(self, name)
        self.friends = []

    def getFriends(self):
        return self.friends

    def addFriend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("hello")

    def ageDiff(self, other):
        diff = self.getAge() - other.getAge()
        if self.age > other.age:
            print(self.name, "is",diff, "years older than",other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)

    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)


class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def changeMajor(self, major):
        self = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")

    def __str__(self):
        return "student:" + str(self.name) + ":" + str(self.age)