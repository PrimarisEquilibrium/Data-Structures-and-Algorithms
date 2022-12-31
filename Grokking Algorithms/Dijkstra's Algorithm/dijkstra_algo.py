# --------------------------- Graph Initialization --------------------------- #

# Store names
graph = {}
graph["you"] = ["alice", "bob", "claire"]

# Store Neighbors & Weights

graph["start"] = {"a": 6, "b": 2}
graph["a"] = {"fin": 1}
graph["b"] = {"a": 3, "fin": 5}
graph["fin"] = {}

# Store Costs (Edge Value) & Parent Nodes

inf = float("inf")
costs = {"a": 6, "b": 2, "fin": inf}
parents = {"a": "start", "b": "start", "fin": inf}

processed = []  # To avoid checking a node more than once

# ------------------------- Find Lowest Cost Function ------------------------ #

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")  # Lowest cost is introduced as infinity
    lowest_cost_node = None     # Lowest cost node is introduced as None
    for node in costs:          # Go through all the nodes in cost
        cost = costs[node]      
        # If it's the lowest cost so far and hasn't been in processed yet...
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost  # ... set it as the new lowest-cost node
            lowest_cost_node = node # The node key name
    return lowest_cost_node

# ------------------------- Algorithm Implimentation ------------------------- #

node = find_lowest_cost_node(costs) # Find the lowest-cost node that you haven't processed yet.
while node is not None:             # If you've processed all the nodes, this while loop is done.
    cost = costs[node]      # The cost of the current node
    neighbors = graph[node] # All the neighbors of the current node
    for n in neighbors.keys():      # Go through all the neighbors of this node.
        new_cost = cost + neighbors[n]  # Cost = Current Node Cost | Neighbors[n] = The price to the next node
        if costs[n] > new_cost:     # If it's cheaper to get to this neighbor by going through this node...
            costs[n] = new_cost     # ... update cost for this node.
            parents[n] = node       # This node becomes the new parent for this neighbor.
    processed.append(node)
    node = find_lowest_cost_node(costs)