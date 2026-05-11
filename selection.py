
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print("\nSorted Array:")
print(arr)



"""
Title
Selection Sort Algorithm in Python

Objective
To sort a list of elements in ascending order using the Selection Sort technique.

Theory
Selection Sort is a simple sorting algorithm used to arrange elements in ascending or descending order. In this method, the smallest element from the unsorted part of the array is selected and placed at the correct position.
The sorting process starts from the first index of the array. The algorithm searches for the minimum element in the remaining unsorted portion of the array. After finding the smallest element, it swaps that element with the current position. This process continues until the entire array becomes sorted.
In this program, the user first enters the number of elements and then inputs all array elements one by one. The algorithm uses two loops:

The outer loop selects the current position.

The inner loop searches for the minimum element.

The variable min_index stores the index of the smallest element found during comparison. After the comparison is completed, swapping is performed using:
arr[i], arr[min_index] = arr[min_index], arr[i]
Selection Sort repeatedly places the correct smallest element at the beginning of the unsorted array. After every pass, one element gets fixed in its correct position.
Important Points

Selection Sort
Simple comparison-based sorting algorithm.
Minimum Element Selection
Finds smallest element in unsorted array.

Swapping
Selected minimum element is swapped with current position.

Outer Loop
Controls number of passes.
Inner Loop
Finds smallest element.


In-Place Sorting
Sorting happens within the same array.


Time Complexity
Best Case: O(n²)
Average Case: O(n²)
Worst Case: O(n²)

Space Complexity
O(1) because no extra array is used.
Stable Sorting
Basic Selection Sort is not stable.

Applications
Small datasets
Educational purposes
Basic sorting understanding

Algorithm
Start the program.
Read number of elements.
Input array elements.
Repeat for each position in array:
Assume current index as minimum.
Compare with remaining elements.
Find smallest element.
Swap smallest element with current element.
Print sorted array.
End the program.


Conclusion
This program implements the Selection Sort algorithm to arrange elements in ascending order. It repeatedly selects the minimum element from the unsorted part of the array and places it in the correct position. The algorithm is simple and easy to understand, making it useful for learning sorting techniques."""