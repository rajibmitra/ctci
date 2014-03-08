def showAsMatrix(mat):
    [print(i) for i in mat]

def tozeros(seq):
    PATTERN = 0

    rowlen = range(len(seq))
    colen = range(len(seq[0]))

    rowReset = [False for _ in rowlen]
    colReset = [False for _ in colen]

    # first pass, mark the pattern
    for r in rowlen:
        for c in colen:
            if seq[r][c] == PATTERN:
                rowReset[r] = colReset[c] = True

    # second pass, modify the sequence in place
    for r in rowlen:
        for c in colen:
            if rowReset[r] or colReset[c]:
                seq[r][c] = 0

    return seq


if __name__ == '__main__':
    matrix = [ [18, 0, 27, -5],
               [4, -7, 12,  1],
               [28, 1, 9,   0] ]

    showAsMatrix(matrix)
    tozeros(matrix)
    print()
    showAsMatrix(matrix)
