size = int(input('Please input your board size: '))

Mat = []
for i in range(size):
    Mat.append(['E']*size)

def printboard(Mat):
    for i in Mat:
        print(i)
    return None

def movex(r,c,Mat):
    if r>size or c>size:
        print("Invalid Move")
    else:
        Mat[r][c] = "X"
    return None

def movey(r,c,Mat):
    if r>size or c>size:
        print("Invalid Move")
    else:
        Mat[r][c] = "Y"
    return None
