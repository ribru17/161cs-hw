# NOTE: The solutions for 1. and 2. are inspired by the existing
# mathematical observations of the Fibonacci sequence.

# compute the Nth padovan number
# `N` is an integer, function returns an integer
def PAD(N):
    # compute p, equivalent of the golden ratio but for padovan sequence
    # this value is derived from the cubic formula:
    # it is the real solution of x^3 - x - 1 = 0
    p = (1/2 + (1/4 - 1/27) ** (1/2)) ** (1/3) + \
        (1/2 - (1/4 - 1/27) ** (1/2)) ** (1/3)
    # compute coefficient for p^N based on formula
    # for solving recurrence relations
    c = p ** 5 / (2 * p + 3)
    # solution is the integer closest to this value. Thus we have
    # found a solution quicker than the recursive way using mathematics
    return round(c * p ** N)


# compute amount of sums required to calculate first N terms
# `N` is an integer, function returns an integer
def SUMS(N):
    # first few values are below:
    # 0 0 0 1 1 2 3 4 6

    # we see that these follow the pattern S(n) = S(n-2) + S(n-3) + 1
    # where S(0) = S(1) = S(2) = 0. this is because P(n) = P(n-2) + P(n-3)
    # meaning that calculating P(n) requires the amount of additions in P(n-2)
    # PLUS the additions required to calculate P(n-3) plus 1 (we add one since
    # we need to do an additional addition to combine the result)

    # using this information we can develop a function to find the amount of
    # sums required to calculate the Nth value, this time using recursion

    # keep track of values up to S(n-3)
    previous = [0, 0, 0]
    # keep track of S(n)
    current = 0

    # calculate recurrence relation
    while N >= 3:
        N -= 1
        previous[0] = previous[1]
        previous[1] = previous[2]
        previous[2] = current
        current = previous[0] + previous[1] + 1

    return current


# anonymize each leaf node in a given tree
# `TREE` is the root of a tree to be anonymized,
# function returns anonymized tree
def ANON(TREE):
    if type(TREE) is not tuple:
        return '?'
    else:
        return_value = []
        for i in TREE:
            # tuples are immutable so we must assemble the values in a list
            # and then convert that list to a tuple before returning it
            return_value.append(ANON(i))
        return tuple(return_value)


# returns the height of a given tree
# `TREE` is the root of a tree, function returns an integer
def TREE_HEIGHT(TREE):
    if type(TREE) is not tuple:
        return 0
    else:
        checked = []
        for i in TREE:
            checked.append(1 + TREE_HEIGHT(i))

        # return the deepest subtree that was found
        return max(checked)


# return the tuple formed from a postorder traversal of a given ordered tree
# `TREE` is the root of an ordered tree, function returns a tree
def TREE_ORDER(TREE):
    if type(TREE) is not tuple:
        return tuple([TREE])
    else:
        return_value = []

        left = TREE_ORDER(TREE[0])
        right = TREE_ORDER(TREE[2])
        center = TREE_ORDER(TREE[1])

        # must assemble items in this way so that the return value
        # is a tuple that does not contain nested tuples

        # add left items to tuple
        if type(left) is tuple:
            return_value += list(left)
        else:
            return_value.append(left)

        # add right items to tuple
        if type(right) is tuple:
            return_value += list(right)
        else:
            return_value.append(right)

        # add right items to tuple
        if type(center) is tuple:
            return_value += list(center)
        else:
            return_value.append(center)

        # return finished postorder tuple
        return tuple(return_value)
