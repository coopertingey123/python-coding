# Given an array of integers nums and an integer target, return the indices of the two numbers 
# such that they add up to the target. Assume that each input would have exactly one solution.

nums = [1, 2, 3, 34, 5, 8]

def add_nums(num1, num2):
    return print(num1 + num2)

def check_palindrome(word):
    if (word == word[::-1]):
        return print(True)
    else:
        return print(False)

def fizz_buzz():
    for num in range(0, 100):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

def find_max_element(arr1):
    return print(max(arr1))

def factorial_of_a_num(num):
    total = 1
    for i in range(1, num + 1):
        total = total * i

    return print(total)

def reverse_a_string(word):
    return print(word[::-1])

def check_array(arr1):
    if (arr1 == sorted(arr1)):
        return print(True)
    else:
        return print(False)
    
def find_idx(arr, target):
    target_found = -1

    for idx, val in enumerate(arr):
        if val == target:
            target_found = idx

    return print(target_found)

def combine_arrays(arr1, arr2):
    combined_arr = arr1 + arr2
    return print(sorted(combined_arr))

def count_chars_in_string(word, char):
    char_count = {}

    for i in word:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    return print(char_count[char])

def reverse_linked_list(arr1):
    return print(arr1[::-1])


def find_missing_num(arr1):
    missing_nums = []
    maxNum = max(arr1)
    minNum = min(arr1)

    for num in range(minNum, maxNum - 1):
        if num not in arr1:
            missing_nums.append(num)    

    return print(missing_nums)

def two_sum_problem(arr1, target):
    sums = {}
    for idx, val in enumerate(arr1):
        matching_val = target - val

        if matching_val in sums:
            return print([sums[matching_val], idx])
        
        sums[val] = idx


    return print(sums)
        

def find_longest_substring(word):

    word_bank = []

    current_str = word[0]


    for idx in range(1, len(word)):
        if word[idx] != word[idx - 1]:
            current_str += word[idx]
        else:
            word_bank.append(current_str)
            current_str = word[idx]

    word_bank.append(current_str)

    max_len = max(word_bank, key=len)

    return print(len(max_len))


def valid_parens(str1):
    stack = []
    # Hash map to keep track of matching pairs
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    
    for char in str1:
        if char in matching_parentheses.values():
            # If it's an opening parenthesis, push it onto the stack
            stack.append(char)
        elif char in matching_parentheses.keys():
            # If it's a closing parenthesis, check if it matches the top of the stack
            if not stack or stack.pop() != matching_parentheses[char]:
                return False
        else:
            # If the character is not a parenthesis, ignore it
            continue
    
    # If stack is empty, all parentheses were matched
    return len(stack) == 0

def first_non_repeating_character(s):
    from collections import Counter
    
    # Count the frequency of each character
    count = Counter(s)
    
    # Find the first character with a frequency of 1
    for index, char in enumerate(s):
        if count[char] == 1:
            return index
    
    return -1  # Return -1 if no non-repeating character is found

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    def check_balance(node):
        if not node:
            return 0, True
        
        left_height, left_balanced = check_balance(node.left)
        right_height, right_balanced = check_balance(node.right)
        
        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        height = max(left_height, right_height) + 1
        
        return height, balanced
    
    _, balanced = check_balance(root)
    return balanced

def max_subarray_sum(nums):
    if not nums:
        return 0
    
    max_so_far = max_ending_here = nums[0]
    
    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

find_longest_substring('hellllo')
