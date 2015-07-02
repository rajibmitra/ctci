from classes.linkedlist import *

def deleteNode(n):
    if not n or not n.next:
        return

    n.data = n.next.data
    n.next = n.next.next

if __name__ == '__main__':
    ml = LinkedList(1)
    [ml.append(i) for i in range(2, 6)]
    print(ml)
    n = ml.kth(3)
    deleteNode(n)
    print(ml)
