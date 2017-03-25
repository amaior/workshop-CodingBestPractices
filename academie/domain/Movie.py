'''
Created on Mar 7, 2017

@author: Le
'''
class Movie:
    
    def __init__(self, idi, title, apparition, website):
        '''
        Constructor for Movie class
        '''
        self.__title = title
        self.__movieId = idi
        self.__apparition = apparition
        self.__website = website
        
    '''
    Setting attribute methods
    '''
    def setTitle(self, title):
        self.__title = title
    
    def setApparition(self, apparition):
        self.__apparition = apparition
    
    def setMovieId(self, idi):
        self.__movieId = idi

    def setWebsite(self, website):
        self.__website = website
        
    '''
    Getting attribute methods
    '''
    
    def getTitle(self):
        return self.__title
    
    def getApparition(self):
        return self.__apparition
    
    def getMovieId(self):
        return self.__movieId
    
    def getWebsite(self):
        return self.__website

    def __str__(self):
        '''
        Overrides the str() built-in function
        '''
        r = ""
        r += "Movie: " + str(self.getMovieId()) +'. ' +str(self.__title)+ " appeared in " + self.__apparition + " "
        r += "\nWebsite: " + self.__website
        return r
