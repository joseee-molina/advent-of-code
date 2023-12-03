def solvePuzzle():
    # Using readlines()
    file1 = open('input.txt', 'r')    
    red = 12
    green = 13
    blue  = 14
    sum = 0

    while True:
        line = file1.readline()
        if not line:
            break
        line = line.strip()
        spaces = line.split()
        id = int(spaces[1][0:len(spaces[1])-1])
        games = line.split(';')
        poss = True
        
        maxRed = 0
        maxGreen = 0
        maxBlue= 0
        for game in games:
            game = game.split()
            redCount = 0
            greenCount = 0
            blueCount = 0

            

            for i in range(len(game)):
                if "red" in game[i]:
                    redCount += int(game[i-1])
                if "blue" in game[i]:
                    blueCount += int(game[i-1])
                if "green" in game[i]:
                    greenCount += int(game[i-1])

            if redCount> maxRed:
                maxRed = redCount
            if greenCount> maxGreen:
                maxGreen = greenCount
            if blueCount> maxBlue:
                maxBlue = blueCount
       
        sum += maxRed * maxGreen * maxBlue


        
    print(sum)
    file1.close()

if __name__ == "__main__":
    solvePuzzle()