def merge_sort(arr, depth=0):
    indent = "  " * depth  # indentation for visualization
    print(f"{indent}Sorting: {arr}")

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid], depth + 1)
    right_half = merge_sort(arr[mid:], depth + 1)

    merged = merge(left_half, right_half, depth + 1)
    print(f"{indent}Merged: {merged}")
    return merged

def merge(left, right, depth):
    indent = "  " * depth
    print(f"{indent}Merging {left} and {right}")

    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    print(f"{indent}Result: {merged}")
    return merged

print(3 // 2)
# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("\nFinal sorted array:", sorted_arr)
