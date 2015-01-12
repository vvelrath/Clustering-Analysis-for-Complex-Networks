# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Vivekanandh"
__date__ ="$Nov 18, 2014 8:05:28 PM$"

import csv
import os
import sys
from numpy import *
import numpy
from collections import defaultdict
        

#Function to check for convergence
def checkForConvergence(previous_matrix, current_matrix):
    convergence = 1
    for i in range(num_vertices):
        for j in range(num_vertices):
            if previous_matrix[i][j] != current_matrix[i][j]:
                convergence = 0
                break
    return convergence

#-------------------------------------------------------------------------------
#Main code starts

#Parsing Arguments
len_of_argv = len(sys.argv)
for a in range(len_of_argv):
    if sys.argv[a] == '-f':
        fileName = str(sys.argv[a + 1])
    elif sys.argv[a] == '-e':    
        exp = int(sys.argv[a + 1])
    elif sys.argv[a] == '-r':
        r = float(sys.argv[a + 1])
    else:
        continue

with open(os.path.join(fileName)) as file:
    if "yeast_undirected_metabolic" in fileName:
        reader = csv.reader(file,delimiter = '\t')
    else:
        reader = csv.reader(file,delimiter = ' ')
    edges = list(reader)
    
#Indexing matrix
indexing_matrix = defaultdict(int)
index_to_labels = defaultdict(int)
index = -1
for edge in edges:
    if(indexing_matrix.get(edge[0]) == None):
        index = index + 1
        indexing_matrix[edge[0]] = index
        index_to_labels[index] = edge[0]
    if(indexing_matrix.get(edge[1]) == None):
        index = index + 1
        indexing_matrix[edge[1]] = index
        index_to_labels[index] = edge[1]
        
#Number of vertices
num_vertices = len(indexing_matrix)

#Calculating the adjacency matrix
adj_matrix = [[0 for j in range(num_vertices)] for i in range(num_vertices)]
adj_matrix = numpy.asarray(adj_matrix).astype(float)

for edge in edges:
    adj_matrix[indexing_matrix.get(edge[0])][indexing_matrix.get(edge[1])] = 1
    adj_matrix[indexing_matrix.get(edge[1])][indexing_matrix.get(edge[0])] = 1
    
#Adding self loops
for i in range(num_vertices):
    adj_matrix[i][i] = 1

#Normalising the matrix
num_outgoing_links = adj_matrix.sum(axis=0)
markov_matrix = adj_matrix / num_outgoing_links[numpy.newaxis, :]

previous_matrix = markov_matrix

var = 1; i = 0
while var == 1:
    
    i += 1
    print "Iteration",i 
    
    #Expand the matrix by taking the power of the matrix
    markov_matrix = numpy.linalg.matrix_power(markov_matrix, exp)
    
    #Inflate the markov matrix by taking A.*A
    markov_matrix = numpy.power(markov_matrix, r)

    #Normalising the matrix
    num_outgoing_links = markov_matrix.sum(axis=0)
    markov_matrix = markov_matrix / num_outgoing_links[numpy.newaxis, :]

    #Rounding off to two decimal places
    markov_matrix =  markov_matrix.round(4)
    
    #Comparing the previous and the current matrix to check for convergenge
    if checkForConvergence(previous_matrix, markov_matrix) == 1:
        break
        
    #Assigning the previous matrix to be the markov matrix
    previous_matrix = markov_matrix    

#Finding clusters from the doubly idempotent matrix    
visited = defaultdict(int)
cluster_no = 1
cluster = [0 for i in range(num_vertices)]

for i in range(num_vertices):
    has_clusters = 0
    for j in range(num_vertices):
        if markov_matrix[i][j] > 0 and visited.get(j) == None:
            has_clusters = 1
            cluster[j] = cluster_no
            visited[j] = 1
    if has_clusters == 1:
        cluster_no = cluster_no + 1

#Writing the clusters to the file
f = open(fileName.split('.')[0]+'.clu', 'w')
f.write("*Partition ")
f.write(os.path.basename(fileName).split('.')[0]+"\n")
f.write("*Vertices ")
f.write(str(num_vertices)+"\n")

f = open(fileName.split('.')[0]+'.clu', 'a')
numpy.savetxt(f, cluster, fmt='%d')

print cluster
print "Number of clusters:",cluster_no - 1