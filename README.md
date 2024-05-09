# leetcode_solutions
Here i post the solutions of divers leetcode problems

## 1. longest common prefix:
commonPrefix: This method takes two words as input and returns their common prefix. It iterates through each character in the words and appends characters to prefix until a mismatch is encountered.
longestCommonPrefix: This method takes a list of strings as input and returns the longest common prefix among them. It initializes prefix with the first string in the list and iterates through each word in the list twice. For each pair of words, it finds their common prefix using the commonPrefix method and updates prefix if a shorter common prefix is found. Finally, it returns prefix.
