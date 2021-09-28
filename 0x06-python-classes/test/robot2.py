#!/usr/bin/python3
class Robot:
    
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return "Robot(\""+ self.name + "\"," + str(self.build_year) + ")"

if __name__ == "__main__":
    x = Robot("Jikzi", 1978)
    
    x = repr(x)
    print(x)
    print("Type of x_str:", type(x))
    new = eval(x)
    print(new)
    print("Type of x_str:", type(new))

