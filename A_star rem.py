Graph_nodes = {}
Graph_nodes = eval(input("Enter your graph : "))
print("\nThe Graph you entered is : ")
for key, value in Graph_nodes.items():
    print(key, ":", value)

startnode = input("\nEnter the start node : ")
stopnode = input("Enter the stop node : ")

def aStarAlgo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node
    H_dist = eval(input("\nEnter the key-value corresponding to parent and its heuristics : "))
    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n == None or g[v] + H_dist[v] < g[n] + H_dist[n]:
                n = v
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == None:
            print('Path does not exist!')
            return None
        
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('\nPath found : {}'.format(path))
            return None
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

aStarAlgo(startnode, stopnode)
