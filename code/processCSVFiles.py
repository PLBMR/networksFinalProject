#processCSVFiles.py
#helper script that processes our .csv files for us

#imports

import networkx as nx
import pandas as pd
import re
import os

#helper functions

def getEdgesAndEntityFilenames(csvDir):
    #helper that getes our edge and entity filenames from the csv directory
    edgeFilename = None
    entityFilenameList = [] #will build on this
    for filename in os.listdir(csvDir):
        if ("edge" in filename.lower()): #make this our edge filename
            edgeFilename = csvDir + os.sep + filename
        elif ("ignore" not in filename.lower()):
            entityFilenameList.append(csvDir + os.sep + filename)
    return (edgeFilename,entityFilenameList)

def createNode(nodeRow):
    #helper that creates information for given node row
    nodeID = nodeRow["node_id"]
    nodeDict = dict(zip(list(nodeRow.index),list(nodeRow)))
    #then clean keys
    cleanedNodeDict = {} #we will add to this
    for key in nodeDict:
        value = nodeDict[key]
        newKey = re.sub("_","",key)
        cleanedNodeDict[newKey] = value
    print cleanedNodeDict
    return (nodeID,cleanedNodeDict)

def addEntities(givenNet,entityFilename):
    #helper that adds entities to the given network
    entityFrame = pd.read_csv(entityFilename)
    entityFrame = entityFrame[entityFrame["country_codes"] == "USA"]
    #get entity type
    entityFileList = entityFilename.split(os.sep)
    entityType = entityFileList[len(entityFileList) - 1]
    entityType = entityType[0:(len(entityType) - len(".csv"))]
    #then transfer node list
    nodeIDList = list(entityFrame.apply(createNode,axis = 1))
    givenNet.add_nodes_from(nodeIDList,entType = entityType)

def addEdges(givenNet,edgeFilename):
    #helper that adds edges to given network
    edgeFrame = pd.read_csv(edgeFilename)
    edgeFrame = edgeFrame[(edgeFrame["node_1"].isin(givenNet.nodes())) &
                          (edgeFrame["node_2"].isin(givenNet.nodes()))]
    print edgeFrame.shape
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
    exportFilename = "../data/processed/easternEuropeNetwork.gml"
    buildNetwork(csvDir,exportFilename)
