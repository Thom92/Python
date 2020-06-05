class Employee(Person):

    hours = 0
    salary = 0

    def __init__(self, name, cpr, hours, salary):
        self.__name = name
        self.__cpr = cpr
        self.__hours = hours
        self.__salary = salary
    @property
    def hours(self):
        return self.__hours
    @property    
    def salary(self):
        return self.__salary       
    
