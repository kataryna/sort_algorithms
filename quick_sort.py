"""
File contains quick sort algorithm
"""
from abstract_sort import AbstractSort

class QuickSort(AbstractSort):

    def __init__(self):
        '''
        Class implements quick sort algorithm
        '''
        self.name = 'Quick Sort'

    def sort(self, unsorted_list):
        """
        :param unsorted_list: unsorted list of integers
        :return: sorted list
        """

        if len(unsorted_list) <= 1:
            # if our list has one element, you have nothing to do
            return unsorted_list

        current = 0
        for i in range(1, len(unsorted_list)):

            if unsorted_list[i] <= unsorted_list[0]:
                current += 1
                unsorted_list[i], unsorted_list[current] = unsorted_list[current],unsorted_list[i]

        unsorted_list[0], unsorted_list[current] = unsorted_list[current], unsorted_list[0]
        left = self.sort(unsorted_list[0:current])
        right = self.sort(unsorted_list[current + 1:len(unsorted_list)])
        unsorted_list = left + [unsorted_list[current]] + right
        #print(unsorted_list)
        return unsorted_list
