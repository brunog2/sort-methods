from math import ceil

def sort(array, i, n):
    print(array, i, n, '\n')

    print(f'Verifying {array[i]} and {array[i+n]}')
    if array[i] > array[i+n]:
        print(f'Swap {array[i]} and {array[i+n]}\n')
        tmp = array[i]

        array[i] = array[i+n]
        array[i+n] = tmp

    if i + n == len(array) - 1:
        if n > 1: return sort(array, 0, n-1)
        return array

    return sort(array, i+1, n)
        
        
# [5, 2, 3, 4, 7, 8, 9]
# n / 2 = 3 (espaço)
# i = 0   

array = [5, 2, 3, 4, 7, 8, 9]
n = ceil(len(array)/2)



print(sort(array, 0, n))