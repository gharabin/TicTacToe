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

def checkend(Mat):
    for i in range(len(Mat)):
        if Mat[i] == ['X']*len(Mat):
            return 1
        elif [Mat[j][i] for j in range(len(Mat))] == ['X']*len(Mat):
            return 1
        elif [Mat[j][j] for j in range(len(Mat))] == ['X']*len(Mat):
            return 1
        elif [Mat[i][-i-1] for i in range(len(Mat))] == ['X']*len(Mat):
            return 1
        if Mat[i] == ['X']*len(Mat):
            return 1
        elif [Mat[j][i] for j in range(len(Mat))] == ['X']*len(Mat):
            return 1
        elif [Mat[j][j] for j in range(len(Mat))] == ['X']*len(Mat):
            return 1
        elif [Mat[i][-i-1] for i in range(len(Mat))] == ['X']*len(Mat):
            return 1
        else:
            return 0

def endmessage(end):
    if end == 1:
        print('X has won the game!')
    elif end == 2:
        print('Y has won the game!')
