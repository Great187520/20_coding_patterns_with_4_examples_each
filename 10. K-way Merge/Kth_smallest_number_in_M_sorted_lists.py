from heapq import *

def find_Kth_smallest(lists, k):
    minHeap = []

    for i in range(len(lists)):
        heappush(minHeap, (lists[i][0], 0, i))

    poppedoff = 0
    while minHeap:
        number, currIndex, listIndex - heappop(minHeap)

        poppedOff += 1

        if poppedoff == k:
            return number
        if currIndex + 1 < len(lists[listIndex]):
            heappush(minHep, (lists[listIndex][currIndex + 1], currIndex + 1, listIndex))
    return -1

def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5))) #4
    
    print("Kth smallest number if: "+
          str(find_Kth_smallest([[5, 8, 9], [1,7]], 3))) #7
    
    print("We should fail this as in we sholud see -1")
    print("Kth smallest number is: "+
          str(find_Kth_smallest([[5, 8, 9],[1, 7]], 6))) #-1
main()