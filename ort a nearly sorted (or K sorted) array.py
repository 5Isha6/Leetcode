#Sort a nearly sorted (or K sorted) array
# https://www.geeksforgeeks.org/nearly-sorted-algorithm/

def sort_k(arr, n, k):

    heap = arr[: k+1]
    heapify(heap)
    t_idx = 0
    for i in range(k+1, n):
        arr[t_idx] = heappop(heap)
        heappush(heap,arr[i])
        t_idx += 1

    while heap:
        arr[t_idx] = heappop(heap)
        t_idx += 1
    
    return arr


k = 3
arr = [2, 6, 3, 12, 56, 8]
n = len(arr)
print(sort_k(arr, n, k))
 
