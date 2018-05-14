import numpy as np
import time
# import numba
# @numba.jit

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return a * b // gcd(a, b)

def qotient(a, b):
    g = gcd(a,b)
    if(g == 0):
        return [0,1]
    else:
        return [a//g, b//g]

def qotient_vector_teisubai(c, vector):
    result = np.empty((vector.size,2))
    for i in range(vector.size):
        g = gcd(vector[i], c)
        result[i] = [vector[i]//g, c//g]
    return result

def qotient_subtraction(a, b):
    return qotient(a[0]*b[1]-a[1]*b[0],a[1]*b[1])

def qotient_subt_vector(vector1, vector2):
    vector = np.zeros(vector1.shape)
    for i in range (vector1.shape[0]):
        vector[i] = qotient_subtraction(vector1[i],vector2[i])
    return vector

def qotient_sum(a,b):
    return qotient(a[0]*b[1]+a[1]*b[0],a[1]*b[1])

def inner(vector1,vector2):
    vector = vector1 * vector2
    norm = np.array([0,1])
    for i in range(vector.shape[0]):
        norm = qotient_sum(vector[i],norm)
    return norm

def gram_schmidt_qotient(vectors):
    # 係数(v_primeのノルムの二乗)を格納
    keisu = np.zeros((len(vectors), 2))
    irekae = np.array([[0, 1], [1, 0]])
    for i in range(len(vectors)):
        if (i > 1):
            vectors[i - 1] = vectors[i]
            for j in range(i - 1):
                vectors[i - 1] = qotient_subt_vector(vectors[i - 1],np.dot(keisu[j], irekae) * inner(vectors[i], vectors[j]) * vectors[j])
                keisu[i - 1] = inner(vectors[i - 1], vectors[i - 1])
        # i=0のとき
        elif (i == 0):
            keisu[i] = inner(vectors[i], vectors[i])
    return vectors
