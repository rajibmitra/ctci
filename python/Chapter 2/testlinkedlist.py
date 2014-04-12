import unittest
from classes.linkedlist import *
from removeduplicates import *

class TestNode(unittest.TestCase):
    def testStrRepr(self):
        '''The string representation of a node should be the expected'''
        n = Node(3)
        self.assertEqual(str(n), '3')

    def testValue(self):
        '''The value of a node should be the expected'''
        n = Node(8)
        self.assertEqual(n, 8)

    def testNoLink(self):
        '''The next node of a new node should be None'''
        n = Node(1)
        self.assertEqual(n.next, None)

class TestLinkedList(unittest.TestCase):
    def testSizeNewList(self):
        '''The size of a fresh list with one node should be 1'''
        ml = LinkedList(4)
        self.assertEqual(len(ml), 1)

    def testSizeFilledList(self):
        '''The size of a list with known number of inserted elements should be the expected'''
        ml = LinkedList(0)
        [ml.append(i) for i in range(1, 5)]
        self.assertEqual(len(ml), 5)

    def testRemoveDupl(self):
        '''removeDupl must remove all duplicates from known structures'''
        orig = [38, -5, 14, 8, 8, 8, 7, -5, 38, 9, 38]
        exp  = [38, -5, 14, 8,       7,         9    ]
        ml = LinkedList(orig[0])
        [ml.append(i) for i in orig[1:]]
        removeDupl(ml)
        self.assertEqual(str(ml), str(exp))

    def testRemoveDuplNoBuf(self):
        '''removeDuplNoBuf must remove all duplicates from known structures'''
        orig = [38, -5, 14, 8, 8, 8, 7, -5, 38, 9, 38]
        exp  = [38, -5, 14, 8,       7,         9    ]
        ml = LinkedList(orig[0])
        [ml.append(i) for i in orig[1:]]
        removeDuplNoBuf(ml)
        self.assertEqual(str(ml), str(exp))

if __name__ == '__main__':
    unittest.main()
