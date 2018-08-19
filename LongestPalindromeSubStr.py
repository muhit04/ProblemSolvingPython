# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
# Input: "cbbd"
# Output: "bb"
# Source: https://leetcode.com/problems/longest-palindromic-substring/description/

class LongestPalindromeSubStr:
    def __init__(self, input_str: str):
        self.input_str = input_str

    def check_if_palindrome(self, palin_str: str):
        if palin_str == palin_str[::-1]:
            return True
        return False

    def form_largest_palindrome(self):
        str_container = ""
        valid_palin = ""
        length = len(self.input_str)
        for i in range(length):
            str_container = self.input_str[i]
            for j in range(i+1, length):
                str_container += self.input_str[j]
                if self.check_if_palindrome(str_container):
                    if len(valid_palin) < len(str_container):
                        valid_palin = str_container
        
        return valid_palin



if __name__ == "__main__" :
    l = LongestPalindromeSubStr('cbd')
    print(l.form_largest_palindrome())