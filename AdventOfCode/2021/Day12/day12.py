import sys
sys.path.append('./..')
import utils

sys.setrecursionlimit(int(1e9))

def process_input(data):
    graph = {}
    keys = set()
    for l in data:
        connection = l.split('-')
        lhs = connection[0]
        rhs = connection[1]
        keys.add(lhs)
        keys.add(rhs)
    for key in keys:
        graph[key] = set()
    for l in data:
        connection = l.split('-')
        lhs = connection[0]
        rhs = connection[1]
        keys.add(lhs)
        graph[lhs].add(rhs)
        graph[rhs].add(lhs)

    return graph

class Graph: 
    def __init__(self, V) -> None:
        self.V = V
        self.adj = {v: set() for v in V}

    def addEdge(self, u, v):
        self.adj[u].add(v)
        self.adj[v].add(u)

    def count_paths(self, s, d):
        visited = {v: False for v in self.V}
        path_count = [0]
        self.count_paths_util(s, d, visited, path_count)
        return path_count[0]
    
    def count_paths_util(self, u: str, d: str, visited: list, path_count: list):
        if not u.isupper():
            visited[u] = True

        if (u == d):
            path_count[0] += 1
        
        else:
            for v in self.adj[u]:
                if not visited[v]:
                    self.count_paths_util(v, d, visited, path_count)
        visited[u] = False

    def count_paths2(self, s, d):
        visited = {v: 0 for v in self.V}
        visited['start'] = True
        path_count = [0]
        self.count_paths_util2(s, d, visited, path_count, False)
        return path_count[0]
    
    def count_paths_util2(self, u: str, d: str, visited: list, path_count: list, double: bool):
        if (u == d):
            path_count[0] += 1
            return
        visited[u] += 1
        for v in self.adj[u]:
            if v.isupper():
                self.count_paths_util2(v, d, visited, path_count, double)
            elif visited[v] == 0:
                self.count_paths_util2(v, d, visited, path_count, double)
            elif visited[v] == 1 and not double:
                self.count_paths_util2(v, d, visited, path_count, True)
        visited[u] -= 1

def part_1(data):
    graph = Graph(list(set(data.keys())))
    for key in data.keys():
        for destination in data[key]:
            graph.addEdge(key, destination)
    return graph.count_paths('start', 'end')

def part_2(data):
    graph = Graph(list(set(data.keys())))
    for key in data.keys():
        for destination in data[key]:
            graph.addEdge(key, destination)
    return graph.count_paths2('start', 'end')

if __name__ == '__main__':
    utils.TESTING = False

    data = utils.readlines()
    data = process_input(data)

    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))