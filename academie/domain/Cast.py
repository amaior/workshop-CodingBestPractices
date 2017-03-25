
class Cast:
    
    def __init__(self, idi, actorId, movieId):
        '''
        Constructor for Actor class
        '''
        self.__castId = idi
        self.__actorId = actorId
        self.__movieId = movieId
    
    '''
    Setting attribute methods
    '''
            
    def setCastId(self, idi):
        self.__castId = idi
        
    def setActorId(self, idi):
        self.__actorId = idi
        
    def setMovieId(self, idi):
        self.__movieId = idi
        
    '''
    Getting attribute methods
    '''
    def getCastId(self):
        return self.__castId
    
    def getActorId(self):
        return self.__actorId
    
    def getMovieId(self):
        return self.__movieId