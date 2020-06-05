class Administration(Employee):

    vacation = 0
    def __init__(self, name, cpr, hours, salary, vacation):
        super.__name = name
        super.__cpr = cpr
        super.__hours = hours
        super.__salary = salary
        self.__vacation = vacation
    @property
    def vacation(self):
        return self.__vacation