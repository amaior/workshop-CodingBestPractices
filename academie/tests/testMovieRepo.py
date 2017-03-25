import unittest
from domain.Movie import Movie
from repo.movieRepo import movieRepo
class MovieRepoTest(unittest.TestCase):
    '''
    Unit test case for movierepo
    '''
    def setUp(self):
        self.movie = movieRepo()
        
    def testMovieRepo(self):
        
        self.assertEqual(len(self.movie.getRepo()), 2)
        