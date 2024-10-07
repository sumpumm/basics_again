def hash(func):
    def wrapper():
        print("#"*5)
        func()
        print("#"*5)
    return wrapper

def star(func):
    def wrapper():
        print("*"*5)
        func()
        print("*"*5)
    return wrapper

@hash
@star
def hello():
    print("hello world")
    
hello()