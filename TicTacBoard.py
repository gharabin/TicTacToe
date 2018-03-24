size = int(input('Please input your board size: '))

Mat = []
for i in range(size):
    Mat.append(['E']*size)

while checkend(Mat) == 0:
