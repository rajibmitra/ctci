import unittest
from rotation import *

class TestRotation(unittest.TestCase):
    def testEmpty(self):
        '''isRotation must return false for empty strings'''
        self.assertFalse(isRotation('', ''))

    def testSingle(self):
        '''isRotation must return true for single same-character strings'''
        self.assertTrue(isRotation('a', 'a'))

    def testDouble(self):
        '''isRotation must return true for double same-character strings'''
        self.assertTrue(isRotation('ab', 'ab'))

    def testTrue(self):
        '''isRotation must return true for known rotation strings'''
        words = ( ('erbottlewat', 'waterbottle'),
                  ('hello', 'hello') )

        for w1, w2 in words:        
            self.assertTrue(isRotation(w1, w2))

    def testFalse(self):
        '''isRotation must return true for known non-rotation strings'''
        words = ( ('erbottlewa', 'waterbottle'),
                  ('nick', 'nik'),
                  ('hello', 'hello w') )

        for w1, w2 in words:
            self.assertFalse(isRotation(w1, w2))

if __name__ == '__main__':
    unittest.main()

    
        
