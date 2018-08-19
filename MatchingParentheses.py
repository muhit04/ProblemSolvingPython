# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# Example 1:
# Input: "()"
# Output: true
# Example 2:
# Input: "()[]{}"
# Output: true
# Example 3:
# Input: "(]"
# Output: false
# Example 4:
# Input: "([)]"
# Output: false
# Example 5:
# Input: "{[]}"
# Output: true
# Source: https://leetcode.com/problems/valid-parentheses/description/

class MatchingParen:
    def __init__(self, input_str: str):
        self.input_str = input_str
    
    def check_match(self):
        match = dict(zip('({[', ')}]'))
        queue = []
        for i in self.input_str:
            if i in match:
                queue.append(match[i])
            elif (queue and i != queue.pop()):
                return False
                
        return not queue


if __name__ == "__main__":
    m = MatchingParen('([])')
    print(m.check_match())
    