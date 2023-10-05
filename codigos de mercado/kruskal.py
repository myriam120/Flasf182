import tkinter as tk

def kruskal(graph):
    def find(parent, vertex):
        if parent[vertex] == vertex:
            return vertex
        return find(parent, parent[vertex])
    
    def union(parent, rank, u, v):
        root_u = find(parent, u)
        root_v = find(parent, v)
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

    graph = sorted(graph, key=lambda x: x[2])  # Ordenar aristas por peso
    num_vertices = len(set(v for u, v, w in graph))
    parent = {i: i for i in range(num_vertices)}
    rank = {i: 0 for i in range(num_vertices)}
    minimum_spanning_tree = []

    for u, v, weight in graph:
        if find(parent, u) != find(parent, v):
            minimum_spanning_tree.append((u, v, weight))
            union(parent, rank, u, v)

    return minimum_spanning_tree

def find_min_path():
    vertices = entry_vertices.get().split(',')
    edges = entry_edges.get().split(',')
    weights = entry_weights.get().split(',')
    
    graph = []
    
    for edge, weight in zip(edges, weights):
        u, v = edge.split('-')
        graph.append((u, v, int(weight)))
    
    minimum_spanning_tree = kruskal(graph)
    result_label.config(text="Camino mínimo:\n" + '\n'.join([f"{u}-{v}: {w}" for u, v, w in minimum_spanning_tree]))

# Crear la ventana
window = tk.Tk()
window.title("Algoritmo de Kruskal")

# Crear etiquetas y campos de entrada
vertices_label = tk.Label(window, text="Vértices (separados por coma):")
entry_vertices = tk.Entry(window)

edges_label = tk.Label(window, text="Aristas (formato u-v, separadas por coma):")
entry_edges = tk.Entry(window)

weights_label = tk.Label(window, text="Pesos de las aristas (separados por coma):")
entry_weights = tk.Entry(window)

result_label = tk.Label(window, text="")

# Crear botón para encontrar el camino mínimo
find_button = tk.Button(window, text="Encontrar Camino Mínimo", command=find_min_path)

# Colocar los elementos en la ventana
vertices_label.pack()
entry_vertices.pack()
edges_label.pack()
entry_edges.pack()
weights_label.pack()
entry_weights.pack()
find_button.pack()
result_label.pack()

# Iniciar la ventana
window.mainloop()
