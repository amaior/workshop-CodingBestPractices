
from repo.castRepo import *

class castController:
    def __init__(self, repo):
        self.__repo = repo
    
    def add(self, cast):
        '''
        adds a new cast in file
        input:the cast
        '''
        self.__repo.getRepo().append(cast)
        self.__repo.saveDataToFile()
    
    def deleteByMovie(self, idi):
        '''
        removes an cast from the file
        input:the movie id
        '''
        poz = 0
        for c in self.__repo.getRepo():
            if int(c.getMovieId()) == int(idi):
                self.__repo.getRepo().pop(poz)
            poz += 1
        self.__repo.saveDataToFile()
        
    def deleteByActor(self, idi):
        '''
        removes an cast from the file
        input:the actor id
        '''
        poz = 0
        for c in self.__repo.getRepo():
            if int(c.getActorId()) == int(idi):
                self.__repo.getRepo().pop(poz)
            poz += 1
        self.__repo.saveDataToFile()
        
    def getAll(self):
        '''
        returns the entire repository
        '''
        return self.__repo.getRepo()
