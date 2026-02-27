def threeWayPartition(arr, a, b):
    n = len(arr)
    low = 0
    mid = 0
    high = n - 1
    
    while mid <= high:
        if arr[mid] < a:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
            
        elif arr[mid] >= a and arr[mid] <= b:
            mid += 1
            

        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            
    return arr

array = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
lowVal = 10
highVal = 20
print(threeWayPartition(array, lowVal, highVal))