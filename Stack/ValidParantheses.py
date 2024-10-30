class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return False

        length = len(s)

        stack = []

        for i in s:
            if i in "([{":
                stack.append(i)

            elif i in ")}]":
                # Closing bracket at the start without opening bracket, as stack is empty
                if not stack:
                    return False

                top = stack.pop()

                # Check if the popped bracket matches the current closing bracket
                if (i == ")" and top != "(") or \
                   (i == "]" and top != "[") or \
                   (i == "}" and top != "{"):
                    return False  # Mismatched brackets
            
        # After processing all characters, check if any opening brackets are left
        return len(stack) == 0  # True if all brackets matched
