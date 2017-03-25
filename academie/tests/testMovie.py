
import unittest
from domain.Movie import Movie

class MovieTest(unittest.TestCase):
    '''
    Unit test case for Movie
    '''
    def setUp(self):
        self.m = Movie(1, "Sherlock", "2000", "sherlock.com")
        
    def testMovie(self):
        self.assertEqual(self.m.getMovieId(), 1)
        self.assertEqual(self.m.getTitle(), "Sherlock")
        self.assertEqual(self.m.getApparition(), "2000")
        self.assertEqual(self.m.getWebsite(), "sherlock.com")
        self.m.setMovieId(2)
        self.assertEqual(self.m.getMovieId(), 2)
        self.m.setTitle("Lion")
        self.assertEqual(self.m.getTitle(), "Lion")
        self.m.setApparition("1999")
        self.assertEqual(self.m.getApparition(),"1999")
        self.m.setWebsite("websh.com")
        self.assertEqual(self.m.getWebsite(), "websh.com")