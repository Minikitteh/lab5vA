#Yamel Hernandez
#80590552
#CS 2302
#Diego Aguirre
#Anindita Nath
#Lab 5 ver A
#Purpose of this lab was to understand how heaps
# & heapsort work, using a min-heap

from Heap import Heap

############################################################
###################  functions  ############################

#heapsort
def heap_sort(list):
    result = []
    heap = Heap()
    for elem in list:
        heap.insert(elem)
    while not heap.is_empty():
        result.append(heap.extract_min())
    return result


#read a file seperated by commas & print in a sorted sequence


############################################################
def main():
    use = "/home/yamel/Desktop/CS3/lab5/labtext"
    H = Heap()
    with open(use) as f:
        for line in f:
            info = line.split(',')
            for i in info:
                H.insert(i)
    print(H.extract_min())
    
main()

