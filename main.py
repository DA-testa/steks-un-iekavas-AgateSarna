# python3
# Agate Šarna 221RDB224
from collections import namedtuple
Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    br_dict = {'(':'}','[':']','{':'}'}
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i+1
            rem = opening_brackets_stack.pop()
            if not are_matching(rem.char, next):
                return i+1
    if len(opening_brackets_stack) == 0:
        return "Sucess"
    else:
        return [opening_brackets_stack[0].position + 1]


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()
