class Person:
    name = ""
    cpr = ""
    def __init__(self, name, cpr):
        self._name = name
        self._cpr = name
    
    @property
    def name(self):
        return self.name
    @property    
    def cpr(self):
        return self.cpr 
    def _str_(self):
        return "\nName: " + name + "Cpr: " + cpr

class Employee(Person):

    hours = 0
    salary = 0

    def __init__(self, name, cpr, hours, salary):
       super().__init__(name, cpr)
       self._hours = hours
       self._salary
    def __getHours(self):
        return self._hours
     
    def _getSalary(self):
        return self._salary      

class Member(Person):

    isBasic = True
    def __init__(self, name, cpr, isBasic):
        super().__init__(name, cpr)
        self._isBasic = isBasic

    def getMemberType(self, isBasic):
        if(isBasic):
            return "Basic Membership"
        else:
            return "Full Membership"        
    
    def basic(self, isBasic):
        isBasic = True

    def monthlyFee(self, isBasic):
        if(isBasic):
            return 199
        else:
            return 299        
        
class Administration(Employee):

    vacation = 0
    def __init__(self, name, cpr, hours, salary, vacation):
        super().__init__(name, cpr, hours, salary)
        self._vacation = vacation
    @property
    def vacation(self):
        return self.__vacation

class Instructor(Employee):
    def __init__(self, name, cpr, hours, salary):
        super().__init__(name, cpr, hours, salary)
    def returnSalary(self, x):
        x = Employee()
        if(x.__getHours == 37):
            return 23000
        else:
            return x._getHours * 456    

    @property    
    def salary(self):
        return self._salary
       
list = []
person1 = Member("Frederik Lumberger", "920328-0923", True)
person2 = Member("Nick", "293928-2392", True)
          


list.append(person1)
list.append(person2)
print(list)
    
       
