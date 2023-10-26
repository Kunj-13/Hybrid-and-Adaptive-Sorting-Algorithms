
import random
import time
import psutil

# Hybrid Sorting Algorithm
def hybrid_sort(arr, threshold=10):
    if len(arr) < threshold:
        return selection_sort(arr)  # Use selection sort for small arrays
    else:
        return quick_sort(arr)  # For larger arrays, use Quick Sort

# Implementing Quick Sort to sort arrays
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Implementing Selection Sort to sort arrays
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Generate and sort some input arrays
input_arrays = [
    [5, 3, 1, 4, 2],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [100, 200, 300, 400, 500],
]
# Displays the arrays that we sorted
for input_arr in input_arrays:
    sorted_arr = hybrid_sort(input_arr.copy())
    print("Input:", input_arr)
    print("Sorted Output:", sorted_arr)
    print()


# Testing - Validate the correctness of the hybrid sorting algorithm
def test_sorting_algorithm():
    for _ in range(100):
        arr = [random.randint(1, 1000) for _ in range(1000)]
        hybrid_result = hybrid_sort(arr.copy())
        sorted_result = sorted(arr.copy())
        assert hybrid_result == sorted_result, "Sorting algorithm failed"

# Benchmarking - Compare the performance of sorting algorithms by measuring memory usage and execution time
def benchmark_sorting_algorithm(sort_func, name):
    execution_times = []
    memory_usages = []

    for _ in range(10):  # Run the benchmark 10 times and average the results
        arr = [random.randint(1, 1000) for _ in range(10000)]
        memory_usage_before = psutil.virtual_memory().used
        start_time = time.time()
        sort_func(arr)
        end_time = time.time()
        memory_usage_after = psutil.virtual_memory().used

        execution_times.append(end_time - start_time)
        memory_usages.append(memory_usage_after - memory_usage_before)

    avg_execution_time = sum(execution_times) / len(execution_times)
    avg_memory_usage = sum(memory_usages) / len(memory_usages)

    print(f"{name} - Avg Execution Time: {avg_execution_time:.6f} seconds, Avg Memory Usage: {avg_memory_usage / (1024 * 1024):.2f} MB")

# Testing sorting algorithm for correctness
test_sorting_algorithm()

# Benchmarking - Compare the performance of the hybrid sorting algorithm with Quick Sort and Selection Sort
benchmark_sorting_algorithm(hybrid_sort, "Hybrid Sort")
benchmark_sorting_algorithm(quick_sort, "Quick Sort")
benchmark_sorting_algorithm(selection_sort, "Selection Sort")


