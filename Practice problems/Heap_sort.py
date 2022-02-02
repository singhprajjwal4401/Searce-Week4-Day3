def heapify(arr, n, i):
    largest = i #initalize the largest at root
    l = 2*i+1
    r = 2*i+2

    if l<n and arr[largest] < arr[l]: #check if left node exist
        largest = l

    if r<n and arr[largest] < arr[r]: #check if right node exist
        largest =r

    if largest != i: #change root
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)
#sort the array
def heapSort(arr):
    n = len(arr)
    #max_heap 
    for i in range(n//2-1, -1, -1):
         heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i] ,arr[0] = arr[0], arr[i] # swap the elements in heap
        heapify(arr, i ,0)
# main driver code
arr = [12,11,3,6,9]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i],end=" ")
