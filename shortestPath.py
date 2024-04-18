from heapq import heappop, heappush
from sys import maxsize


class Node:
    def __init__(self, name: str, neighbors: dict):
        self.name = name
        self.neighbors = neighbors

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

    cityList = {
        "Oradea": {"Sibiu": 151, "Zerind": 71},
        "Zerind": {"Oradea": 71, "Arad": 75},
        "Arad": {"Zerind": 75, "Sibiu": 140, "Timisoara": 118},
        "Timisoara": {"Arad": 118, "Lugoj": 111},
        "Lugoj": {"Timisoara": 111, "Mehadia": 70},
        "Mehadia": {"Lugoj": 70, "Dobreta": 75},
        "Dobreta": {"Mehadia": 75, "Craiova": 120},
        "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
        "Rimnicu Vilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97},
        "Craiova": {"Dobreta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
        "Fagaras": {"Sibiu": 99, "Bucharest": 211},
        "Pitesti": {"Rimnicu Vilcea": 97, "Bucharest": 101, "Craiova": 138},
        "Bucharest": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85},
        "Giurgiu": {"Bucharest": 90},
        "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
        "Vaslui": {"Urziceni": 142, "Iasi": 92},
        "Iasi": {"Vaslui": 92, "Neamt": 87},
        "Neamt": {"Iasi": 87},
        "Hirsova": {"Urziceni": 98, "Eforie": 86},
        "Eforie": {"Hirsova": 86}
    }

    graph = {}
    for city, neighbors in cityList.items():
        graph[city] = Node(city, neighbors)

    return graph


graph = createGraph()

print(shortestPath(graph, "Arad", "Bucharest"))
