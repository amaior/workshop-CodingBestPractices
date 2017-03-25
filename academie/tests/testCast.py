import unittest
from domain.Cast import Cast

class CastTest(unittest.TestCase):
    '''
    Unit test case for Cast
    '''
    def setUp(self):
        self.m = Cast(1,2,3)
        
    def testCast(self):
        self.assertEqual(self.m.getMovieId(), 3)
        self.assertEqual(self.m.getActorId(),2)
        self.assertEqual(self.m.getCastId(), 1)
        self.m.setMovieId(2)
        self.assertEqual(self.m.getMovieId(), 2)
        self.m.setActorId(3)
        self.assertEqual(self.m.getActorId(), 3)
        self.m.setCastId(9)
        self.assertEqual(self.m.getCastId(),9)