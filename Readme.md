MARKOV CLUSTERING ALGORITHM
==================================

### Team members

Vivekanandh Vel Rathinam (vvelrath@buffalo.edu), Amitha Narasimha Murthy (amithana@buffalo.edu), 
Neeti Narayan (neetinar@buffalo.edu)

### Description

The objective of this assignment is to implement the Markov Clustering Algorithm and apply the algorithm to the given three datasets, AT&T Web network, physics collaboration network, and the yeast metabolic network

### Implementation

We have implemented the MCL using python as the programming language. We give as input to the program the following												
1. Path of the file which has the vertices and edges[-f filepath]																								
2. Expansion factor(e) [-e expansion]																															
3. Inflation factor(r) [-r inflation]																												

### Program Execution

1) Run the markovclustering.py with three parameters																		
   [-f file_path]																				
   [-e expansion_factor]																						
   [-r inflation_factor]																													
2) The Partition file(.clu) is generated in the same directory as the input file(.txt)															
3) The networking file(.net) is file given to us for the home work. No changes were made to the file														
3) Import the network file and the partition file into pajek and cross-check the results																	