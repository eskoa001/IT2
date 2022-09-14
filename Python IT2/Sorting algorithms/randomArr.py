import random

filePath = "Sorting algorithms/randomNumbers.txt"

def randomArr(number):

    with open(filePath,'w') as file:
        pass

    f = open(filePath, "a")
    for x in range(number):
        f.write(str(random.randrange(1,number)) + "\n")
    f.close()

    f = open(filePath, "r")

    randomArr = []

    for x in range(number):
        number = f.readline().replace('\n',"")
        randomArr.append(int(number))
    
    return randomArr