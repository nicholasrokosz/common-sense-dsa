from collections import deque

def str_reverse(str):
    stack = deque()
    result_str = ""

    for char in str:
        stack.append(char)

    while len(stack) > 0:
        result_str += stack.pop()

    return result_str




print(str_reverse("abcde"))
