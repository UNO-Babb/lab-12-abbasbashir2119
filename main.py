# main.py
import time
import random
import AllSorts

def test_sorting_algorithms():
    random.seed(2020)
    numberTerms = 1000  # use 10000 if your system can handle it

    orderedList = list(range(numberTerms))
    reversedList = list(range(numberTerms, 0, -1))
    randomList = [random.randint(1, 10000) for _ in range(numberTerms)]

    datasets = {
        "Ordered": orderedList,
        "Reversed": reversedList,
        "Random": randomList
    }

    sorting_algorithms = {
        "Bubble Sort": AllSorts.bubbleSort,
        "Bubble Sort (Early Exit)": AllSorts.bubbleSortEarlyExit,
        "Selection Sort": AllSorts.selectionSort,
        "Insertion Sort": AllSorts.insertionSort,
        "Merge Sort": AllSorts.mergeSort
    }

    for sort_name, sort_func in sorting_algorithms.items():
        print(f"\n--- {sort_name} ---")
        for data_name, data in datasets.items():
            test_data = data.copy()
            start = time.time()
            sort_func(test_data)
            end = time.time()
            print(f"{data_name} List Time: {end - start:.5f} seconds")

if __name__ == '__main__':
    test_sorting_algorithms()
