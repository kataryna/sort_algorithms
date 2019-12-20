"""
Abstract Class for sorting algorithms
"""
from abc import ABC, abstractmethod


class AbstractSort(ABC):
    def __init__(self):
        """
        Abstract Class for sorting algorithms
        """
        self.name=''

    @abstractmethod
    def sort(self, unsorted_list) :
        """
        :param unsorted_list: unsorted list of integers
        :return: sorted list
        """

        raise NotImplementedError

