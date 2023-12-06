
def solvePuzzle():
    # Using readlines()
    file1 = open('in.txt', 'r')    
    res = 1
    times = []
    dist = []
    t = True
    while True:
        line = file1.readline()
        if not line:
            break
        line = line.strip().split()
        if t:
            for i in range(1, len(line)):
                times.append(int(line[i]))
                t = False
        else:
            for i in range(1, len(line)):
                dist.append(int(line[i]))
        
    time = int(''.join(map(str,times)))
    dist = int(''.join(map(str,dist)))
    print(time)
    print(dist)
    
    #just need to fins the index i, everything between i and t-i beats
    #the distance
    k = 0
    beatsDist = 0

    while k<time:
        newD = calcDist(time,k)

        if newD > dist:
            beatsDist+=1
        k+=1

    file1.close()
    print(beatsDist)

def calcDist(t,k):
    return (t-k)*k
if __name__ == "__main__":
    solvePuzzle()