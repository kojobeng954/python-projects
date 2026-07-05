class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello, my name is {self.name}.")


john = Person("John Smith")
john.talk()

bob = Person("Bob Johnson")
bob.talk()
