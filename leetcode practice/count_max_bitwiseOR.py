''' Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

 An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

 The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed). 
 
 Example:

Input: nums = [3,2,1,5]
Output: 6
Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]

    steps :
    find all subsets of the array
    calculate the bitwise OR for each subset
    then count how many subsets yield the maximum bitwise OR
 '''


from itertools import combinations


def count_max_bitwiseOR(arr):

    def calculate_bitwise_or(subset):
        result = 0
        for num in subset:
            result |= num
        return result

    # find all bitwise OR combinations
    bitwise_or_list = []
    for i in range(1, len(arr) + 1):
        bitwise_or_list.extend(map(calculate_bitwise_or, combinations(arr, i)))
    
    # count how many subsets yield the maximum bitwise OR
    count = bitwise_or_list.count(max(bitwise_or_list))
    return count




# test the function
count_max_bitwiseOR([3, 2, 1, 5])
