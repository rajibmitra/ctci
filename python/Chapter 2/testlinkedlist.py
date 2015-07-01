import unittest
from classes.linkedlist import *
from removeduplicates import *
from kthlast import *

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

    def testKthToLast(self):
        '''kthToLast must return the expected node'''
        ml = LinkedList(8)
        [ml.append(i) for i in (3, -5, 24, 11, -9)]
        self.assertEqual(kthToLast(ml, 0), None)
        self.assertEqual(kthToLast(ml, 6), None)
        self.assertEqual(kthToLast(ml, 1), -9)
        self.assertEqual(kthToLast(ml, 3), 24)

    def testKthToLastRunner(self):
        '''kthToLastRunner must return the expected node'''
        ml = LinkedList(8)
        [ml.append(i) for i in (3, -5, 24, 11, -9)]
        self.assertEqual(kthToLastRunner(ml, 0), None)
        self.assertEqual(kthToLastRunner(ml, 6), None)
        self.assertEqual(kthToLastRunner(ml, 1), -9)
        self.assertEqual(kthToLastRunner(ml, 3), 24)
        

if __name__ == '__main__':
    unittest.main()
