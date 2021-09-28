class Robot:

    def __init__(self, name=None, year=None):
        self.name = name
        self.year = year

    def say_hi(self):
        if self.name:
            print("Greetings, I am {} and was created in {:d}.".format(self.name, self.year))
        else:
            print("Hi, I am a robot without a name {}.")

    def set_name(self, name):
        self.name = name
    
    def set_year(self, year):
        self.year = year

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year


x = Robot()
x.set_name("Fone")
x.year = 1975
x.say_hi()

y = Robot()
y.set_name(x.get_name())
y.year = 2003
print(y.get_name())
