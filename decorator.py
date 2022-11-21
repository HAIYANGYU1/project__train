
def my_decorater(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@my_decorater
def say_hi():
    print("hello")


if __name__ == "__main__":
    say_hi()