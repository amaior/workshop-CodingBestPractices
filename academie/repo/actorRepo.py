
from domain.Actor import *
import re
class actorRepo:
    def __init__(self):
        self.__data = self.readFile()
        
    def getRepo(self):
        return self.__data
    
    def readFile(self):
        '''
        function that reads from file
        '''
        s = []
        f = open("actor.csv", "r")
        line = f.readline().strip()
        while len(line) > 0:
            line = line.split(",")
            actor = Actor(int(line[0]), line[1], line[2], line[3], line[4], line[5], int(line[6]), int(line[7]), line[8], line[9])
            self.validateActor(actor)
            s += [actor]
            line = f.readline().strip()
        f.close()
        return s
    
    def validateActor(self, actor):
        '''
        validates the input of an actor
        raises value error if it is not what expected
        '''
        if re.match("^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$", actor.getPhone()) == None:
            raise ValueError("Phone nb must contain 10 digits!")
        if re.match("^.+@.+\..+$", actor.getEmail()) == None:
            raise ValueError("Invalid email!")
        if re.match("^[0-9]+$", str(actor.getWeight())) == None:
            raise ValueError("Invalid weight!")
        if re.match("^[0-9]+$", str(actor.getHeight())) == None:
            raise ValueError("Invalid height!")
        if re.match("^[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]$", actor.getBirthDate()) == None:
            raise ValueError("Invalid date!")
        
        return
    def storeFile(self, actor):
        '''
        function that writes into a file
        '''
        self.validateActor(actor)
        f = open("actor.csv", "w")
        actors = self.__data
        for s in actors:
            f.write(str(s.getActorId()) +',' + s.getName() +',' + s.getPrenume() +',' + str(s.getBirthDate()) +',' + s.getNationality() +',' + s.getCity() +',' + str(s.getHeight()) +',' + str(s.getWeight()) +',' + s.getEmail() +',' + s.getPhone()+ '\n')

        '''for s in actors:
            if Actor(sentence.split(" "), len(sentence.split(" "))) == s:
                raise ValueError("Actor already exists!")
        '''   
        f.write(str(actor.getActorId()) +',' + actor.getName() +',' + actor.getPrenume() +',' + str(actor.getBirthDate()) +',' + actor.getNationality() +',' + actor.getCity() +',' + str(actor.getHeight()) +',' + str(actor.getWeight()) +',' + actor.getEmail() +',' + actor.getPhone()+ '\n')
        #actor = actor.split(" ")
        #self.__data.append(Actor(actor, len(sentence)))
        f.close()
        
    def saveDataToFile(self):
        '''
        function that writes into a file
        '''
        f = open("actor.csv", "w")
        actors = self.__data
        for s in actors:
            f.write(str(s.getActorId()) +',' + s.getName() +',' + s.getPrenume() +',' + str(s.getBirthDate()) +',' + s.getNationality() +',' + s.getCity() +',' + str(s.getHeight()) +',' + str(s.getWeight()) +',' + s.getEmail() +',' + s.getPhone()+ '\n')
        f.close()
        