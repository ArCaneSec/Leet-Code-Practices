class Solution:
    def isValid(self, string):
        stack = []
        open_form = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for s in string:
            if s in ")]}":
                if len(stack) == 0 :
                    return False

                if stack[-1] != open_form[s]:
                    return False
                stack.pop(-1)
                continue

            stack.append(s)

        return len(stack) == 0
            

print(Solution().isValid("]"))