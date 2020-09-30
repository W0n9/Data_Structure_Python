from typing import Union


class Stack(object):
    def __init__(self, limit: int = 10) -> None:
        self.stack = []
        self.limit = limit

    def push(self, data: Union[int, str]) -> None:
        if len(self.stack) >= self.limit:
            raise IndexError()
        self.stack.append(data)

    def pop(self) -> Union[int, str]:
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError()

    def peek(self) -> Union[int, str]:
        if self.stack:
            return self.stack[-1]

    def is_empty(self) -> bool:
        return not bool(self.stack)

    def size(self) -> int:
        return len(self.stack)


def balanced_parentheses(parentheses):
    stack = Stack(len(parentheses))
    for parenthesis in parentheses:
        if parenthesis == '(':
            stack.push(parenthesis)
        elif parenthesis == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()


if __name__ == "__main__":
    examples = ['((()))', '((())', '(()))']
    print('Balanced parentheses demonstration:\n')
    for example in examples:
        print(example + ': ' + str(balanced_parentheses(example)))