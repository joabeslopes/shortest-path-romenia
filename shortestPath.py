from sys import maxsize

class Node:
    def __init__(self, name:str, neighbors:list):
        self.name = name
        self.neighbors = neighbors
    
    def getDistance(self, node:str):
        for n in self.neighbors:
            if n[0] == node:
                return n[1]


def dijkstra(graph:dict, sourceNode:str):
    n = len(graph)
    dist = {city: maxsize for city in graph}
    dist[sourceNode] = 0
    nodes = {city: None for city in graph}
    nodes[sourceNode] = graph[sourceNode]
    closed = []

    while (len(closed) < len(graph)):
        currentDistance = min(distance for distance in dist if distance not in closed)
        closed.append(currentDistance)

        currVertex = graph[currentDistance]

        for n in currVertex.neighbors:
            neighbor = n[0]
            distance = currVertex.getDistance(neighbor)
            new_distance = dist[currentDistance] + distance
            if new_distance < dist[neighbor]:
                dist[neighbor] = new_distance
                nodes[neighbor] = currVertex
    return dist, nodes

def shortestPath(graph:dict, sourceNode:str, destNode:str):
    distances, nodes = dijkstra(graph, sourceNode)
    path = []
    distance = distances[destNode]

    current = destNode
    while sourceNode not in path:
        path.append(current)
        current = nodes[current].name
    path.reverse()
    return path, distance

def createGraph():
    cityList = [
                "Oradea", 
                "Zerind", 
                "Arad", 
                "Timisoara", 
                "Lugoj",
                "Mehadia",
                "Dobreta",
                "Sibiu",
                "Rimnicu Vilcea",
                "Craiova",
                "Fagaras",
                "Pitesti",
                "Bucharest",
                "Giurgiu",
                "Urziceni",
                "Vaslui",
                "Iasi",
                "Neamt",
                "Hirsova",
                "Eforie"
                ]

    neighborsList = [
                    [["Sibiu", 151], ["Zerind", 71]], 
                    [["Oradea", 71], ["Arad", 75]],  
                    [["Zerind", 75], ["Sibiu", 140], ["Timisoara", 118]], 
                    [["Arad", 118], ["Lugoj", 111]], 
                    [["Timisoara", 111], ["Mehadia", 70]],
                    [["Lugoj", 70], ["Dobreta", 75] ],
                    [ ["Mehadia", 75], ["Craiova",120] ],
                    [["Arad", 140], ["Oradea", 151], ["Fagaras", 99], ["Rimnicu Vilcea", 80] ],
                    [ ["Sibiu", 80], ["Craiova", 146], ["Pitesti", 97] ],
                    [ ["Dobreta", 120], ["Rimnicu Vilcea", 146], ["Pitesti", 138] ],
                    [ ["Sibiu", 99], ["Bucharest", 211] ],
                    [ ["Rimnicu Vilcea", 97], ["Bucharest", 101], ["Craiova", 138] ],
                    [ ["Fagaras", 211], ["Pitesti", 101], ["Giurgiu", 90], ["Urziceni", 85] ],
                    [ ["Bucharest", 90] ],
                    [ ["Bucharest", 85], ["Hirsova", 98], ["Vaslui", 142] ],
                    [["Urziceni", 142], ["Iasi", 92]],
                    [["Vaslui", 92], ["Neamt", 87] ],
                    [["Iasi", 87]],
                    [["Urziceni", 98], ["Eforie", 86] ],
                    [["Hirsova", 86]]
                    ]

    graph = {}
    for c in range(len(cityList)):
        city = cityList[c]
        neighbors = neighborsList[c]
        graph[city] = Node(city, neighbors)

    return graph


graph = createGraph()

print ( shortestPath(graph, "Arad", "Bucharest") )
