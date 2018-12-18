#!/usr/bin/env python3
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

import pdb

def node_path(graph, nodeID1, nodeID2):
    # return list with single nodeID, if start is same as end location
    # return None if there is no path between the nodes
    # otherwise, return a list of nodeIDs corresponding to the shortest path from nodeID1 to nodeID2
    # nodeID1 should be first element, nodeID2 should be the last

    if nodeID1 == nodeID2:
        return [nodeID1]

    # stack of nodes we want to visit
    to_visit = [nodeID1]

    # dictionary of node ids along with their previous nodes
    node_dict = {}

    # list of nodes that we can return as a result
    traversal_path = []

    for node_id in to_visit:

        if node_id == nodeID2:
            # pdb.set_trace()

            while node_id != nodeID1:
                traversal_path += [node_id]
                node_id = node_dict[node_id]

            traversal_path += [node_id]
            traversal_path.reverse()
            return traversal_path

        edges = graph.getNode(node_id).edges

        for edge in edges:
            if edge not in node_dict:
                node_dict[edge] = node_id

            if edge not in to_visit:
                to_visit.append(edge)

    return None


if __name__ == "__main__":

    #defines the variable "testGraph"
    exec(open("testData.py").read())
    print(node_path(testGraph, "Monty", "Angie"))
    print(node_path(testGraph, "Monty", "Adolf"))
