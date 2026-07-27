class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def talk(self):
        print(f"Hello, my first name is {self.fname} and my last name is {self.lname}.")


person1 = Person("Anthony", "Evans")
person1.talk()

person2 = Person("John", "Smith")
person2.talk()

person3 = Person("Bob", "Doe")
person3.talk()
