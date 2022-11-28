# Given an array arr. Return True if it is an almost sorted array, and False if it's not.
# arr is almost sorted if there is an element arr[i] such that the rest of the array are sorted.
# i.e. arr[0] <= arr[1] <= ... <= arr[i-2] <= arr[i-1] <= arr[i+1] <= arr[i+2] <= ... <= arr[n-2] <= arr[n-1]
# https://leetcode.com/discuss/interview-question/1717779/google-onsite-almost-sorted-array



def almost_sorted(arr):

    def helper(i, j):

        if arr[i-2] > arr[i]:
            return False
        
        while i + 1 < j:
            if arr[i + 1] < arr[i]:
                return False
            i += 1
        return True

    i = 0
    j = len(arr)
    while i + 1 < j:
        
        if arr[i + 1] < arr[i]:
            return helper(i + 2 , j)
        i += 1
    
    return True



print(almost_sorted([3,5,10,6,14]))
True
print(almost_sorted([3,5,3,10,6,14]))
False
print(almost_sorted([3,5,3,6,13,14]))
True
print(almost_sorted([3,5,3,6,13,14,20,15]))
False
print(almost_sorted([3,5,3,6,13,14,20,150]))
True
