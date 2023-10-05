import tkinter as tk
import heapq

# Definir una representación del grafo de trayectos
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

def dijkstra(graph, start, end):
    # Inicializar distancias y camino
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Construir el camino mínimo
    path = []
    current = end
    while current != start:
        path.insert(0, current)
        current = previous_nodes[current]
    path.insert(0, start)

    return distances[end], path

def find_shortest_path():
    start_station = entry_start.get()
    end_station = entry_end.get()

    if start_station not in graph or end_station not in graph:
        result_label.config(text="Estación inicial o final no válida.")
        return

    shortest_distance, shortest_path = dijkstra(graph, start_station, end_station)
    result_label.config(text=f"Distancia mínima: {shortest_distance}\nRuta más corta: {' -> '.join(shortest_path)}")

# Crear la ventana
window = tk.Tk()
window.title("Encontrar Camino Mínimo")

# Crear etiquetas y campos de entrada
start_label = tk.Label(window, text="Estación Inicial:")
entry_start = tk.Entry(window)

end_label = tk.Label(window, text="Estación Final:")
entry_end = tk.Entry(window)

result_label = tk.Label(window, text="")

# Crear botón para encontrar el camino mínimo
find_button = tk.Button(window, text="Encontrar Camino Mínimo", command=find_shortest_path)

# Colocar los elementos en la ventana
start_label.pack()
entry_start.pack()
end_label.pack()
entry_end.pack()
find_button.pack()
result_label.pack()

# Iniciar la ventana
window.mainloop()
