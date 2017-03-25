'''
Created on Mar 7, 2017

@author: Le
'''
from domain.Movie import *
import re

class movieRepo:
    def __init__(self):
        self.__data = self.readFile()
        
    def getRepo(self):
        return self.__data
    
    def validateMovie(self, movie):
        '''
        validates the input of an actor
        raises value error if it is not what expected
        '''
        if re.match("^[0-9][0-9][0-9][0-9]$", movie.getApparition()) == None:
            raise ValueError("Invalid apparition year!")
        if re.match(".+\..+", movie.getWebsite()) == None:
            raise ValueError("Invalid website!")
        
    
    def readFile(self):
        '''
        function that reads from file
        '''
        s = []
        f = open("movie.csv", "r")
        line = f.readline().strip()
        while len(line) > 0:
            line = line.split(",")
            '''l = []
            for i in range(3,len(line)):
                l.append(line[i])
            if l==[]:
                raise ValueError("Must enter at least an actor!")
            '''
            movie = Movie(int(line[0]), line[1], line[2], line[3])
            self.validateMovie(movie)
            s += [movie]
            line = f.readline().strip()
        f.close()
        return s
    
    def storeFile(self, movie):
        '''
        function that writes into a file
        '''
        f = open("movie.csv", "w")
        movies = self.__data
        for s in movies:
            f.write(str(s.getMovieId())+ ',' +s.getTitle() +',' + s.getApparition() +',' + s.getWebsite())
            '''for a in s.getActors():
                f.write(',' + a)
            '''
            f.write('\n')
        '''for s in actors:
            if Actor(sentence.split(" "), len(sentence.split(" "))) == s:
                raise ValueError("Actor already exists!")
        '''
        self.validateMovie(movie)   
        f.write(str(movie.getMovieId()) + ',' + movie.getTitle() +',' + movie.getApparition() +',' + movie.getWebsite())
        '''for a in movie.getActors():
            f.write(',' + a)
        '''
        f.write('\n')
        f.close()
        
    def saveDataToFile(self):
        '''
        function that writes into a file
        '''
        f = open("movie.csv", "w")
        movies = self.__data
        for s in movies:
            f.write(str(s.getMovieId())+ ',' +s.getTitle() +',' + s.getApparition() +',' + s.getWebsite())
            f.write('\n')
        f.close()
