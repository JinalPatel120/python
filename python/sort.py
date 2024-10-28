# bubble sort


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [12, 54, 2, 87, 54, 21]
bubble_sort(arr)

for i in range(len(arr)):
    print(arr[i])


# selection sort


def selectionSort(array, size):

    for s in range(size):
        min_idx = s

        for i in range(s + 1, size):

            if array[i] < array[min_idx]:
                min_idx = i

        (array[s], array[min_idx]) = (array[min_idx], array[s])


data = [7, 2, 1, 6]
size = len(data)
selectionSort(data, size)

print("Sorted Array in Ascending Order is :")
print(data)


# insertion sort


def insertion_sort(list1):

    for i in range(1, len(list1)):

        a = list1[i]

        j = i - 1

        while j >= 0 and a < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1

        list1[j + 1] = a

    return list1


# Driver code
list1 = [7, 2, 1, 6]
print("The unsorted list is:", list1)
print("The sorted new list is:", insertion_sort(list1))
