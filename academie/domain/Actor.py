
class Actor:
    
    def __init__(self, idi, name, prenume, birthDate, nationality, city, height, weight, email, phone):
        '''
        Constructor for Actor class
        '''
        self.__name = name
        self.__prenume = prenume
        self.__actorId = idi
        self.__birthDate = birthDate
        self.__nationality = nationality
        self.__city = city
        self.__height = height
        self.__weight = weight
        self.__email = email
        self.__phone = phone
        
    '''
    Setting attribute methods
    '''
    def setName(self, name):
        self.__name = name
    
    def setPrenume(self, prenume):
        self.__prenume = prenume
    
    def setActorId(self, idi):
        self.__actorId = idi
    
    def setBirthDate(self, date):
        self.__birthDate = date
    
    def setNationality(self, nationality):
        self.__nationality = nationality
    
    def setCity(self, city):
        self.__city = city
    
    def setHeight(self, height):
        self.__height = height
    
    def setWeight(self, weight):
        self.__weight = weight
        
    def setEmail(self, email):
        self.__email = email
    
    def setPhone(self, phone):
        self.__phone = phone
    '''
    Getting attribute methods
    '''
    
    def getName(self):
        return self.__name
    
    def getPrenume(self):
        return self.__prenume
    
    def getActorId(self):
        return self.__actorId
    
    def getBirthDate(self):
        return self.__birthDate
    
    def getNationality(self):
        return self.__nationality
    
    def getCity(self):
        return self.__city
    
    def getHeight(self):
        return self.__height
    
    def getWeight(self):
        return self.__weight
        
    def getEmail(self):
        return self.__email
        
    def getPhone(self):
        return self.__phone
    
    def __str__(self):
        '''
        Overrides the str() built-in function
        '''
        r = ""
        r += "Actor: " + str(self.__actorId)+ ". " + self.__name + " " + self.__prenume
        r += "\nBirth date: "+  str(self.__birthDate) +" " 
        r += "\nNationality: " + self.__nationality 
        r += "\nCity: " + self.__city
        r += "\nHeight & Weight: " + str(self.__height) +"m "+ str(self.__weight) +"kg"
        r += "\nEmail: " + self.__email +" "
        r += "\nPhone: "  + self.__phone
        return r

