import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Cost from start node to current node
        self.h = h  # Heuristic cost from current node to goal node
        self.f = self.g + self.h  # Estimated total cost

    def __lt__(self, other):
        return self.f < other.f

def read_graph():
    graph = {}
    while True:
        edge = input("Enter edge and weight (e.g., 'S-A-1'), or type 'done' to finish: ").strip()
        if edge.lower() == 'done':
            break
        start, end, weight = edge.split('-')
        if start not in graph:
            graph[start] = []
        graph[start].append((end, int(weight)))
    return graph

def read_heuristics():
    heuristics = {}
    while True:
        heuristic = input("Enter heuristic value for node (e.g., 'S=5'), or type 'done' to finish: ").strip()
        if heuristic.lower() == 'done':
            break
        node, h_value = heuristic.split('=')
        heuristics[node] = int(h_value)
    return heuristics

def successors(state, graph):
    return graph.get(state, [])

def heuristic(state, heuristics):
    return heuristics.get(state, float('inf'))

def goal_test(state):
    return state == 'G'

def astar_search(initial_state, graph, heuristics):
    open_list = []
    closed_set = set()

    initial_node = Node(initial_state, g=0, h=heuristic(initial_state, heuristics))
    heapq.heappush(open_list, initial_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if goal_test(current_node.state):
            return current_node

        closed_set.add(current_node.state)

        for successor_state, step_cost in successors(current_node.state, graph):
            if successor_state in closed_set:
                continue

            g = current_node.g + step_cost
            h = heuristic(successor_state, heuristics)
            f = g + h

            successor_node = Node(successor_state, parent=current_node, g=g, h=h)

            for node in open_list:
                if node.state == successor_state and f >= node.f:
                    break
            else:
                heapq.heappush(open_list, successor_node)

    return None

print("Enter the graph edges and weights:")
graph = read_graph()
print("Enter the heuristic values for nodes:")
heuristics = read_heuristics()

initial_state = input("Enter the initial state: ").strip()
result_node = astar_search(initial_state, graph, heuristics)
if result_node:
    path = []
    while result_node:
        path.append(result_node.state)
        result_node = result_node.parent
    print("Path found:", path[::-1])
else:
    print("No path found.")
