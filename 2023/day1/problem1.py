def getNum(i, line):
    if i+3 <=len(line) and line[i:i+3]=="one":
        return 1
    
    if i+3 <=len(line) and line[i:i+3]=="two":
        return 2

    if i+5 <=len(line) and line[i:i+5]=="three":
        return 3
    if i+4 <=len(line) and line[i:i+4]=="four":
        return 4
    if i+4 <=len(line) and line[i:i+4]=="five":
        return 5
    if i+3 <=len(line) and line[i:i+3]=="six":
        return 6
    if i+5 <=len(line) and line[i:i+5]=="seven":
        return 7
    if i+5 <=len(line) and line[i:i+5]=="eight":
        return 8
    if i+4 <=len(line) and line[i:i+4]=="nine":
        return 9
    if i+4 <=len(line) and line[i:i+4]=="zero":
        return 0
    return -1

def solvePuzzle():
    # Using readlines()
    file1 = open('input.txt', 'r')    
    sum = 0
    
    while True:
        line = file1.readline()
        if not line:
            break

        line = line.strip()
        for i in range(len(line)):
            if line[i].isdigit():
                num1 = int(line[i])
                break
            tryingChar = getNum(i,line)
            if tryingChar!=-1:
                num1 = tryingChar
                break
            

        i = len(line)-1
        while i>=0:
            if line[i].isdigit():
                num2 = int(line[i])
                break
            tryingChar = getNum(i,line)
            if tryingChar!=-1:
                num2 = tryingChar
                break
            i -= 1
        print(num1)
        print(num2)
        print("----")
        sum = sum + num2 + 10*num1
 
    file1.close()
    print(sum)

if __name__ == "__main__":
    solvePuzzle()