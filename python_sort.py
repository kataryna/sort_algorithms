"""
File contains sort algorithm
"""
from abstract_sort import AbstractSort

class PythonSort(AbstractSort):

    def __init__(self):
        """
        Class implements sort algorithm based on function sorted (used to test and comp)
        """
        self.name = 'function sorted'

    def sort(self, unsorted_list):
        """
        :param unsorted_list: unsorted list of integers
        :type unsorted_list: list
        :return: sorted list[int]
        """
        return sorted(unsorted_list)