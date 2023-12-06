def getSeeds(lines):
    seeds = []
    lines = lines.split('\n')
    lines = lines[0].split()
    i = 1
    while i<len(lines):
        seeds.append(int(lines[i]))
        i+=1
    return seeds

def getMappingFromTo(lines, whatToWhat):
    getSeedToSoilMap = {}
    lines = lines.split('\n')
    
    i = lines.index(whatToWhat)
    i+=1
    seedToSoil = []
    while lines[i] != '':
        seedToSoil.append([int(x) for x in lines[i].split()])
        i+=1
    
    return seedToSoil

def seedToFinal(seed, finalArr):
    minVal =float('inf')
    
    previous = seed
    for somethingToSomething in finalArr:
        
        #seed to soil
        finalValue = previous
        for conversion in somethingToSomething:
            #mapings
            if previous >= conversion[1] and previous<(conversion[1] + conversion[2]):
                extra = previous-conversion[1]
                finalValue = conversion[0] + extra
                break
        previous = finalValue
    

    return finalValue

def solvePuzzle():
    # Using readlines()
    file1 = open('input.txt', 'r')    
    lines = ""
    while True:
        line = file1.readline()
        if not line:
            break

        line = line.strip()
        lines += line + '\n'
 
    file1.close()
    print()
    seeds = getSeeds(lines)
    #print(seeds)
    finalArr = []
    seedToSoil = getMappingFromTo(lines, 'seed-to-soil map:')
    finalArr.append(seedToSoil)
    soilToFertilizer = getMappingFromTo(lines, 'soil-to-fertilizer map:')
    finalArr.append(soilToFertilizer)

    fertilizerToWater = getMappingFromTo(lines, 'fertilizer-to-water map:')
    finalArr.append(fertilizerToWater)

    waterToLight = getMappingFromTo(lines, 'water-to-light map:')
    finalArr.append(waterToLight)

    lightToTemperature = getMappingFromTo(lines, 'light-to-temperature map:')
    finalArr.append(lightToTemperature)

    temperatureToHumidity = getMappingFromTo(lines, 'temperature-to-humidity map:')
    finalArr.append(temperatureToHumidity)

    humidityToLocation = getMappingFromTo(lines, 'humidity-to-location map:')
    finalArr.append(humidityToLocation)

    
    #print(finalArr)
    #print(seeds)
    i = 0
    minVal = float('inf')
    seedToValues = {}
    while i<len(seeds):
        k = 0
        #print(i)
        upperLim = seeds[i+1]
        currAdvanced = 0
        while k<upperLim:
        #while k<10:
            
            finalVal = seedToFinal(seeds[i]+k, finalArr)
            if finalVal < minVal:
                minVal = finalVal
                #print(minVal)
            #print(k, " ", minVal, " ",finalVal, " ", seeds[i+1], " ", currAdvanced)            
            k+=1
        i+=2

    print(minVal)
    

if __name__ == "__main__":
    solvePuzzle()