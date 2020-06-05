class Person:
    name = ""
    cpr = ""
    def __init__(self, name, cpr):
        self.__name = name
        self.__cpr = name
    
    @property
    def name(self):
        return self.name
    @property    
    def cpr(self):
        return self.cpr 
    def _str_(self):
        return "\nName: " + name + "Cpr: " + cpr
