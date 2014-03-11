# def isRotation(s1, s2):
#     if len(s1) != len(s2):
#         return False

#     if not s1 or not s2:
#         return False

#     s2 = s2 * 2
#     return s2.find(s1) != -1

def isRotation(s1, s2):
    '''check if s1 is a rotation of s2'''
    if len(s1) != len(s2):
        return False

    if not s1 or not s2:
        return False

    return (s2 * 2).find(s1) != -1
    

if __name__ == '__main__':
    words = ( ('erbottlewa', 'waterbottle'),
              ('erbottlewat', 'waterbottle'),
              ('copa', 'apoc'),
              ('nick', 'nik'),
              ('', ''),
              (' ', ' ') )

    for w1, w2 in words:
        print('isRotation({}, {}): {}'.format(w1, w2, isRotation(w1, w2)))
