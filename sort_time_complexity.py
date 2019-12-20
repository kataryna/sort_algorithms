"""
Class to measure execution time for given sort algorithms
"""

import time
import matplotlib.pyplot as plt
import random
from copy import deepcopy
from abstract_sort import AbstractSort


class SortTimeComplexity:

    def __init__(self):
        """
        Class to measure execution time for given sort algorithms
        """
        self.test_data_lengths: list[int]= [3, 10, 20, 30, 50, 70, 100,200]
        self.count_for_mean: int = 3
        self.algorithms: list[str] =[]
        self.test_data: list[list[int]] = []
        self.generate_data_to_tests()

    @staticmethod
    def generate_random_list(length :int) -> list:
        """
        generates a list of integers of the given length
        :param length: length of random list
        :return: random list of integers
        """
        return [random.randint(1,1000) for _ in range(length)]

    def generate_data_to_tests(self):
        """
        method generates random data set and save it in self.test_data (samole data to run tests)
        :return: set lists of integers (every list in this set has longer length)
        """
        for length in self.test_data_lengths:
            self.test_data.append(self.generate_random_list(length))

    def measure_time(self, sorter: AbstractSort, unsorted_list: list) -> float:
        """
        :param sorter: object of chosen sort method algorithm
        :param unsorted_list: list of input data
        :return: mean measurement of algorithm execution time [in mili seconds]
        """
        start = time.time()
        # give deepcopy of test data list to algorithm (every sort method uses the same data to tests)
        sorter.sort(deepcopy(unsorted_list))
        end = time.time()
        return (end - start) * 1000

    def measure_mean_time(self, sorter: AbstractSort, unsorted_list: list) -> float:
        """
        :param sorter: object of chosen sort method algorithm
        :param unsorted_list: list of input data
        :return: measurement of algorithm execution time [in seconds]
        """
        times = [self.measure_time(sorter, unsorted_list) for _ in range(self.count_for_mean)]
        result = sum(times) / self.count_for_mean
        return result

    def run_sorter_tests(self, sorter: AbstractSort):
        """
        :param sorter: object of chosen sort method algorithm
        :return: adds results of measurement to plot
        """
        self.algorithms.append(sorter.name)

        times=[]
        for i, length in enumerate(self.test_data_lengths):
            times.append(self.measure_mean_time(sorter, self.test_data[i]))
        plt.plot(self.test_data_lengths, times)

    def display_plot(self):
        """
        :return: displays plot for all chosen sorter algorithms
        """
        plt.xlabel('length of sorted list')
        plt.ylabel('execution time[ms]')
        plt.title('Execution time of sort algorithm')
        plt.legend(self.algorithms)
        plt.grid(True)
        plt.show()
