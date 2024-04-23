class Square:
    
    def __init__(self):
        self.height = 0

    def area(self):
        return self.height * self.height
    
my_shape = Square()
my_shape.height = 10
print(my_shape.area())