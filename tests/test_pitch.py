import unittest
from app.models import Pitch,User
from app import db
class PitchTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Pitch class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.user_Kernaeljoy = User(username = 'Kernaeljoy', password = 'berry', email = 'kerryjojo5@gmail.com')
        self.new_pitch = Pitch(1,"Brightfunnel","Brightfunnel is a marketing attribution platform designed to help marketers understand the true value of their marketing touches and their impact on the revenue and buyer’s journey.",'Kernaeljoy')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_id,1)
        self.assertEquals(self.new_pitch.pitch_name,'Brightfunnel')
        self.assertEquals(self.new_pitch.pitch_description,'Brightfunnel is a marketing attribution platform designed to help marketers understand the true value of their marketing touches and their impact on the revenue and buyer’s journey.')
        self.assertEquals(self.new_pitch.user,self.user_Kernaeljoy)
    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)
    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitches = Pitch.get_pitches(1)
        self.assertTrue(len(got_pitches) == 1)       
