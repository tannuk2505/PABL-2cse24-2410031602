def commonElements(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    n1, n2, n3 = len(arr1), len(arr2), len(arr3)
    res = []
    last_found = float('-inf') 

    while i < n1 and j < n2 and k < n3:
        if arr1[i] == arr2[j] == arr3[k]:
            if arr1[i] != last_found:
                res.append(arr1[i])
                last_found = arr1[i]
            i += 1
            j += 1
            k += 1
        
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
            
    return res if res else -1