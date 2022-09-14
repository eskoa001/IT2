import randomArr, time, json

number = 1000000

randomArr = randomArr.randomArr(number)

def countingSort(arr, unique):
    number = [0]*unique
    sorted = []
    for x in arr:
            number[x] += 1
    i = 0
    while i < len(number):
        k = 0
        while k < number[i]:
            sorted.append(i)
            k += 1
        i += 1
    return sorted
    
start = time.time()
tmpArr = countingSort(randomArr, number)
end = time.time()
print(f"Tid brukt: {end - start}")
print(tmpArr[-1])
