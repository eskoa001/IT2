import randomArr, time

randomArr = randomArr.randomArr()

def bubbleSort(arr):
    while (True):
        j = 1
        isSorted = True
        for i in range(0, len(arr)-j, 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = False
        if isSorted == True:
            return arr
        j += 1


start = time.time()
tmpArr = bubbleSort(randomArr)
end = time.time()
print(tmpArr)
print(f"Tid brukt: {end - start}")