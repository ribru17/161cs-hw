##############
# Homework 4 #
##############

# Exercise: Fill this function.
# Returns the index of the variable that corresponds to the fact that
# "Node n gets Color c" when there are k possible colors
def node2var(n, c, k):
    return (n-1)*k+c


# Exercise: Fill this function
# Returns *a clause* for the constraint:
# "Node n gets at least one color from the set {1, 2, ..., k}"
def at_least_one_color(n, k):
    # generate a simple OR between each color so we have a sentence that is
    # true when at least one color is selected
    return [node2var(n, c, k) for c in range(1, k+1)]


# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Node n gets at most one color from the set {1, 2, ..., k}"
def at_most_one_color(n, k):
    clauses = []

    # generate a NAND for all possible pairings then AND them together in order
    # to get a sentence that requires a node to get at MOST *one* color
    for i in range(1, k+1):
        for j in range(i+1, k+1):
            clauses.append([-node2var(n, i, k), -node2var(n, j, k)])

    return clauses


# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Node n gets exactly one color from the set {1, 2, ..., k}"
def generate_node_clauses(n, k):
    # node gets exactly one color if it gets at MOST AND at LEAST *one*
    return at_most_one_color(n, k) + [at_least_one_color(n, k)]


# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Nodes connected by an edge e (represented by a list)
# cannot have the same color"
def generate_edge_clauses(e, k):
    u, v = e
    clauses = []

    # generates a NAND for each possible color between the edge: both cannot be
    # 1 MEANING both cannot have the same color
    for i in range(1, k+1):
        clauses.append([-node2var(u, i, k), -node2var(v, i, k)])

    return clauses


# The function below converts a graph coloring problem to SAT
# Return CNF as a list of clauses
# DO NOT MODIFY
def graph_coloring_to_sat(graph_fl, sat_fl, k):
    clauses = []
    with open(graph_fl) as graph_fp:
        node_count, edge_count = tuple(map(int, graph_fp.readline().split()))
        for n in range(1, node_count + 1):
            clauses += generate_node_clauses(n, k)
        for _ in range(edge_count):
            e = tuple(map(int, graph_fp.readline().split()))
            clauses += generate_edge_clauses(e, k)
    var_count = node_count * k
    clause_count = len(clauses)
    with open(sat_fl, 'w') as sat_fp:
        sat_fp.write("p cnf %d %d\n" % (var_count, clause_count))
        for clause in clauses:
            sat_fp.write(" ".join(map(str, clause)) + " 0\n")
    return clauses, var_count


# Example function call
if __name__ == "__main__":
    graph_coloring_to_sat("graph2.txt", "graph2.cnf", 8)
