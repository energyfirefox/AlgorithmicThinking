# defining constants
# graphs representation

EX_GRAPH0 = {0:set([1, 2]), 
             1:set([]), 
             2:set([])}

EX_GRAPH1 = {0:set([1, 4, 5]), 
             1:set([2, 6]), 
             2:set([3]), 
             3:set([0]), 
             4:set([1]), 
             5:set([2]), 
             6:set([])}

EX_GRAPH2 = {0:set([1, 4, 5]),
             1:set([2, 6]),
             2:set([3, 7]),
             3:set([7]),
             4:set([1]),
             5:set([2]),
             6:set([]),
             7:set([3]),
             8:set([1, 2]),
             9:set([0, 3, 4, 5, 6, 7])}


def make_complete_graph(num_nodes):
    # make_complete_graph
    # this function return complete graph with n*(n-1)/2 nodes
    # for every node we should produce edges to the rest of nodes
    graph_adj = {}
    for node1 in range(num_nodes):
        edges = []
        for node2 in range(num_nodes):
            if (node1 != node2):
                edges.append(node2)
        graph_adj[node1] = set(edges)
    return graph_adj


def compute_in_degrees(digraph):
    # compute_in_degrees
    # this function count in-degree values for every node
    # for every node we should count number of 
    in_degree = {}
    for node1 in digraph.keys():
        in_degree_counter = 0
        for node2 in digraph.keys():
           if node1 in digraph[node2]:
            in_degree_counter += 1
        in_degree[node1] = in_degree_counter
    return in_degree


def in_degree_distribution(digraph):
    # in_degree_distribution
    # this function found in-degree distribution based on in-degree values
    # for degree distrubition we just aggregarte results from previous function
    in_degrees = compute_in_degrees(digraph)
    in_degrees_distribution = {}
    for node in in_degrees.values():
        if node not in in_degrees_distribution.keys():
            in_degrees_distribution[node] = 1
        else:
            in_degrees_distribution[node] += 1
            
    return in_degrees_distribution
