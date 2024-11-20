"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable, Union

""" 
Implementation of a prelude of elementary functions.

Mathematical functions:
- mul
- id
- add
- neg
- lt
- eq
- max
- is_close
- sigmoid
- relu
- log
- exp
- log_back
- inv
- inv_back
- relu_back

For sigmoid calculate as:
$f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
For is_close:
$f(x) = |x - y| < 1e-2$
"""
Number = Union[int, float]


def mul(a: Number, b: Number) -> Number:
    return a * b


def id(x: object) -> object:
    return x


def add(a: Number, b: Number) -> Number:
    return a + b


def neg(x: Number) -> Number:
    return -x


def lt(a: Number, b: Number) -> bool:
    return a < b


def eq(a: Number, b: Number) -> bool:
    return a == b


def max(a: Number, b: Number) -> Number:
    if a > b:
        return a
    return b


def is_close(a: Number, b: Number, epsilon: float = 1e-2) -> bool:
    return abs(a - b) <= epsilon


def sigmoid(x: Number) -> Number:
    return 1.0 / (1.0 + math.exp(-x))


def relu(x: Number) -> Number:
    return 0.0 if x <= 0 else x


def log(x: Number) -> Number:
    if x <= 0:
        raise ValueError("No log vals for 0 or negatives")
    return math.log(x)


def exp(power: int) -> Number:
    return math.e**power


def inv(x: Number) -> Number:
    if x == 0:
        raise ValueError
    return 1 / x


def log_back(x: Number, b: Number) -> Number:
    if x <= 0:
        raise ValueError
    return 1 / x * b


def inv_back(x: Number, b: Number) -> Number:

    return -(x ** (-2)) * b


def relu_back(x: Number, b: Number) -> Number:
    if x > 0:
        return b
    else:
        return 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists




def map(fn: Callable, a: list[object]) -> list[object]:
    return [fn(item) for item in a]


def zipWith():
    pass


def reduce(fn: Callable, a: list[Number]) -> Number:
    result = a[0]
    for item in a[1:]:
        result = fn(result, item)
    return result


def negList(a: list[Number]) -> list[Number]:
    return [-item for item in a]


def addLists(a: list[Number], b: list[Number]) -> list[Number]:
    """Element-wise addition of two given lists

    Args:
        a (list[Number]): _description_
        b (list[Number]): _description_

    Returns:
        list[Number]: _description_
    """
    c = [a[i] + b[i] for i in range(len(a))]
    # another way:
    # c = [x + y for x, y in zip(a, b)]
    return c


def sum(a: list[Number]) -> Number:
    if a:
        return reduce(lambda x, y: x + y, a)
    return 0


def prod(a: list[Number]) -> Number:
    if a:
        return reduce(lambda x, y: x * y, a)
    return 0
