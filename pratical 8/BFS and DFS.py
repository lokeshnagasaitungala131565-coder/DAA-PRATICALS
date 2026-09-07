from collections import deque
import time

class Graph:
    def __init__(self, V):
        self.adj = [[] for _ in range(V)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, start):
        visited = set()
        result = []

        def visit(v):
            visited.add(v)
            result.append(v)
            for n in self.adj[v]:
                if n not in visited:
                    visit(n)

        visit(start)
        return result

    def bfs(self, start):
        visited = {start}
        q = deque([start])
        result = []

        while q:
            v = q.popleft()
            result.append(v)
            for n in self.adj[v]:
                if n not in visited:
                    visited.add(n)
                    q.append(n)

        return result


V = int(input("Vertices: "))
E = int(input("Edges: "))

g = Graph(V)

print("Enter edges:")
for _ in range(E):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start = int(input("Starting vertex: "))

t1 = time.perf_counter_ns()
dfs = g.dfs(start)
t2 = time.perf_counter_ns()

t3 = time.perf_counter_ns()
bfs = g.bfs(start)
t4 = time.perf_counter_ns()

print("\nDFS:", *dfs)
print("BFS:", *bfs)
print("DFS Time:", t2 - t1, "ns")
print("BFS Time:", t4 - t3, "ns")
print("Time Complexity: O(V + E)")