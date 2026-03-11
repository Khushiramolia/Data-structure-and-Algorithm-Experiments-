class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)] #Each node starts as its own parent so each node is its own set representative.
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node]) #finds the leader of a set and connects every node on the way directly to the leader to make future searches faster.
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v #joins two sets together and always attaches the smaller tree under the bigger one so the structure stays small and efficient.
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal_mst(V, edges):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(V)
    mst = []
    total_cost = 0.0

    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v) #This function picks the cheapest edges one by one and connects them without forming a cycle to build the Minimum Spanning Tree.
            mst.append((u, v, w))
            total_cost += w

    print("\nEdges in the Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"{u+1} -- {v+1}  weight: {w:.2f}")  # +1 to display original 1-indexed input
    print(f"Total weight of MST = {total_cost:.2f}")


if __name__ == "__main__":
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))

    edges = []
    print("Enter each edge as: vertex1 vertex2 weight (decimal allowed)")
    for i in range(E):
        u, v, w = input(f"Edge {i+1}: ").split()
        u, v, w = int(u)-1, int(v)-1, float(w)  # convert to 0-index internally
        edges.append((u, v, w))

    kruskal_mst(V, edges)


#The time complexity of Kruskal’s Algorithm is O(E log E) because it first sorts all edges by weight. The union–find operations with path compression take almost constant time, so the sorting step dominates.