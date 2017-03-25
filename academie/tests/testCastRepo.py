import unittest
from domain.Cast import Cast
from repo.castRepo import castRepo
class CastRepoTest(unittest.TestCase):
    '''
    Unit test case for castrepo
    '''
    def setUp(self):
        self.cast = castRepo()
        
    def testCastRepo(self):
        
        self.assertEqual(len(self.cast.getRepo()), 2)
        