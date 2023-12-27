#!/usr/bin/python3

import sys
from os import listdir
import numpy as np
import operator

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}

    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]] 
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    
    sortedClassCount = sorted(classCount.items(), key= operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def getVectorData(file):
    v = np.zeros((1, 1024))
    with open(file) as f:
        for i in range(32):
            l = f.readline()
            for j in range(32):
                v[0, 32 * i + j] = int(l[j])
        return v

def createDataSet(dirname):
    labels = []
    trainingFileList = listdir(dirname)
    m = len(trainingFileList)
    matrix = np.zeros((m, 1024))

    for i in range(m):
        fileName = trainingFileList[i]
        result = int(fileName.split('_')[0])
        labels.append(result)
        matrix[i, :] = getVectorData(dirname + '/' + fileName)
    return matrix, labels

trainingFile = sys.argv[1]
testFile = sys.argv[2]

testFileList = listdir(testFile)
length = len(testFileList)

matrix, labels = createDataSet(trainingFile)

for k in range(1, 21): 
    count = 0 
    error = 0 
                
    for i in range(length):
        temp = int(testFileList[i].split('_')[0])
        testData = getVectorData(testFile + '/' + testFileList[i])
        result = classify0(testData, matrix, labels, k)
                                                        
        count += 1
        if temp != result:
            error += 1
    print(int(error / count * 100))
