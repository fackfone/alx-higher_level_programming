class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("Hello, how are you doing ", self.name, " and you are ", self.age)

if __name__ == '__main__':
    p = Person("Evans", 25)
    p.say_hi()


