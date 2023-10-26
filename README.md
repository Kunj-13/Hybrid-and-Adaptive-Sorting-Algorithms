# Hybrid-and-Adaptive-Sorting-Algorithms         - Kunj Patel
Project 1 - 463 - Includes Source code and Project Report

Hybrid Sorting Algorithm Benchmarking and Performance Analysis

Project Goals
- Implement and benchmark a hybrid sorting algorithm that combines Quick Sort and Selection Sort.
- Validate the correctness of the hybrid sorting algorithm through rigorous testing.
- Compare the performance of the hybrid sorting algorithm with Quick Sort and Selection Sort in terms of execution time and memory usage.
- Analyze the benchmarking results and discuss the performance of the algorithms, both numerically and theoretically.

Algorithm Description
For this project, I developed a hybrid sorting algorithm that uses a threshold to switch between Quick Sort and Selection Sort. A hybrid sorting algorithm is a technique for merging different sorting algorithms into a single algorithm. A hybrid sorting algorithm integrates two or more sorting approaches and use heuristics to select the best sorting method for a given input. Here, I'll describe a hybrid sorting algorithm that combines Merge Sort and Selection Sort while optimizing the sorting process with heuristics. Here's a quick rundown of the algorithm:

Hybrid Sorting Algorithm
  - If the input array size is below a specified threshold, the algorithm uses Selection Sort.
  - If the array size is above the threshold, it employs Quick Sort.

Quick Sort
  - A standard implementation of the Quick Sort algorithm.
  - It recursively partitions the array into smaller subarrays, sorts those subarrays, and combines them to achieve a sorted array.
    
Selection Sort
  - A simple sorting algorithm that iteratively selects the smallest element from the unsorted part of the array and places it at the beginning.

Benchmarking Results
The project conducts a series of benchmarking experiments to compare the performance of the hybrid sorting algorithm with Quick Sort and Selection Sort. It measures execution time and memory usage for each algorithm.

Here are the average benchmarking results based on 10 runs for each algorithm:

Hybrid Sort
  - Average Execution Time: 0.017751 seconds
  - Average Memory Usage: 2.56 MB

Quick Sort
  - Average Execution Time: 0. 017843 seconds
  - Average Memory Usage: 3.172 MB

Selection Sort
  - Average Execution Time: 5.656104 seconds
  - Average Memory Usage: 2.13 MB

Discussion on Performance
- Execution Time: The benchmarking results show that Quick Sort typically performs the best in terms of execution time. Quick Sort is well-known for its efficient average-case performance. Selection Sort, on the other hand, is significantly slower due to its quadratic time complexity.

- Memory Usage: It can be observed from the benchmark results that Quick Sort required more memory due to its recursive nature, which lead to stack space usage. Selection Sort typically uses less memory as it doesn't involve recursion. The hybrid algorithm's memory usage fell between the two.

- Threshold Selection: The threshold value used in the hybrid algorithm significantly impacts its performance. A lower threshold may favor Selection Sort for smaller arrays, while a higher threshold may favor Quick Sort. Careful selection of the threshold is crucial to achieve optimal performance.

- Theoretical Analysis: Quick Sort has an average time complexity of O(n log n) and a worst-case time complexity of O(n^2), while Selection Sort has a time complexity of O(n^2). The hybrid algorithm is expected to perform well for both small and large arrays, combining the strengths of both algorithms. The threshold should be selected based on the expected input size distribution.

- Conclusion: The hybrid sorting algorithm shows promise in terms of performance optimization by demonstrating its adaptability to a variety of input sizes. The sorting technique used (Quick or Selection) is determined by the input size, and the benchmarking results reveal the trade-offs between execution time and memory use. While quick sort continues to outperform selection sort in terms of execution speed, the selection sort outperformes memory usage wise. Both can be very useful in different contexts. Lastly, This is where hybrid sorting algorithm can be practical, as they assist in the selection of algorithms depending on individual requirements amd sort of provides a nice balance between the memory usage and execution time. 

