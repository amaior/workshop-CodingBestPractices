
from repo.actorRepo import *

class actorController:
    def __init__(self, repo):
        self.__repo = repo
    
    def add(self, actor):
        '''
        adds a new actor in file
        input:the actor
        '''
        self.__repo.storeFile(actor)
        self.__repo.getRepo().append(actor)
        
    
    def delete(self, idi):
        '''
        removes an actor from the file
        input:the id
        '''
        poz = 0
        for i in self.__repo.getRepo():
            if i.getActorId() == idi:
                self.__repo.getRepo().pop(poz)
            poz += 1
        self.__repo.saveDataToFile()
        
    def getAll(self):
        '''
        returns the entire repository
        '''
        return self.__repo.getRepo()
    
    def findActorByName(self, name):
        '''
        returns the actor with the given name
        raises error if it doesn't exist
        '''
        for a in self.getAll():
            if a.getName() == name:
                return a
        raise ValueError("Actor does not exist!")
    
    def findActorById(self, idi):
        '''
        returns the actor with the given id
        raises error if it doesn't exist
        '''
        for a in self.getAll():
            if a.getActorId() == idi:
                return a
        raise ValueError("Actor does not exist!")