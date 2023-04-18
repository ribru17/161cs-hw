# returns a tuple displaying the order in which the tree is traversed using BFS
# `TREE`: root of a tree, tuple or primitive type. function returns tuple
def BFS(TREE):
    # base case where root is not a tuple
    if type(TREE) is not tuple:
        return (TREE,)

    checked = []
    q = []

    # initialize q and return value
    for i in TREE:
        if type(i) is not tuple:
            checked.append(i)
        else:
            q.append(i)

    # traverse all nodes, populating the queue and return value list as needed
    while len(q) > 0:
        i = q.pop(0)
        # leaf node found! add to checked
        if type(i) is not tuple:
            checked.append(i)
        # not a leaf node! add all child nodes to the queue
        else:
            for el in i:
                q.append(el)

    # return finally, converting the list to our needed `tuple` data type
    return tuple(checked)


# returns a tuple displaying the order in which the tree is traversed using DFS
# `TREE`: root of a tree, tuple or primitive type. function returns tuple
def DFS(TREE):
    # base case where root is not a tuple
    if type(TREE) is not tuple:
        return (TREE,)

    checked = []

    for i in TREE:
        # spread results to prevent function returning tuple of a tuple of a...
        checked += [*DFS(i)]

    # return finally, converting the list to our needed `tuple` data type
    return tuple(checked)


# performs depth-first iterative-deepening search on a tree with max depth D
# `TREE` is a tree represented by a tuple or a primitive data type, `D` is
# an int representing the max depth. function returns a tuple representing the
# order that the nodes were traversed
def DFID(TREE, D):
    checked = []
    # check tree incrementally increasing depth each time
    for limit in range(D+1):
        DLFS(TREE, limit, checked)

    return tuple(checked)


# helper function for DFID to perform a right->left DFS, limited by a depth D
# `TREE` is a tree represented by a tuple or a primitive data type, `D` is an
# int representing the max depth. path is a list to be updated as the nodes are
# checked. function has no return value
def DLFS(TREE, D, PATH):
    if D < 0:
        return

    # `TREE` is leaf node, append to list of items checked
    if type(TREE) is not tuple:
        PATH.append(TREE)
        return

    # `TREE` is not a leaf node, perform DFS on children (right to left)
    for node in reversed(TREE):
        DLFS(node, D-1, PATH)


# These functions implement a depth-first solver for the homer-baby-dog-poison
# problem. In this implementation, a state is represented by a single tuple
# (homer, baby, dog, poison), where each variable is True if the respective
# entity is on the west side of the river, and False if it is on the east side.
# Thus, the initial state for this problem is (False False False False)
# (everybody is on the east side) and the goal state is (True True True True).
# The main entry point for this solver is the function DFS_SOL, which is called
# with (a) the state to search from and (b) the path to this state. It returns
# the complete path from the initial state to the goal state: this path is a
# list of intermediate problem states. The first element of the path is the
# initial state and the last element is the goal state. Each intermediate state
# is the state that results from applying the appropriate operator to the
# preceding state. If there is no solution, DFS_SOL returns [].
# To call DFS_SOL to solve the original problem, one would call
# DFS_SOL((False, False, False, False), [])
# However, it should be possible to call DFS_SOL with any intermediate state
# (S) and the path from the initial state to S (PATH).
# First, we define the helper functions of DFS_SOL.
# FINAL_STATE takes a single argument S, the current state, and returns True if
# it is the goal state (True, True, True, True) and False otherwise.
def FINAL_STATE(S):
    return S == (True, True, True, True)


# NEXT_STATE returns the state that results from applying an operator to the
# current state. It takes two arguments: the current state (S) and which entity
# to move (A, equal to "h" for homer only, "b" for homer with baby, "d" for
# homer with dog, and "p" for homer with poison).
# It returns a list containing the state that results from that move.
# If applying this operator results in an invalid state (because the dog and
# baby, or poison and baby are left unsupervised on one side of the river), or
# when the action is impossible (homer is not on the same side as the entity)
# it returns []. NOTE that NEXT_STATE returns a list containing the successor
# state (which is itself a tuple)# the return should look something like
# [(False, False, True, True)].
def NEXT_STATE(S, A):
    next_state = list(S)

    # homer must move no matter what
    next_state[0] = not next_state[0]

    # perform the action
    # return early in case homer is not on the same side as the 'movee'
    match A:
        case 'b':
            next_state[1] = not next_state[1]
            if next_state[1] is not next_state[0]:
                return []
        case 'd':
            next_state[2] = not next_state[2]
            if next_state[2] is not next_state[0]:
                return []
        case 'p':
            next_state[3] = not next_state[3]
            if next_state[3] is not next_state[0]:
                return []

    # return invalid if the baby is with either the dog or the poison,
    # and homer is not with them
    if next_state[0] is not next_state[1] and\
            (next_state[1] is next_state[2] or next_state[1] is next_state[3]):
        return []

    # all checks passed! next state is valid.
    return [tuple(next_state)]


# SUCC_FN returns all of the possible legal successor states to the current
# state. It takes a single argument (S), which encodes the current state, and
# returns a list of each state that can be reached by applying legal operators
# to the current state.
def SUCC_FN(S):
    # compute all possible next states and concatenate them into one list
    # (invalid states are empty lists so we don't have to check for that here)
    possible_states = []
    possible_states += NEXT_STATE(S, 'h')
    possible_states += NEXT_STATE(S, 'b')
    possible_states += NEXT_STATE(S, 'd')
    possible_states += NEXT_STATE(S, 'p')
    return possible_states


# ON_PATH checks whether the current state is on the stack of states visited by
# this depth-first search. It takes two arguments: the current state (S) and
# the stack of states visited by DFS (STATES). It returns True if S is a member
# of STATES and False otherwise.
def ON_PATH(S, STATES):
    return S in STATES


# MULT_DFS is a helper function for DFS_SOL. It takes two arguments: a list of
# states from the initial state to the current state (PATH), and the legal
# successor states to the last, current state in the PATH (STATES). PATH is a
# first-in first-out list of states# that is, the first element is the initial
# state for the current search and the last element is the most recent state
# explored. MULT_DFS does a depth-first search on each element of STATES in
# turn. If any of those searches reaches the final state, MULT_DFS returns the
# complete path from the initial state to the goal state. Otherwise, it returns
# [].
def MULT_DFS(STATES, PATH):
    # return early if any of the given successor states are the final state
    for state in STATES:
        if FINAL_STATE(state):
            return PATH + [(True, True, True, True)]

    # recursively check all successor states to see if they are the final state
    for state in STATES:
        # makes sure we don't check states we've already checked
        if ON_PATH(state, PATH):
            continue

        found_path = MULT_DFS(SUCC_FN(state), PATH + [state])

        # solution found!
        if found_path is not []:
            return found_path

    # no solutions found :(
    return []


# DFS_SOL does a depth first search from a given state to the goal state. It
# takes two arguments: a state (S) and the path from the initial state to S
# (PATH). If S is the initial state in our search, PATH is set to []. DFS_SOL
# performs a depth-first search starting at the given state. It returns the
# path from the initial state to the goal state, if any, or [] otherwise.
# DFS_SOL is responsible for checking if S is already the goal state, as well
# as for ensuring that the depth-first search does not revisit a node already
# on the search path (i.e., S is not on PATH).
def DFS_SOL(S, PATH):
    # return early if already at final state
    if FINAL_STATE(S):
        return PATH + [S]
    # initiate search
    return MULT_DFS(SUCC_FN(S), PATH + [S])
