'''
Problem Name: Google Foobar - Fuel Injection Perfection
Author: Ayushi Rawat
'''
map = {}
stack = []
def solution(n):
    n = int(n)
    stack.append(n)
    while len(stack) > 0:
        n = stack[-1]
        if map.get(n):
            stack.pop()
        elif n == 1:
            map[n] = 0
            stack.pop()
        elif n % 2 == 0:
            if map.get(n / 2) is not None:
                map[n] = 1 + map[n / 2]
                stack.pop()
            else:
                stack.append(n / 2)
        else:
            if map.get(n + 1) is not None and map.get(n - 1) is not None:
                map[n] = 1 + min(map[n + 1], map[n - 1])
                stack.pop()
            else:
                stack.append(n - 1)
                stack.append(n + 1)
    return map[n]

