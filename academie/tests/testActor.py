
import unittest
from domain.Actor import Actor

class ActorTest(unittest.TestCase):
    '''
    Unit test case for Actor
    '''
    def setUp(self):
        self.m = Actor(1,"Ana", "Pop", "11/12/1992", "english", "Cluj", 52,96,"ana@g.com","0755555555")
        
    def testActor(self):
        self.assertEqual(self.m.getActorId(), 1)
        self.assertEqual(self.m.getName(), "Ana")
        self.assertEqual(self.m.getPrenume(), "Pop")
        self.assertEqual(self.m.getBirthDate(), "11/12/1992")
        self.assertEqual(self.m.getNationality(), "english")
        self.assertEqual(self.m.getCity(), "Cluj")
        self.assertEqual(self.m.getWeight(), 96)
        self.assertEqual(self.m.getHeight(), 52)
        self.assertEqual(self.m.getEmail(), "ana@g.com")
        self.assertEqual(self.m.getPhone(), "0755555555")
        self.m.setActorId(2)
        self.assertEqual(self.m.getActorId(), 2)
        self.m.setName("Lion")
        self.assertEqual(self.m.getName(), "Lion")
        self.m.setPrenume("Li")
        self.assertEqual(self.m.getPrenume(), "Li")
        self.m.setNationality("roman")
        self.assertEqual(self.m.getNationality(), "roman")
        self.m.setCity("Roman")
        self.assertEqual(self.m.getCity(), "Roman")
        self.m.setWeight(77)
        self.assertEqual(self.m.getWeight(), 77)
        self.m.setHeight(57)
        self.assertEqual(self.m.getHeight(), 57)
        self.m.setBirthDate("11/10/1999")
        self.assertEqual(self.m.getBirthDate(),"11/10/1999")
        self.m.setEmail("web@sh.com")
        self.assertEqual(self.m.getEmail(), "web@sh.com")
        self.m.setPhone("0712345678")
        self.assertEqual(self.m.getPhone(), "0712345678")