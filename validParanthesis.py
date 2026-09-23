#20
class Solution:

    def isValid(self, s: str) -> bool:
        # If the string length is odd, brackets cannot possibly all be in matching pairs
        if len(s) % 2 != 0:
            return False

        # Map each closing bracket to its corresponding opening bracket
        matching = {")": "(", "}": "{", "]": "["}

        # Initialize an empty stack (using a Python list) to store opening brackets
        stack = []

        # Iterate through every character in the given string
        for char in s:
            # Check if the current character is a closing bracket (exists in keys of 'matching')
            if char in matching:
                # Remove and get the top bracket from the stack if not empty;
                # otherwise assign a dummy value '#' that will never match any bracket
                top_element = stack.pop() if stack else "#"

                # Check if the expected opening bracket matches the popped element
                if matching[char] != top_element:
                    return False
            else:
                # If it is an opening bracket ('(', '{', or '['), push it onto the stack
                stack.append(char)

        # Returns True if the stack is completely empty (all brackets were matched),
        # or False if leftover unclosed opening brackets remain
        return not stack
