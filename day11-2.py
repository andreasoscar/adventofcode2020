ins = []
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        ins.append(line.replace("\n",  ""))
height,length = len(ins),len(ins[0])
for i in range(height):
    tmp = ['0']
    for j in range(length):
        if ins[i][j] == "L":
            tmp.append("#")
        else:
            tmp.append(ins[i][j])
    ins[i] = tmp + ['0']
ins.insert(0,['0']*(length+2))
ins.insert(len(ins),['0']*(2+length))
def findadj(i,j):
    nbr = 0
    if not ins[i][j] == ".":
        for x in range(i-1,i+2,1):
            for y in range(j-1,j+2,1):
                if (x,y) != (i,j):
                    if ins[x][y] == "#":
                        nbr += 1
    return nbr
def findnew(i,j):
    nbr = 0
    row, col = i,j
    if not ins[i][j] == ".":
        for x in range(i-1,0,-1):
            if ins[x][j] == "#" or ins[x][j] == "L":
                nbr += 1
                break
        for x in range(i+1,height+1):
            if ins[x][j] == "#" or ins[x][j] == "L":
                nbr += 1
                break
        for y in range(j-1,0,-1):
            if ins[i][y] == "#" or ins[i][y] == "L":
                nbr += 1
                break
        for y in range(j+1,length+1):
            if ins[i][y] == "#" or ins[i][y] == "L":
                nbr += 1
                break
        for y in range(j-1,0,-1):
            if row > 1:
                row = row - 1
            else:
                break
            if ins[row][y] == "#" or ins[row][y] == "L":
                nbr += 1
                break
        row = i
        for y in range(j+1,length+1):
            if row > 1:
                row = row - 1
            else:
                break
            if ins[row][y] == "#" or ins[row][y] == "L":
                nbr += 1
                break
        row = i
        for y in range(j-1,0,-1):
            if row<height+1:
                row = row + 1
            else:
                break
            if ins[row][y] == "#" or ins[row][y] == "L":
                nbr += 1
                break
        row = i
        for y in range(j+1,length+1):
            if row<height+1:
                row = row + 1
            else:
                break
            if ins[row][y] == "#" or ins[row][y] == "L":
                nbr += 1
                break
    return nbr
while True:
    for i in ins:
        print(i)
    print("----------------------------")
    a, gl,adj,findNe = 0,0,[],[]
    for i in range(1,height+1):
        for j in range(1,length+1):
            if ins[i][j] == ("#"):
                a += 1
    for i in range(1,height+1):
        new = []
        for j in range(1,length+1):
            new.append(findadj(i,j))
        adj.append(['0'] + new + ['0'])
    adj.insert(0,['0']*(length+2))
    adj.insert(len(adj),[0]*(length+2))
    for i in range(1,height+1):
        new = []
        for j in range(1,length+1):
            new.append(findnew(i,j))
        findNe.append(['0'] + new + ['0'])
    findNe.insert(0,['0']*(length+2))
    findNe.insert(len(findNe),[0]*(length+2))
    for i in range(1,height+1):
        tmp = []
        for j in range(1,length+1):
            if adj[i][j] >= 5 and ins[i][j] == "#":
                tmp.append("L")
            elif findNe[i][j] == 0 and ins[i][j] == "L":
                tmp.append("#")
            else:
                tmp.append(ins[i][j])
        ins[i] = ['0'] + tmp + ['0']
    for i in range(1,height+1):
        for j in range(1,length+1):
            if ins[i][j] == "#":
                gl += 1
    if gl == a:
        print(gl)
        break
