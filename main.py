class Node:
    def __init__(self, nodeName, straightLineDistance):
        # index of connections and connectionCosts line up.
        # Connections[0] corresponds to connectionCost[0]
        self.connections = []  # list of accessible nodes from self.node
        self.connectionCost = []  # cost of getting to node from self.node
        self.nodeName = nodeName  # name of self.node
        # estimate between node and goal state, must be bellow or equal to real distance
        self.h = straightLineDistance  # h(n) of self.node
        self.g = 0
        self.f = 0

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


def makePath(previousNode, currentNode):
    path = [currentNode]
    for i in range(0, len(previousNode)):
        currentNode = previousNode[currentNode]
        path.append(currentNode)
    print("Path size = " + str(len(path)))
    for i in range(0, len(path)):
        print("Path: " + path[i])


if __name__ == '__main__':
    startingNode = input("Enter starting node: ")
    print("From city : " + startingNode)
    print("To city: Bucharest")
    nodes = createNodes()
    createConnections(nodes)

    # creates dictionary to reference location indexes in the node array
    dict = {}
    for i in range(0, len(nodes)):
        dict[nodes[i].nodeName] = i

    currentNode = nodes[dict[startingNode]]

    currentNode.f = nodes[dict[startingNode]].h
    discoveredNodes = [currentNode]
    previousNode = {}
    while discoveredNodes:
        currentNode = discoveredNodes[0]
        for i in range(0, len(discoveredNodes)):
            if discoveredNodes[i].f < currentNode.f:
                currentNode = discoveredNodes[i]

        print("currentNode.F: " + currentNode.nodeName + " " + str(currentNode.f))

        if currentNode.h == 0:
            makePath(previousNode, currentNode.nodeName)
            break

        # removes the current nodes from the discovered list
        for i in range(0, len(discoveredNodes)):
            if discoveredNodes[i].nodeName == currentNode.nodeName:
                del discoveredNodes[i]
                break

        # loops through all nodes currentNode connects to
        for i in range(0, len(currentNode.connections)):

            # node connecting to current Node
            nextNode = nodes[dict[currentNode.connections[i]]]
            # cost to get to nextNode from currentNode
            nextNodeCost = currentNode.connectionCost[i]
            # print(currentNode.g)

            nextNode.g = int(currentNode.g) + int(nextNodeCost)

            potentialGScoreForNextNode = int(currentNode.g) + int(nextNodeCost)
            print("nextNode.Name: " + nextNode.nodeName)
            print("porentailGScoreForNextNode: " + str(potentialGScoreForNextNode))
            print("nextNode.G: " + str(nextNode.g))

            if potentialGScoreForNextNode < nextNode.g:
                print("goes in here")
                previousNode[nextNode.nodeName] = currentNode.nodeName
                nextNode.g = potentialGScoreForNextNode
                # adds g + h to get f for node we are moving to
                nextNode.f = nextNode.g + nextNode.h
                if nextNode not in discoveredNodes:
                    discoveredNodes.append(nextNode)
            elif nextNode not in discoveredNodes:
                previousNode[nextNode.nodeName] = currentNode.nodeName
                nextNode.g = potentialGScoreForNextNode
                # adds g + h to get f for node we are moving to
                nextNode.f = nextNode.g + nextNode.h
                discoveredNodes.append(nextNode)

    print("failed")
    print(currentNode.f)

# TODO find a more efficient way to make connections between nodes.
# TODO find a more efficient way to make connections between nodes.
# TODO create function to keep track of visited nodes
# TODO The total cost of path is not being added properly, likely do to with the weird way i implemented the connections
