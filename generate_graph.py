import random

# Parameters for graph generation
NUM_VERTICES = 8  # небольшой граф для наглядности
NUM_EDGES = 16    # достаточно рёбер для наличия альтернативных путей
MIN_WEIGHT = 1
MAX_WEIGHT = 10

def generate_graph():
    edges = set()
    
    # Сначала создадим остовное дерево, чтобы гарантировать связность графа
    vertices = list(range(1, NUM_VERTICES + 1))
    connected = {1}  # начинаем с вершины 1
    unconnected = set(vertices[1:])
    
    # Создаем остовное дерево
    while unconnected:
        v1 = random.choice(list(connected))
        v2 = random.choice(list(unconnected))
        weight = random.randint(MIN_WEIGHT, MAX_WEIGHT)
        edges.add((min(v1, v2), max(v1, v2), weight))  # сохраняем упорядоченные пары вершин
        connected.add(v2)
        unconnected.remove(v2)
    
    # Добавляем дополнительные рёбра
    while len(edges) < NUM_EDGES:
        v1 = random.randint(1, NUM_VERTICES)
        v2 = random.randint(1, NUM_VERTICES)
        if v1 != v2:
            edge = (min(v1, v2), max(v1, v2), random.randint(MIN_WEIGHT, MAX_WEIGHT))
            edges.add(edge)
    
    return sorted(list(edges))  # сортируем для читаемости

# Генерируем граф и записываем в файл
graph = generate_graph()

with open('graph.txt', 'w') as f:
    f.write(f"{NUM_VERTICES}\n")
    for v1, v2, weight in graph:
        f.write(f"{v1} {v2} {weight}\n")

print(f"Generated graph with {NUM_VERTICES} vertices and {NUM_EDGES} edges")
print("Graph saved to graph.txt") 