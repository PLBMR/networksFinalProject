#makeCountryProjection.py
#helper script that takes the cleaned full network and projecting it into a
#country-based network.

#imports

import networkx as nx
import pandas as pd
import numpy as np

#helpers

def buildCountryNodes(countryProjection,fullNetwork):
    #builds the nodes for the country projection
    countryDict = {}
    for node in fullNetwork.nodes(data = True):
        #get country for node
        nodeCountry = node[1]["countries"]
        if (type(nodeCountry) != str): #unidentified
            nodeCountry = "Not identified"
        if (nodeCountry in countryDict):
            #add 1 to it
            countryDict[nodeCountry] += 1
        else: #initialize it
            countryDict[nodeCountry] = 1
    #then build nodes in countryProjection
    for country in countryDict:
        countryProjection.add_node(country,numAgents = countryDict[country]) 

def buildCountryEdges(countryProjection,fullNetwork):
    #helper for building our country edges
    edgeDict = {} #will add to this
    for edge in fullNetwork.edges():
        #get fromNode country and toNode country
        fromNodeCountry = fullNetwork.node[edge[0]]["countries"]
        toNodeCountry = fullNetwork.node[edge[1]]["countries"]
        #check types
        if (type(fromNodeCountry) != str):
            fromNodeCountry = "Not identified"
        if (type(toNodeCountry) != str):
            toNodeCountry = "Not identified"
        #then add information to edgeDict
        edgeKey = (fromNodeCountry,toNodeCountry)
        if (edgeKey in edgeDict):
            edgeDict[edgeKey] += 1 
        else:
            edgeDict[edgeKey] = 1 #for weight
    #then add these edges
    for edge in edgeDict:
        countryProjection.add_edge(edge[0],edge[1],weight = edgeDict[edge])

def  buildCountryProjection(cleanedNetworkFilename,finalNetworkFilename):
    #primary helper for building our country projection
    fullNetwork = nx.read_gpickle(cleanedNetworkFilename)
    countryProjection = nx.DiGraph()
    #build nodes in countryProjection
    print "Building Country Nodes..."
    buildCountryNodes(countryProjection,fullNetwork)
    print "Nodes Built!"
    #then build edges in countryProjection
    print "Building Country Edges..."
    buildCountryEdges(countryProjection,fullNetwork)
    print "Edges Built!"
    #then save
    nx.write_gml(countryProjection,finalNetworkFilename)

#main process

if __name__ == "__main__":
    cleanedNetworkFilename = "../data/processed/cleanedNetwork.pkl"
    finalNetworkFilename = "../data/processed/countryProjectedNetwork.gml"
    print "Building Country Projection..."
    buildCountryProjection(cleanedNetworkFilename,finalNetworkFilename)
    print "Country-Projection Built."
