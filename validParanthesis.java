import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public boolean isValid(String s) {
        // Odd length strings can never have matching pairs
        if (s.length() % 2 != 0) {
            return false;
        }

        Deque<Character> stack = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            // Push expected closing bracket when opening bracket is encountered
            if (c == '(') {
                stack.push(')');
            } else if (c == '{') {
                stack.push('}');
            } else if (c == '[') {
                stack.push(']');
            } else {
                // If closing bracket doesn't match top of stack or stack is empty
                if (stack.isEmpty() || stack.pop() != c) {
                    return false;
                }
            }
        }

        // If stack is empty, all opening brackets were matched
        return stack.isEmpty();
    }
}
