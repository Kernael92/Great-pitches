import unittest
from app.models import Pitch

class PitchTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Pitch class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_pitch = Pitch(1,"Brightfunnel","Brightfunnel is a marketing attribution platform designed to help marketers understand the true value of their marketing touches and their impact on the revenue and buyer’s journey.")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))