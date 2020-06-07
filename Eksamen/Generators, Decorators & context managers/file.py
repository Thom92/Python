#Decotrators: wrap a function, modifying its behavior. 
#Decorators can also be used as a way to create getter and setter methods in Python

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def hello_world1():
    print("Hello World!")

say_hello = my_decorator(hello_world1)
hello_world1()

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"
hello_world = return_greeting("World")
print(hello_world)
#Generators: you can create them without building and holding the entire object in memory before iteration. 
#Since Yield sends a value back, but doesn´t exit the function, you can more easily create a save memory space by using generators instead 
#of list comprehensions. It is also used to create data pipelines
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

#Context Manager:
#Context managers: Helps manage resources with the "with" keyword. _enter_() returns the resources, _exit_() does not return anything but performs cleanup.
#Python uses it instead of typical try/catch filereader like other languages.
class FileManager(): 
    def __init__(self, filename, mode): 
        self.filename = filename 
        self.mode = mode 
        self.file = None
          
    def __enter__(self): 
        self.file = open(self.filename, self.mode) 
        return self.file
      
    def __exit__(self, exc_type, exc_value, exc_traceback): 
        self.file.close() 
  
# loading a file  
with FileManager('test.txt', 'w') as f: 
    f.write('Test') 
  
print(f.closed) 
#Decorator: Wraps a function, which means modifying it´s behaviour
