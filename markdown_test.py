import unittest
from markup import *

class TestParser(unittest.TestCase):


    def setUp(self):
        self.x = Parser(Handler())


    def tearDown(self):
        pass


    def testInit(self):
        """
        Парсер должен иметь обработчик, список правил и список фильтров
        """

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
