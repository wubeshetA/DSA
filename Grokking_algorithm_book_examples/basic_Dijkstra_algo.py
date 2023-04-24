# This file include implementation of Dijkstra algorithm with a simple implementation

# graph includes neighbor vertex and their cost to reach them.
graph = {"start": {"A": 6,
                   "B": 2},
         "A": {"finish": 1},
         "B": {"finish": 5,
               "A": 3
               },
         "finish": {}
         }

# represent parent in dict
parent = {"start": None,
          "A": None,
          "B": None,
          "finish": None}
costs = {
    "A": 6,
    "B": 2,
    "finish": float("inf")
    
}
processed = []

def find_lowest_cost_node(costs):
    # return the lowest cost node
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    # visit neighbors of node7
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = neighbors[n] + cost
        if costs[n] > new_cost:
            costs[n] = new_cost
            parent[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

if __name__ == '__main__':
    print(costs)          
           
     