from app import create_app,db
from flask_script import Manager,Server
from app.models import PItch



# Creating app instance 
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)
@manager.command
def test():
    '''
    Running the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,Pitch = PItch)


if __name__ == '__main__':
    manager.run()
