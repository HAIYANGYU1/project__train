class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def do_something(self):
        print("something")

class Developer(Person):
    def do_something(self):
        print("dontdosomething")

if __name__ == "__main__":
    tom = Person("tom",22)
    tom.do_something()
    mike = Developer("mike",33)
    mike.do_something()
