from collections import deque

class Solution:
    def checkValidString(self, s: str) -> bool:
        openParStack = deque()
        starStack = deque()

        for ind in range(len(s)):
            if s[ind] == '(':
                openParStack.append(ind)
            elif s[ind] == '*':
                starStack.append(ind)
            elif s[ind] == ')':
                if openParStack:
                    openParStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
        while openParStack:
            if not starStack:
                return False
            indOpenPar = openParStack.pop()
            if indOpenPar > starStack[-1]:
                return False
            starStack.pop()
        return True