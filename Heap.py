#heap class
class Heap:
    def __init__(self):
        self.heap_array = []
        
    def insert(self, k):
        self.heap_array.append(k)
        index = (len(self.heap_array)-1) #starts at last index
        while(index -1) //2 >=0: #parent in bounds
            if self.heap_array[index] < self.heap_array[(index-1) //2]:#rearranges for minheap property
                parentTemp = self.heap_array[(index-1)//2]
                self.heap_array[(index-1) // 2] = self.heap_array[index]
                self.heap_array[index] = parentTemp
            index = index // 2        
        return self.heap_array
    
    def extract_min(self):
        if self.is_empty():
            return None
        min_elem = self.heap_array[0]#1st element is min
        self.heap_array[0] = self.heap_array[len(self.heap_array)-1]#moves last element up
        self.heap_array.pop(len(self.heap_array)-1)  #makes last empty
        i =0
        while (2 * i + 2) < len(self.heap_array)-1: #while right child in bounds
            if self.heap_array[2 * i + 1] > self.heap_array[2 * i + 2]: #if left child is greater than right child
                currentMin = 2 * i + 2 #current min is right child
            else:
                currentMin = 2 * i + 1 #current min is left child
            if self.heap_array[i] > self.heap_array[currentMin]: #keeps minheap property
                indexTemp = self.heap_array[i]
                self.heap_array[i] = self.heap_array[currentMin]
                self.heap_array[currentMin] = indexTemp
            i = currentMin
        return self.heap_array
        return min_elem
    
    def is_empty(self):
        return len(self.heap_array) == 0