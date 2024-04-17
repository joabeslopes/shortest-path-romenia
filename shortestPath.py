from heapq import heappop, heappush
from sys import maxsize


class Node:
    def __init__(self, name: str, neighbors: list):
        self.name = name
        self.neighbors = {neighbor[0]: neighbor[1] for neighbor in neighbors}

    def getDistance(self, node: str):
        return self.neighbors.get(node, maxsize)


def dijkstra(graph: dict, sourceNode: str):
    dist = {city: maxsize for city in graph}
    dist[sourceNode] = 0
    nodes = {city: None for city in graph}
    open_nodes = [(0, sourceNode)]

    while open_nodes:
        currentDistance, currentNode = heappop(open_nodes)

        if currentDistance > dist[currentNode]:
            continue

        for neighbor, distance in graph[currentNode].neighbors.items():
            new_distance = dist[currentNode] + distance
            if new_distance < dist[neighbor]:
                dist[neighbor] = new_distance
                nodes[neighbor] = currentNode
                heappush(open_nodes, (new_distance, neighbor))

    return dist, nodes


def shortestPath(graph: dict, sourceNode: str, destNode: str):
    distances, nodes = dijkstra(graph, sourceNode)
    path = []
    distance = distances[destNode]

    current = destNode
    while current is not None:
        path.append(current)
        current = nodes[current]
    path.reverse()

    return path, distance


def createGraph():
    cityList = [
        "Oradea", "Zerind", "Arad", "Timisoara", "Lugoj",
        "Mehadia", "Dobreta", "Sibiu", "Rimnicu Vilcea", "Craiova",
        "Fagaras", "Pitesti", "Bucharest", "Giurgiu", "Urziceni",
        "Vaslui", "Iasi", "Neamt", "Hirsova", "Eforie"
    ]

    neighborsList = [
        [["Sibiu", 151], ["Zerind", 71]],
        [["Oradea", 71], ["Arad", 75]],
        [["Zerind", 75], ["Sibiu", 140], ["Timisoara", 118]],
        [["Arad", 118], ["Lugoj", 111]],
        [["Timisoara", 111], ["Mehadia", 70]],
        [["Lugoj", 70], ["Dobreta", 75]],
        [["Mehadia", 75], ["Craiova", 120]],
        [["Arad", 140], ["Oradea", 151], ["Fagaras", 99], ["Rimnicu Vilcea", 80]],
        [["Sibiu", 80], ["Craiova", 146], ["Pitesti", 97]],
        [["Dobreta", 120], ["Rimnicu Vilcea", 146], ["Pitesti", 138]],
        [["Sibiu", 99], ["Bucharest", 211]],
        [["Rimnicu Vilcea", 97], ["Bucharest", 101], ["Craiova", 138]],
        [["Fagaras", 211], ["Pitesti", 101], ["Giurgiu", 90], ["Urziceni", 85]],
        [["Bucharest", 90]],
        [["Bucharest", 85], ["Hirsova", 98], ["Vaslui", 142]],
        [["Urziceni", 142], ["Iasi", 92]],
        [["Vaslui", 92], ["Neamt", 87]],
        [["Iasi", 87]],
        [["Urziceni", 98], ["Eforie", 86]],
        [["Hirsova", 86]]
    ]

    graph = {}
    for c in range(len(cityList)):
        city = cityList[c]
        neighbors = neighborsList[c]
        graph[city] = Node(city, neighbors)

    return graph


graph = createGraph()

print(shortestPath(graph, "Arad", "Rimnicu Vilcea"))
