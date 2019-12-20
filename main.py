from abstract_sort import AbstractSort
from bubble_sort import BubbleSort
from quick_sort import QuickSort
from heap_sort import HeapSort
from python_sort import PythonSort

from sort_time_complexity import SortTimeComplexity

if __name__ == '__main__':
    stc = SortTimeComplexity()
    stc.run_sorter_tests(BubbleSort())
    stc.run_sorter_tests(QuickSort())
    stc.run_sorter_tests(HeapSort())
    stc.run_sorter_tests(PythonSort())
    stc.display_plot()