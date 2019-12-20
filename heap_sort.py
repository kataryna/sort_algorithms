"""
Class uses heap structure(imported class) to sort elements in list
"""
from abstract_sort import AbstractSort
from heapq import heappush, heappop

class HeapSort(AbstractSort):

    def __init__(self):
        """
        Class implements min heap sort algorithm
        """
        self.name = 'Heap Sort'

    def sort(self, unsorted_list):
        # print('we',unsorted_list)
        result_list = []
        # making min heap from unsorted_list
        heap_list = []
        for element in unsorted_list:
            heappush( heap_list, element)
        # takes off the top of heap (always the smallest element in set)
        for _ in range(len(unsorted_list)):
            result_list.append(heappop(heap_list))
        #print('wy',result_list)
        return result_list
