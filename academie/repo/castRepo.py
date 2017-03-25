
from domain.Cast import *

class castRepo:
    def __init__(self):
        self.__data = self.readFile()
        
    def getRepo(self):
        return self.__data
    
    def readFile(self):
        '''
        function that reads from file
        '''
        s = []
        f = open("cast.csv", "r")
        line = f.readline().strip()
        while len(line) > 0:
            line = line.split(",")
            s += [Cast(line[0], line[1], line[2])]
            line = f.readline().strip()
        f.close()
        return s
 
    def saveDataToFile(self):
        '''
        function that writes into a file
        '''
        f = open("cast.csv", "w")
        movies = self.__data
        for s in movies:
            f.write(str(s.getCastId()) +',' + str(s.getActorId()) +',' + str(s.getMovieId()))
            f.write('\n') 
        f.close()
