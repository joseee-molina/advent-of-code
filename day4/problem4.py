def solvePuzzle():
    # Using readlines()
    file1 = open('input.txt', 'r')   
    sum = 0 
    
    while True:
        line = file1.readline()
        if not line:
            break

        line = line.strip()
        line = line.split()
        i = 2
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
        x = 0
        print(wCount)
        if wCount > 0:
            x = pow(2, wCount-1)
        print(x)
        sum += x
        
 
    file1.close()
    print(sum)

if __name__ == "__main__":
    solvePuzzle()