#processCSVFiles.py
#helper script that processes our .csv files for us

#imports

import networkx as nx
import pandas as pd
import os

#helper functions

def getEdgesAndEntityFilenames(csvDir):
    #helper that getes our edge and entity filenames from the csv directory
    edgeFilename = None
    entityFilenameList = [] #will build on this
    for filename in os.listdir(csvDir):
        if ("edge" in filename.lower()): #make this our edge filename
            edgeFilename = csvDir + os.sep + filename
        else:
            entityFilenameList.append(csvDir + os.sep + filename)
    return (edgeFilename,entityFilenameList)

def addEntities(givenNet,entityFilename):
    #helper that adds entities to the given network
    entityFrame = pd.read_csv(entityFilename)
    nodeIDList = list(entityFrame["node_id"])
    givenNet.add_nodes_from(nodeIDList)

def addEdges(givenNet,edgeFilename):
    #helper that adds edges to given network
    edgeFrame = pd.read_csv(edgeFilename)
    #then get nodes
    getEdgeTup = lambda s : (s["node_1"],s["node_2"])
    edgeTupleList = list(edgeFrame.apply(getEdgeTup,axis = 1))
    givenNet.add_edges_from(edgeTupleList)

def buildNetwork(csvDir,exportFilename):
    #function that performs the process of building our network
    givenNet = nx.Graph()
    #get list of entities and our edges
    (edgeFilename,entityFilenameList) = getEdgesAndEntityFilenames(csvDir)
    #then add all entities
    for entityFilename in entityFilenameList:
        addEntities(givenNet,entityFilename)
    #then add edges
    addEdges(givenNet,edgeFilename)
    nx.write_gml(givenNet,exportFilename)

#main process

if __name__ == "__main__":
    #get entity name list
    csvDir = "../data/raw/csvFiles"
    exportFilename = "../data/processed/fullNetwork.gml"
    buildNetwork(csvDir,exportFilename)
