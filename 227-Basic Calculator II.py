# 2024-09-20
class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        i = 0
        priority = False
        s = s.replace(" ", "")

        while i < len(s):

            if s[i].isdigit():
                j = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                stack.append(s[j:i])
                if priority == True:
                    num1 = int(stack.pop())
                    op = stack.pop()
                    num2 = int(stack.pop())
                    if op == "*":
                        stack.append(str(num1 * num2))
                    elif op == "/":
                        stack.append(str(num2 // num1))

                    priority = False

            else:
                if s[i] == "*" or s[i] == "/":
                    priority = True
                stack.append(s[i])
                i += 1

        print(stack)
        res = 0
        cur_op = "+"
        for s in stack:
            if s.isdigit() and cur_op == "+":
                res += int(s)
            elif s.isdigit() and cur_op == "-":
                res -= int(s)
            elif not s.isdigit():
                cur_op = s

        return res