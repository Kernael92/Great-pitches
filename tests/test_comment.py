import unittest
from app.models import Comment

class CommentTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Comment class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_comment = Comment(1,"It's precise and straight to the point,bravo!")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))