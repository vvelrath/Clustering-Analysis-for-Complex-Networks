# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Vivekanandh"
__date__ ="$Nov 22, 2014 3:38:21 AM$"

if __name__ == "__main__":
    print "Hello World"

#Function to multiply two matrices
def multiplyMatrices(markov_matrix1, markov_matrix2):
    num_vertices = len(markov_matrix1)
    new_matrix = [[0 for j in range(num_vertices)] for i in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(num_vertices):
            for k in range(num_vertices):
                new_matrix[i][j] = new_matrix[i][j] + (markov_matrix1[i][k] * markov_matrix2[k][j])
    return new_matrix

#Function to compute matrix powers
def powerOfMatrix(markov_matrix, power):
    original_matrix = markov_matrix
    for i in range(2, power):
        print i
        markov_matrix = multiplyMatrices(markov_matrix, original_matrix)
    return markov_matrix