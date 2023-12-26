#!/usr/bin/python3

import sys
import numpy as np
import operator
from os import listdir


trainingFile = sys.argv[1]
testFile = sys.argv[2]


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
	sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]


def CreateDataSet(dirname):
	labels = []
	trainingList = listdir(dirname)
	num = len(trainingList)
	matrix = np.zeros((num, 1024))

	for i in range(num):
		fn = trainingList[i]
		answer = int(fn.split('_')[0])
		labels.append(answer)
		matrix[i, :] = getArray(dirname + '/' + fn)
	return matrix, labels


def getArray(filename):
	result = np.zeros((1, 1024))
	with open(filename) as fp:
		for i in range(32):
			line = fp.readline()
			for j in range(32):
				result[0, 32 * i + j] = int(line[j])
		return result




testList = listdir(testFile)
length = len(testList)
matrix, labels = CreateDataSet(trainingFile)

for k in range (1, 21):
	all = 0
	errorCount = 0

	for i in range(length):
		all += 1
		answer = int(testList[i].split('_')[0])
		testData = getArray(testFile + '/' + testList[i])
		result = classify0(testData, matrix, labels, k)
		
		if answer != result :
			errorCount += 1

	errorRate = int(errorCount / all * 100)	
	print(errorRate)