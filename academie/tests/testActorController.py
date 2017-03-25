
import unittest
from controller.actorController import actorController
from domain.Actor import Actor
from repo.actorRepo import actorRepo
class ActorControllerTest(unittest.TestCase):
    '''
    Unit test case for ActorController
    '''
    def setUp(self):
        self.actor = actorRepo()
        self.m = actorController(self.actor)
        
    def testActorController(self):
        
        self.assertEqual(len(self.m.getAll()), 4)
        self.m.add(Actor('3',"Ana", "Pop", "11/12/1992", "english", "Cluj", 52,96,"ana@g.com","0755555555"))
        self.assertEqual(len(self.m.getAll()), 5)
        self.m.delete(3)
        self.assertEqual(len(self.m.getAll()), 4)
        a = self.m.findActorById('3')
        self.assertEqual(a.getName(),"Ana")
        a = self.m.findActorByName("Ana")
        self.assertEqual(a.getActorId(), '3')