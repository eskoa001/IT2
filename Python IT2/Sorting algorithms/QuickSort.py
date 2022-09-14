import randomArr, time

number = 15

randomArr = randomArr.randomArr(number)


#skjønte endelig hvordan denne funka så kan mekke den i it2 timen 
#trenger ikke splitte, bare jobbe med mindre og mindre deler av arrayen

def quickSort(arr):
    pivot = arr[-1]
    i = 0
    k = len(arr)-1
    while(i+1 < k):   
        if arr[i] <= pivot:
            i += 1
        if arr[k] >= pivot: 
            k -= 1
        else:
            print(f" Pointer1: {i} = {arr[i]} \n Pivot: {pivot} \n Pointer2: {k}  = {arr[k]} ")
            arr[i], arr[k] =  arr[k], arr[i]    
            print(arr)  
            print("\n")
            
    print(i, arr[i])
    print(k, arr[k])
    #arr[-1], arr[i+1] =  arr[i+1], arr[-1] 
    print(arr)  
    print(k>pivot)
print(randomArr)
quickSort(randomArr)
