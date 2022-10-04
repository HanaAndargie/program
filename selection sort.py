#User function Template for python3

class Solution: 
    
    def select(self, arr, i):
        return arr[i]

    def selectionSort(self, arr, n):

        for i in range(len(arr)):
            minpos = arr[i]
            for j in range(i + 1, len(arr)):
                if arr[j] < minpos:
                    minpos = arr[j]
                    arr[i], arr[j] = minpos, arr[i]
        return arr
