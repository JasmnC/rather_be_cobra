## Coding Questions

#  Coding Problem 1: Two Sum
# Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
# You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

testcase1_1 = two_sum([2, 7, 11, 15], 9)
print(testcase1_1)  # -> [0, 1]
testcase1_2 = two_sum([3, 2, 4], 6)
print(testcase1_2)  # -> [1, 2]



# Coding Problem 2: Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# A substring is a contiguous sequence of characters within a string. You need to find the longest substring where all characters are unique (no character appears more than once).

def length_of_longest_substring(s: str) -> int:
    list_substrings = []
    cur_ans = ""
    for i in range(len(s)):
        if s[i] not in list_substrings:
            list_substrings.append(s[i])
            
        else:
            if len(cur_ans) < len(list_substrings):
                cur_ans = ''.join(list_substrings)
            list_substrings = []
    return cur_ans if len(cur_ans) > len(list_substrings) else ''.join(list_substrings)
    
testcase2_1 = length_of_longest_substring("abcabcbb")
print(testcase2_1) # "abc"
testcase2_2 = length_of_longest_substring("bbbbb")
print(testcase2_2)  # "b"
testcase2_3 = length_of_longest_substring("pwwkew")
print(testcase2_3)  # "wke"



# Coding Problem 3: Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# You must write an algorithm that runs in O(n) time and without using the division operation. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

def product_except_self(nums: list[int]) -> list[int]:
    prefix_products = [1] * len(nums)
    postfix_products = [1] * len(nums)  
    res=[]

    for i in range(1,len(nums)):
        prefix_products[i] = nums[i - 1] * prefix_products[i - 1]

    for j in range(len(nums) - 2, -1, -1):
        postfix_products[j] = nums[j + 1] * postfix_products[j + 1]
    
    for i in range(len(nums)):
        res.append(prefix_products[i] * postfix_products[i])
    return res  

testcase3_1 = product_except_self([1, 2, 3, 4])
print(testcase3_1) # [24, 12, 8, 6]

testcase3_2 = product_except_self([-1, 1, 0, -3, 3])
print(testcase3_2) # [0, 0, 9, 0, 0]



# Coding Problem 4: Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once. For example, "listen" and "silent" are anagrams.

def group_anagrams(strs: list[str]) -> list[list[str]]:
    mapping={}
    for s in strs:
        ang=''.join(sorted(s))
        if  ang in mapping.keys():
            mapping[ang].append(s)
        else:
            mapping[ang]=list([s])
    return list(mapping.values())

testcase4_1 = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(testcase4_1)  # [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
testcase4_2 = group_anagrams([""])
print(testcase4_2)  # [[""]]
testcase4_3 = group_anagrams(["a"])
print(testcase4_3)  # [["a"]]