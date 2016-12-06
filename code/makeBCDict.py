#makeBCDict.py
#quick subroutine to make the betweenness centrality dictionary independent of
#my notebook analysis

#imports

import pandas as pd
import numpy as np
import cPickle as cpkl
import networkx as nx

#then the general process

mainNetwork = nx.read_gpickle("../data/processed/doesBusinessWith.pkl")
numNodesConsidered = 90 #for sampling purposes
bcDict = nx.betweenness_centrality(mainNetwork,k = numNodesConsidered)
cpkl.dump(bcDict,open("../data/processed/newBCDict.pkl","wb"))
