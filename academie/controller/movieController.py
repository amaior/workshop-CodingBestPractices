
from repo.movieRepo import movieRepo
from domain.Movie import Movie

class movieController:
    def __init__(self, repo):
        self.__repo = repo
    
    def add(self, movie):
        '''
        adds a new movie in file
        input:the movie
        '''
        self.__repo.storeFile(movie)
        self.__repo.getRepo().append(movie)
        
    
    def delete(self, idi):
        '''
        removes a movie from the file
        input:the id
        '''
        poz = 0
        for i in self.__repo.getRepo():
            if i.getMovieId() == idi:
                self.__repo.getRepo().pop(poz)
            poz += 1
        self.__repo.saveDataToFile()
        
    def getAll(self):
        '''
        returns the entire repository
        '''
        return self.__repo.getRepo()
    
    def findMovieById(self, idi):
        '''
        returns the movie with the given id
        raises error if it doesn't exist
        '''
        for m in self.getAll():
            if m.getMovieId() == idi:
                return m
        raise ValueError("Movie does not exist!")
    
    def findMovieByTitle(self, title):
        '''
        returns the movie with the given title
        raises error if it doesn't exist
        '''
        for m in self.getAll():
            if m.getTitle() == title:
                return m
        raise ValueError("Movie does not exist!")