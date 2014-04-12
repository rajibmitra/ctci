from classes.linkedlist import *

def removeDupl(ml):
    '''Remove duplicates using a temporary buffer'''
    found = set()
    n = ml.head
    prev = None
    while n:
        # if the current node already exists "remove" it
        if n.data in found:
            assert prev, 'prev should not be None'
            prev.next = n.next
        # remember the visited nodes
        else:
            found.add(n.data)
            prev = n
        n = n.next

def removeDuplNoBuf(ml):
    '''Remove duplicates without a temporary buffer'''
    n = ml.head
    while n:
        r = n                   # the runner node
        while r.next:
            if r.next == n:
                r.next = r.next.next
            else:
                r = r.next
        n = n.next

if __name__ == '__main__':
    ml = LinkedList(0)
    for i in (0, 3, 4, 0, 3, 18, 9, 18, 7, 4, 12):
        ml.append(i)
    print(ml)
    removeDupl(ml)
    print(ml)
