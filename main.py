class Node:
    def __init__(self, nodeName, straightLineDistance):
        # index of connections and connectionCosts line up.
        # Connections[0] corresponds to connectionCost[0]
        self.connections = []  # list of accessible nodes from self.node
        self.connectionCost = []  # cost of getting to node from self.node
        self.nodeName = nodeName  # name of self.node
        # estimate between node and goal state, must be bellow or equal to real distance
        self.straightLineDistance = straightLineDistance  # h(n) of self.node

    # adds the name and cost from self.node to another node
    def addConnection(self, nodeName, cost):
        self.connections.append(nodeName)
        self.connectionCost.append(cost)


# reads data from distance.txt file and creates the nodes
# returns an array of type nodes containing the all nodes generated from the distance.txt text file
def createNodes():
    f1 = open("distances.txt", "r")
    rawDistances = f1.read()

    rawDistances = rawDistances.split("\n")
    nodes = []

    for i in range(0, len(rawDistances)):
        temp = rawDistances[i].split("-")
        nodes.append(Node(temp[0], int(temp[1])))

    return nodes


# reads data from map.txt and creates all the connections
def createConnections(nodes):
    f2 = open("map.txt", "r")
    rawMap = f2.read()

    rawMap = rawMap.replace("-", ",")
    rawMap = rawMap.split("\n")

    for i in range(0, len(nodes)):
        tempMap = rawMap[i].split(",")
        for j in range(1, len(tempMap)):
            tempMap1 = tempMap[j].split("(")
            nodes[i].addConnection(tempMap1[0], tempMap1[1][0:len(tempMap1[1]) - 1])


if __name__ == '__main__':
    nodes = createNodes()
    createConnections(nodes)
   #  print(nodes[1].connections[1] + " " + nodes[1].connectionCost[1])
    visted = []
    visted.append(nodes[0])
    # creates dictionary to reference location indexes in the node array
    dict = {}
    for i in range(0, len(nodes)):
        dict[nodes[i].nodeName] = i
    print(nodes[dict["Bucharest"]].straightLineDistance)


# TODO find a more efficient way to make connections between nodes.
# TODO create function to keep track of visited nodes
# TODO create function to calculate h(n) + g(n)
