import unittest
from domain.Actor import Actor
from repo.actorRepo import actorRepo
class ActorRepoTest(unittest.TestCase):
    '''
    Unit test case for actorrepo
    '''
    def setUp(self):
        self.actor = actorRepo()
        
    def testCastRepo(self):
        
        self.assertEqual(len(self.actor.getRepo()), 4)
        