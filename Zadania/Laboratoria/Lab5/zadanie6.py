class Dog:
    count = 0
    dogs = []

    def __init__(self, name):
        self.name = name
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self, n):
        print("{} says: {}".format(self.name, "Woof! " * n))

    @staticmethod
    def print_count_name():
        print("Count: {}".format(Dog.count))
        print("Name dogs: {}".format(Dog.dogs))
        print()


dog1 = Dog("Burek")
Dog.print_count_name()

dog2 = Dog("Jurek")
Dog.print_count_name()

dog3 = Dog("Reksio")
Dog.print_count_name()
