class Node:
    def __init__(self, nodeName, straightLineDistance):
        # index of connections and connectionCosts line up.
        # Connections[0] corresponds to connectionCost[0]
        self.connections = []  # list of accessible nodes from self.node
        self.connectionCost = []  # cost of getting to node from self.node
        self.nodeName = nodeName  # name of self.node
        # estimate between node and goal state, must be bellow or equal to real distance
        self.h = straightLineDistance  # h(n) of self.node
        self.g = float('inf')
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


if __name__ == '__main__':

    startingNode = input("Enter starting node: ")
    print("From city : " + startingNode)
    print("To city: Bucharest")
    nodes = createNodes()
    createConnections(nodes)

    #tempNode = nodes[0]
   # tempNode.nodeName = "test"
   # print(nodes[0].nodeName)

    # creates dictionary to reference location indexes in the node array
    dict = {}
    for i in range(0, len(nodes)):
        dict[nodes[i].nodeName] = i
    currentNode = nodes[dict[startingNode]]
    currentNode.f = nodes[dict[startingNode]].h
    visted = []
    visted.append(currentNode)
    while True:
        smallestF = float('inf')
        smallestFPath = ''
        for i in range(0, len(currentNode.connections)):

            # calculates and stores g(n), and f(n) in the respective nodes
            # moves cost to get to node n-1 to node n
            nextNode = nodes[dict[currentNode.connections[i]]]

            nextNodeCost = currentNode.connectionCost[i]

            # adds cost of new node to n
            potentialGScoreForNextNode = nextNodeCost + currentNode.g
            # nextNode.g = int(nextNodeCost) + int(currentNode.g)
            if potentialGScoreForNextNode < nextNode.g:
                nextNode.g = potentialGScoreForNextNode
                # adds g + h to get f for node we are moving to
                nextNode.f = nextNode.g + nextNode.h
            if nextNode not in visted:
                visted.append(nextNode)

            # will be used for visited list
            #for j in range(0, len(visted)):
                #if nextNode.f > visted[j].f:
                    #print("This is going off")
                    #test = 1

            if nextNode.f < smallestF:
                smallestF = nextNode.f
                smallestFPath = nextNode



        #print(currentNode.nodeName)
        print("Cost so far to " + smallestFPath.nodeName + " " + str(smallestFPath.g))

        visted.append(currentNode)
        currentNode = smallestFPath

        if smallestFPath.nodeName == "Bucharest":
            print(currentNode.nodeName)
            break


# TODO find a more efficient way to make connections between nodes.
# TODO create function to keep track of visited nodes
# TODO The total cost of path is not being added properly, likely do to with the weird way i implemented the connections
