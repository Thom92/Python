class Instructor(Employee):

  
    def __init__(self, name, cpr, hours, salary):
        super.__name = name
        super.__super = name
        self.__hours = hours
        self.__salary = salary
    @property
    def hours(self):
        return self.__hours
    @property    
    def salary(self):
        return self.__salary       
    
