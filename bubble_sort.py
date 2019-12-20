"""
File contains bubble sort algorithm
"""
from abstract_sort import AbstractSort

class BubbleSort(AbstractSort):
    def __init__(self):
        """
        Class implements bubble sort algorithm
        """
        self.name = 'Bubble Sort'

    def sort(self, unsorted_list):
        """
        :param unsorted_list: unsorted list of integers
        :return: sorted list
        """

        for j in range(len(unsorted_list) - 1):
            for i in range(0, len(unsorted_list) - j - 1):
                if unsorted_list[i] > unsorted_list[i + 1]:
                    unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
        #print(unsorted_list)
        return unsorted_list
