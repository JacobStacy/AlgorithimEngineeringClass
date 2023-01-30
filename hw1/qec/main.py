# Complete the monolithRotation function below.
def monolithRotation(matrix, r):
    pass

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0]) # Number of rows

    n = int(mnr[1]) # Number of columns

    r = int(mnr[2]) # Number of rotations

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    monolithRotation(matrix, r)

