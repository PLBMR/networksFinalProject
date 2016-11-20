#practiceVisualizingGraph.r
#helper for visualizing our graph

#imports
library(igraph)
library(ggplot2)
library(ggnet)

nodeSize = 2
#load in dataset

givenGraph = read_graph("../data/processed/ukraineNetwork.gml",
                        format = "gml")
ggnet2(givenGraph,node.size = nodeSize)
