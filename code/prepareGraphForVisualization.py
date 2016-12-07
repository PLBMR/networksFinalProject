#prepareGraphForVisualization.py
#helper that prepares our graph for visualization by removing many low-degree
#nodes

#imports

import networkx as nx
import sys

#helpers

def getNodesBelowGivenDegree(givenNet,givenDegree):
    #finds the nodes below a given degree
    nodeBelowDegreeList = []
    #get degree
    degreeDict = givenNet.degree()
    for nodeInd in degreeDict:
        if (degreeDict[nodeInd] < givenDegree):
            nodeBelowDegreeList.append(nodeInd)
    return nodeBelowDegreeList

def deleteNodesBelowGivenDegree(givenNet,givenDegree):
    #helper that deletes nodes from givenNet that are below a given degree
    nodeBelowDegreeList = getNodesBelowGivenDegree(givenNet,givenDegree)
    givenNet.remove_nodes_from(nodeBelowDegreeList)

def deleteAndExport(netImportName,givenDegree,netExportName):
    #the proces that imports a graph, deletes nodes below a given degree,
    #and exports them to a new graph
    importedGraph = nx.read_gpickle(netImportName)
    deleteNodesBelowGivenDegree(importedGraph,givenDegree)
    #then export
    print len(importedGraph.nodes()), "nodes left."
    nx.write_gml(importedGraph,netExportName)

#the main process

if __name__ == "__main__":
    #get command line arguments
    args = sys.argv
    args = args[1:] #gets rid of name of python file
    #get import, export, and degree name
    importFilename = args[0]
    exportFilename = args[1]
    degreeCutoff = int(args[2])
    #then perform our process
    deleteAndExport(importFilename,degreeCutoff,exportFilename)
