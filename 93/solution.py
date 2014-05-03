#!/usr/bin/env python
#
# Project Euler 93


from itertools import product, permutations


def solution():
    best_solution = None
    best_score = 0
    for solution in generate_solutions():
        targets = generate_targets(*solution)
        score = longest_consecutive(targets)
        if score > best_score:
            best_solution = solution
            best_score = score
    return format_solution(best_solution)


def format_solution(a):
    return "".join(str(x) for x in a)


def generate_solutions():
    for a in xrange(0, 7):
        for b in xrange(a + 1, 8):
            for c in xrange(b + 1, 9):
                for d in xrange(c + 1, 10):
                    yield (a, b, c, d)


def longest_consecutive(s):
    numbers = sorted(list(s))
    longest_run, current_run = 0, 0
    in_run = False
    previous = numbers[0]
    for current in numbers[1:]:
        if in_run:
            if current == previous + 1:
                current_run += 1
                if current_run > longest_run:
                    longest_run = current_run
            else:
                in_run = False
                current_run = 0
        else:
            if current == previous + 1:
                in_run = True
        previous = current

    return longest_run


def generate_targets(a, b, c, d):
    targets = set()
    for (op1, op2, op3) in product(ops, ops, ops):
        for (u, x, y, z) in permutations([a, b, c, d]):
            targets.update(smoke_trees(op1, op2, op3, u, x, y, z))
    return targets


def smoke_trees(*args):
    result = set()
    for tree in trees:
        try:
            x = tree(*args)
            if x > 0 and x == int(x):
                result.add(x)
        except ZeroDivisionError:
            pass
    return result


def tree1(op1, op2, op3, u, x, y, z):
    return op3(op2(op1(u, x), y), z)

def tree2(op1, op2, op3, u, x, y, z):
    return op2(op1(u, x), op3(y, z))

def tree3(op1, op2, op3, u, x, y, z):
    return op3(op1(u, op2(x, y)), z)

def tree4(op1, op2, op3, u, x, y, z):
    return op1(u, op3(op2(x, y), z))

def tree5(op1, op2, op3, u, x, y, z):
    return op1(u, op2(x, op3(y, z)))

trees = [tree1, tree2, tree3, tree4, tree5]


def op_add(a, b):
    return a + b

def op_sub(a, b):
    return a - b

def op_mul(a, b):
    return a * b

def op_div(a, b):
    return a / float(b)

ops = [op_add, op_sub, op_mul, op_div]


if __name__ == "__main__":
    print solution()
