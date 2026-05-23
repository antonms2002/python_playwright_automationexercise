class Car():
    number_of_wheels = 4

    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color
        self.print_name_and_wheels()

    def print_name_and_wheels(self):
        print(self.name, self.number_of_wheels)

    def track(self):
        self.number_of_wheels = 6

    @classmethod
    def print_number_of_wheel(cls):
        print(cls.number_of_wheels)

mercedes = Car("m", 1500, "blue")

# mercedes.track()
# mercedes.print_name_and_wheels()
# mercedes.print_number_of_wheel()
# print(mercedes.__dict__)