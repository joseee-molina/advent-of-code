def solvePuzzle():
    # Using readlines()
    file1 = open('input.txt', 'r')   
    sum = 0 

    numsDict = {}
    #indicates number of copy cards per number
    maxReach = 1
    additional = 0
    
    while True:
        line = file1.readline()
        if not line:
            break

        line = line.strip()
        line = line.split()
        i = 2
        currCard = int(line[1][0:len(line[1])-1])
        

        winning  = set()
        while i< len(line):
            if line[i] == '|':
                break
            winning.add(line[i])
            i+=1
        i+=1
        wCount = 0
        while i<len(line):
            if line[i] in winning:
                wCount+=1
            i+=1
        
        if maxReach < currCard+wCount:
            maxReach = currCard + wCount

        if currCard not in numsDict:
            numsDict[currCard] = 1
        
        currentInstances = 0
        currentInstances += numsDict[currCard]
        
        
        k = 1
        while k<=wCount:
            if (currCard + k) not in numsDict:
                numsDict[currCard + k] = currentInstances+1
            else:
                numsDict[currCard + k] += currentInstances
            k+=1
        if currCard==maxReach+1 and wCount == 0:

            break

    file1.close()
    sum = 0
    print(numsDict)
    for k in numsDict.keys():
        sum+= numsDict[k]
    
    print(sum)

if __name__ == "__main__":
    solvePuzzle()