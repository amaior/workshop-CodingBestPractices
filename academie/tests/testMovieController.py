
import unittest
from controller.movieController import movieController
from domain.Movie import Movie
from repo.movieRepo import movieRepo
class MovieControllerTest(unittest.TestCase):
    '''
    Unit test case for MovieController
    '''
    def setUp(self):
        self.movie = movieRepo()
        self.m = movieController(self.movie)
        
    def testMovieController(self):
        
        self.assertEqual(len(self.m.getAll()), 2)
        self.m.add(Movie(1, "Sherlock", "2000", "sherlock.com"))
        self.assertEqual(len(self.m.getAll()), 3)
        self.m.delete(1)
        self.assertEqual(len(self.m.getAll()), 2)
        a = self.m.findMovieById(3)
        self.assertEqual(a.getTitle(),"Batman")
        a = self.m.findMovieByTitle("Ratatouille")
        self.assertEqual(a.getMovieId(), 2)