"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
def pivot_index(nums):
    # Your code here
    """
    Input: list of integers
    Output: an int, the pivot index (note that we don't count the value ar the pivot)

    Plan 1: loop through each number, then get the sum of all the numbers to this number's left side
    get the sum of all the numbers to this number's right side.
    If the two sums match, return the index of the current number

    this plans work, but we perform a lot of redundant summing
    because of the fact that we're touching every other number excepts the
    current number, for every single number in the list, this an O(n^2) solution

    Plan 2: keep track of the total sum of the list
            keep track of the current sum as we iterate
            iterate trough our numbers
            substract the current number from the total
                if it does, return the index of the current number
                else, add the current number to the running sum
            if we reach the end of the loop, then no number satisfies what wer are looking for, so return -1
    
    for this plan, when iterating, we only take the current number and add/substract it from a variable we're keeping track of
    so when iterating, we only look at the current number, and none of the other numbers in the list.
    """
    total = sum(nums) # O(n)
    running = 0

    for i, num in enumerate(nums): # O(n)
        #substract num from total
        total -= num

        #check if total = running
        if total == running:
            #return the index of num
            return i
        
        running += num

    return -1

nums = [1,2,3]

print(pivot_index(nums))