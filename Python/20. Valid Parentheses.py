class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = "([{"
        close = ")]}"

        if s[0] in close:
            return False

        for i in s:
            try:
                if stack[0] in close:
                    return False
            except IndexError:
                if i in close:
                    return False
            if i in open:
                stack.append(i)
            else:
                open_index = close.index(i)
                open_value = open[open_index]
                if stack[-1] != open_value:
                    return False
                else:
                    del stack[-1]
        return False if len(stack) > 0 else True