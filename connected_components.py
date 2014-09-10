""" set of fucntions for graphs operations """ 
import random

def bfs_visited(ugraph, start_node):
    """ input: ugraph - undirected graph
    start node = node for start
    return set of visited nodes """

    visited = []
    queue_visited = []
    visited.append(start_node)
    queue_visited.append(start_node)    
    while len(queue_visited) >= 1:
        node = queue_visited.pop(0)
        neighbours_node = ugraph[node]
        for neighb in neighbours_node:
             if neighb not in visited:
                visited.append(neighb)
                queue_visited.append(neighb)
    return set(visited)

def cc_visited(ugraph):
    """ cc_visited function computes set of connected components 
    input: ugraph - undirected graph
    output: set of connected components """
    remaining_nodes = ugraph.keys()
    connected_components = []
    while len(remaining_nodes) >= 1:
        node = random.choice(remaining_nodes)
        visited = bfs_visited(ugraph, node)
        connected_components.append(visited)
        for visited_node in visited:
            if visited_node in remaining_nodes:
                remaining_nodes.remove(visited_node)
    return connected_components

def largest_cc_size(ugraph):
    """ compute cc visted and select largest component """
    connected_components = cc_visited(ugraph)
    max_comp_size = 0
    for comp in connected_components:
        if len(comp) > max_comp_size:
            max_comp_size = len(comp)           
    return  max_comp_size


def compute_resilience(ugraph, attack_order):
    """ compute resilience count size of largest component
    after every removing of nodes from attack_order lsit """
    largest_connected_components = []
    largest_connected_components.append(largest_cc_size(ugraph))
    for node in attack_order:
        # removing node
        ugraph.pop(node, None)
        # removing edges
        for other_node in ugraph.keys():
            edge = ugraph[other_node]
            if node in edge:                
                edge.remove(node)
                ugraph[other_node] = edge
        largest_connected_components.append(largest_cc_size(ugraph))      
    return largest_connected_components

