class Person:
   
    name = ""
    cpr = ""

    def __init__(self, name, cpr):
        self.name = name
        self.cpr = cpr
     
    def __repr__(self):
        return "\nName: " + self.name + " CPR: " + self.cpr  

class Employee(Person):

    hours = 0
    salary = 0

    def __init__(self, name, cpr, hours, salary):
       super().__init__(name, cpr)
       self.hours = hours
       self.salary = salary
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

    vacation = True
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

 

      
list = []
person1 = Member("Frederik Lumberger", "920328-0923", True)
person2 = Member("Nick", "293928-2392", True)   
person3 = Member("Yo", "0923233", False)
person4 = Instructor("Hello", "2392302", 37, 23000)    
person5 = Administration("Hi", "0239023", 37, 23000, True)
list.append(person1)
list.append(person2)
list.append(person3)
list.append(person4)
list.append(person5)
print(list)
person = Person
for person in list: 
    if isinstance(person, Employee): 
         if isinstance(person, Administration):
                 a = Administration()
                 print("\nName: " + a.name + "\nCpr: " + a.cpr + "\nSalary: " + a.salary + "\nHours: " + a.hours + "\nVacation: " + a.vacation)
                 continue
         elif isinstance(person, Instructor):
                i = Instructor
                print("\nName: " + i.name() + "\nCpr: " + i.cpr + "\nSalary: " + i.salary + "\nHours: " + i.hours)
                continue
                
                e = Employee()
                print("\nName: " + e.getName() + "\nCpr: " + e.getCpr() + "\nHours: " + e.getHours() + "\nSalary: " + e.getSalary())
            
        
    
       
