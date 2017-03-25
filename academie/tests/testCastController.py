import unittest
from controller.castController import castController
from domain.Cast import Cast
from repo.castRepo import castRepo
class CastControllerTest(unittest.TestCase):
    '''
    Unit test case for MovieController
    '''
    def setUp(self):
        self.cast = castRepo()
        self.m = castController(self.cast)
        
    def testCastController(self):
        
        self.assertEqual(len(self.m.getAll()), 4)
        self.m.add(Cast(1,2,3))
        self.assertEqual(len(self.m.getAll()), 5)
        self.m.deleteByActor(1)
        self.assertEqual(len(self.m.getAll()), 3)
        self.m.deleteByMovie(1)
        self.assertEqual(len(self.m.getAll()), 2)