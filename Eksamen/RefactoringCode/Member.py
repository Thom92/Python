class Member(Person):

    isBasic = True
    def __init__(self, name, cpr, isBasic):
        self.__name = name
        self.__cpr = cpr
        self.__isBasic = isBasic

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
    

