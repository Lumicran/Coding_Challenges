# -*- coding: utf-8 -*-


class Graph:
    def __init__(self, nodeList = []):
        
        #mapping of node names to nodes
        self.__nodes__ = {}
          
        for node in nodeList:
            self.__nodes__[node.id] = node
        
        
    def add(self, node):
        self.__nodes__[node.id] = node
        
        
    def getNode(self, id):
        return self.__nodes__.get(id, None)
        
class Node:
    def __init__(self, id, edges = []):
        
        self.id = id
        
        #list of node ids that can be reached from this node
        self.edges = edges


    def addEdge(self, nodeId):
        self.edges.append(nodeId)

    def __repr__(self):
        return self.id
        


def hops(graph, nodeID):
    # return a list of node ID's of all nodes you can reach in 2 hops without any duplicates

    node_set = set([nodeID])

    # Use getNode, passing in nodeID to find starting point
    current = graph.getNode(nodeID)

    # Use .edges to find out which nodes are one hop away from node
    edges = current.edges

    second_hop = []

    for edge in edges:
        node_set.add(edge)

        edge_node = graph.getNode(edge)
        second_hop = edge_node.edges

        for each_id in second_hop:
            node_set.add(each_id)

    return list(node_set)


def node_distance(graph, nodeID1, nodeID2):
    # return 0 if nodeID1 is the same as nodeID2
    # return None if there is no path between the nodes
    # return an integer number of the shortest number of hops that is between the two nodes.

    # to visit, which is a list of nodes to check the id against
    # visited, which is used to check "to visit" against so that there aren't any duplicates
    # next_to_visit, which is used to compare children against visited

    num_hops = 0

    to_visit = [graph.getNode(nodeID1)]
    visited = set()

    while to_visit:
        next_to_visit = []

        for node_ele in to_visit:

            if node_ele.id == nodeID2:
                return num_hops

            visited.add(node_ele)

            # list of one string of node ids
            edges = node_ele.edges
        

            # iterate through node ID list 
            for edge in edges:

                # for each node id, find the actual node and assign to edge
                edge = graph.getNode(edge)

                # if node is not in visited (set of nodes)
                if edge not in visited and edge not in to_visit and edge not in next_to_visit:
                    # Add node to next_to_visit
                    next_to_visit.append(edge)

        to_visit = list(next_to_visit)
        num_hops += 1



    return None

    # Do not mutate            
                # edges = to_visit.pop(0).edges

                # for edge in edges:
                #     to_visit.append(graph.getNode(edge))


if __name__ == "__main__":

    #defines the variable "testGraph"
    exec(open("testData.py").read())

    # print(hops(testGraph, "George"))
    # import pdb

    # pdb.set_trace()

    print(node_distance(testGraph, "Monty", "Angie"))
    # print(testGraph.getNode("Angie").edges)


    # alpha = Graph([Node("A", ["B", "D"]), Node("B", ["A", "C", "D"]), 
    #     Node("C", ["B", "D", "F"]), Node("D", ["C", "B", "A"]), Node("F", ["C"])])

    # print(alpha.getNode("B").edges)

    # print(hops(alpha, "B"))
    # print(hops(alpha, "F"))    

    # print(node_distance(alpha, "A", "C"))
    # print(node_distance(alpha, "A", "F"))
    # print(node_distance(alpha, "A", "A"))
    # print(node_distance(alpha, "A", "E"))

        
        
