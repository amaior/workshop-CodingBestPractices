
from domain.Actor import *
from domain.Movie import *
from controller.movieController import *
from controller.actorController import *

class UI:
    def __init__(self, movieController, actorController,castController):
        self._actorController = actorController
        self._movieController = movieController
        self._castController = castController
        
    def printMenu(self):
        string = '\nAvailable commands:\n'
        string += '\t 1 - Add actor\n'
        string += '\t 2 - Add movie\n'
        string += '\t 3 - Remove an actor\n'
        string += '\t 4 - Remove a movie\n'
        string += '\t 5 - Display all actors\n'
        string += '\t 6 - Display all movies\n'
        string += '\t 7 - Display an actor\n'
        string += '\t 8 - Display a movie\n'
        string += '\t 0 - Exit\n'
        print(string)
    
    def mainMenu(self):
        keepalive = True
        while keepalive:
            try:
                UI.printMenu(self)
                command = input("Enter command: ").strip()
                if command == '0':
                    print("Good bye!")
                    keepalive = False
                elif command == '1':
                    idi = input("Give the id: ")
                    name = input("Give the name of the actor: ")
                    prenume = input("Give the first name of the actor: ")
                    birth = input("Give his birth date: ")
                    nationality = input("Give his nationality: ")
                    city = input("Give his city: ")
                    weight = input("Give his weight: ")
                    height = input("Give his height: ")
                    email = input("Give his email: ")
                    phone = input("Give his phone: ")
                    
                    m = Actor(idi, name, prenume, birth, nationality, city, weight, height, email, phone)
                    self._actorController.add(m)
                elif command == '2':
                    idi = input("Give the id: ")
                    title = input("Give the title of the movie: ")
                    apparition = input("Give the apparition of the movie: ")
                    web = input("Give the website of the movie: ")
                    '''leng = int(input("Give how many actors play in the movie"))
                    actors = []
                    for i in range(0,leng):
                        actors.append(input("Give an actor: "))
                    '''
                    m = Movie(idi, title, apparition, web)
                    self._movieController.add(m)
                elif command == '3':
                    name = input("Give the name of the actor: ")
                    actor = self._actorController.findActorByName(name)
                    self._actorController.delete(actor.getActorId())
                    self._castController.deleteByActor(actor.getActorId())
                elif command == '4':
                    title = input("Give the title of the movie: ")
                    movie = self._movieController.findMovieByTitle(title)
                    self._movieController.delete(movie.getMovieId())
                    self._castController.deleteByMovie(movie.getMovieId())
                elif command == '5':
                    for n in self._actorController.getAll():
                        print(str(n))
                        print('\n')
                elif command == '6':
                    for n in self._movieController.getAll():
                        print(str(n))
                        print('\n')
                elif command == '7':
                    name = input("Give the name of the actor: ")
                    actor = self._actorController.findActorByName(name)
                    ok = 0
                    for n in self._castController.getAll():
                        if int(n.getActorId()) == int(actor.getActorId()):
                            if ok == 0:
                                print(str(actor))
                                print ("plays in: ")
                            ok = 1 
                            movie = self._movieController.findMovieById(int(n.getMovieId()))
                            print(movie.getTitle() + " ")
                    if ok == 0:
                        print("actor plays in no movie!")
                elif command == '8':
                    title = input("Give the title of the movie: ")
                    movie = self._movieController.findMovieByTitle(title)
                    ok = 0
                    for n in self._castController.getAll():
                        if int(n.getMovieId()) == int(movie.getMovieId()):
                            if ok == 0:
                                print(str(movie))
                                print("has the cast: ")    
                            ok = 1
                            actor = self._actorController.findActorById(int(n.getActorId()))
                            print(actor.getName() + " " + actor.getPrenume() + ' ')
                    if ok == 0:
                        print("movie has no cast!")
                        
                else:
                    print("Invalid command!")
            except Exception as exc:
                print("Error encountered - "+str(exc))
            except ValueError as exc:
                print("Error encountered - "+str(exc))
                
    def printList(self,l):
        print("List is:")
        for c in l:
            print(str(c))