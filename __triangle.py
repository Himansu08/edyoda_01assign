class Shape:
    def _init_(self, sides):
        self.sides = sides

    def validate_triangle(self):
        if (self.sides[0] + self.sides[1] > self.sides[2] and
            self.sides[1] + self.sides[2] > self.sides[0] and
            self.sides[2] + self.sides[0] > self.sides[1]):
            print("Valid Triangle")
        else:
            print("Invalid Triangle")

    def validate_rectangle(self):
        if self.sides[0] == self.sides[2] and self.sides[1] == self.sides[3]:
            print("Valid Rectangle")
        else:
            print("Invalid Rectangle")


a = Shape([int(x) for x in input().split()])
b = Shape([int(x) for x in input().split()])

a.validate_triangle()
b.validate_rectangle() 