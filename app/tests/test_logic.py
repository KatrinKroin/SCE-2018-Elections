import unittest
from app import app


class LogicTest(unittest.TestCase):

    def setUp(self):
        print 'ok'
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()