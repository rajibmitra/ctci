import unittest
from tozeros import *

class TestToZeros(unittest.TestCase):
    def testEmpty(self):
        '''tozeros must return empty for empty matrices'''
        self.assertEqual(tozeros([[]]), [[]])

    def testSingle(self):
        '''tozeros must return the original for 1x1 matrices'''
        self.assertEqual(tozeros([[7]]), [[7]])

    def testDouble(self):
        '''tozeros must return the expected for 2x2 matrices'''
        orig = [ [0, 1],
                 [2, 3] ]

        exp  = [ [0, 0],
                 [0, 3] ]

        self.assertEqual(tozeros(orig), exp)

    def testTwoByThree(self):
        '''tozeros must return the expected for 3x4 matrices'''
        orig = [ [1, 2,  0, 4],
                 [5, 6,  7, 8],
                 [9, 10, 11, 12] ]

        exp  = [ [0, 0,  0, 0],
                 [5, 6,  0, 8],
                 [9, 10, 0, 12] ]

        self.assertEqual(tozeros(orig), exp)

    def testMoreTwoZeros(self):
        '''tozeros must return the expected for matrices with > 1 zeros'''
        orig = [ [1,  2,  3,   4],
                 [5,  0,  7,   8],
                 [9,  10, 11,  12],
                 [13, 14, 15,  0] ]

        exp =  [ [1,  0,  3,   0],
                 [0,  0,  0,   0],
                 [9,  0,  11,  0],
                 [0,  0,  0,   0] ]

        self.assertEqual(tozeros(orig), exp)

if __name__ == '__main__':
    unittest.main()

