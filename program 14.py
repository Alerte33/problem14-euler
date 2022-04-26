from typing import Dict

from lib.numbertheory import is_even
def collatz(n: int, d: Dict[int, int]) -> int:
    """ Compute the Collatz sequence starting at :math:`n`

    The length of a Collatz sequence starting at :math:`n` can be computed by iterating the Collatz map until it reaches
    :math:`1`. While this would be sensible for a single :math:`n`, performing this for many values of :math:`n` will
    result in a lot of redundant calculations.

    Consider the following two overlapping Collatz sequence:

    .. math::

        64 \\rightarrow 32 \\rightarrow 16 \\rightarrow 8 \\rightarrow 4 \\rightarrow 2 \\rightarrow 1 \\\\
        10 \\rightarrow 5 \\rightarrow 16 \\rightarrow 8 \\rightarrow 4 \\rightarrow 2 \\rightarrow 1

    Observe the coalescence of these two sequences when they both reach the value :math:`16`. These two sequences
    provide the lengths of Collatz sequences starting at: :math:`1,2,4,5,8,10,16,32` and :math:`64`.

    By caching all results as i go i can avoid re-computing the tail of any coalescing sequences.

    :param n: the start of the Collatz sequence
    :param d: a dictionary of existing solutions
    :return: the length of the Collatz sequence starting at :math:`n`

    .. note:: the dictionary :math:`d` will be updated with any partial results computed.
    """

    try:
        return d[n]
    except KeyError:
        if is_even(n):
            d[n] = 1 + collatz(n // 2, d)
        else:
            d[n] = 1 + collatz(3 * n + 1, d)
        return d[n]


def solve():
    """ Compute the answer to Project Euler's problem #14 """

    upper_bound = 1000000 # search limit

    # Apply the recursive to find the maximal length chain
    d = {1: 1}
    for i in range(1, upper_bound, 1):
        collatz(i, d)

    # Identify the largest chain
    v = list(d.values())
    k = list(d.keys())
    answer = k[v.index(max(v))]

    return answer


expected_answer = 837799
