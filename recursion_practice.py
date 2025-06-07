def merge_sort(arr, depth=0):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left_arr = merge_sort(arr[:middle], depth +1)
    right_arr = merge_sort(arr[middle:], depth + 1)
    print(left_arr, right_arr , depth)

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
# print("\nFinal sorted array:", sorted_arr)
