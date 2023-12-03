
def thereIsSymbol(i,j,arr):
    pos = [(i+1, j), (i-1,j), (i+1, j+1), (i-1, j-1), (i,j+1), (i, j-1), (i-1, j+1), (i+1, j-1)]
    indices = []
    for p in pos:  
        if p[0]>= 0 and p[1] >=0 and p[0] <len(arr) and p[1]<len(arr[0]):
            if arr[p[0]][p[1]] == '*':
                indices.append((p[0], p[1]))
    return indices
        

 # {gear positions --> [numbers]}
 #        
def solvePuzzle():
    # Using readlines()
    file1 = open('input.txt', 'r')    
    sum = 0
    lines = []

    sum = 0
    
    while True:
        line = file1.readline()
        if not line:
            break

        line = line.strip()
        lines.append(line)
    file1.close()

    gearsToNums = {}


    for i in range(len(lines)):
        j = 0
        while(j < len(lines[0])):
            if lines[i][j].isdigit():
                #get number
                k = j 
                currentGearPositions = set()
                currNum = []    
                adjacent = False
                while k<len(lines[0]) and lines[i][k].isdigit():
                    currNum.append(int(lines[i][k]))
                    #check if there is symbol somewhere
                    gearInd = thereIsSymbol(i,k,lines)
                    for g in gearInd:
                        currentGearPositions.add(g)

                    k += 1
                num = int(''.join(map(str,currNum)))

                for g in currentGearPositions:
                    if g in gearsToNums:
                        gearsToNums[g].append(num)
                    else:
                        gearsToNums[g] = [num]
                j = k
            
            j+=1
    for g in gearsToNums.keys():
        if len(gearsToNums[g]) !=2:
            pass
        else: 
            sum += (gearsToNums[g][0] * gearsToNums[g][1])
    
    print(sum)
            #if there is a symbol nearby, add number to sum

if __name__ == "__main__":
    solvePuzzle()