def createGraph():
    cityList = [
        "Oradea", "Zerind", "Arad", "Timisoara", "Sibiu", 
        "Bucharest", "Cluj-Napoca", "Iasi", "Constanta", "Craiova", 
        "Brasov", "Galati", "Ploiesti", "Braila", "Bacau"
    ]
    neighborsList = [
        [["Zerind", 71], ["Sibiu", 151]], 
        [["Arad", 75], ["Oradea", 71]], 
        [["Zerind", 75], ["Timisoara", 118], ["Sibiu", 140]],
        [["Arad", 118], ["Lugoj", 70]],
        [["Oradea", 151], ["Arad", 140], ["Fagaras", 99]],
        [["Ploiesti", 60], ["Pitesti", 100]],
        [["Turda", 40]], 
        [["Vaslui", 80], ["Bacau", 90]],
        [["Mangalia", 45]], 
        [["Pitesti", 108]], 
        [["Sibiu", 141], ["Ploiesti", 171]],
        [["Braila", 25]], 
        [["Bucharest", 60], ["Brasov", 171]],
        [["Galati", 25]],
        [["Iasi", 90], ["Piatra Neamt", 80]]
    ]

    graph = {}
    for c, city in enumerate(cityList):
        neighbors = neighborsList[c]
        graph[city] = Node(city, neighbors)
    return graph

graph = createGraph()
print(shortestPath(graph, "Arad", "Oradea"))
