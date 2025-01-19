#Time and space complexity : O(n)
# Stack pop and push operations are O(1).

class Solution:
    def isValid(self, s: str)-> bool:

        closetoopen = {')':'(', '}':'{', ']':'['}
        stack = []

        for c in s:
            if c in closetoopen:
                if stack and stack[-1] == closetoopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        
s = "(){}[]"
myobject = Solution()
output = myobject.isValid(s)

print(output)


