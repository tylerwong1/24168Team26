from mmap import ALLOCATIONGRANULARITY
from sys import getsizeof
from numpy import allclose
from .course import *
import csv
import os

allAreas = {}
allClasses = {}
topAreas = []
topSubs = {}
numbering = {}

def reading():
    file = open('website/areas.csv')

    csvreader = csv.reader(file)

    header = next(csvreader)

    rows = []
    for row in csvreader:
        rows.append(row)

    file.close()

    for i in rows:
        if i[0] not in allAreas:
            a1 = Area(i[0])
            allAreas[i[0]] = a1
        a1.topics(i[1])
        for j in range(2,len(i)):
            a1.t[i[1]].courses(i[j])
            if i[j] not in allClasses:
                c1 = Course(i[j])
                allClasses[i[j]] = c1

    file = open("website\courses.csv")

    csvreader = csv.reader(file)

    header = next(csvreader)

    rows = []
    for row in csvreader:
        rows.append(row)

    file.close()

    for i in rows:
        for j in range(1,len(i)):
            allAreas[i[0]].courses(i[j])

def values1(values):
    reading()
    for key, value in allAreas.items():
        value.updateIndex(int(values[key]))
        for c in value.c:
            allClasses[c].updateIndex(int(values[key]) - 3)


def topS():
    for key, value in allAreas.items():
        for c in value.c:
            allClasses[c].updateIndex(0.25)
        if value.index == 5 or value.index == 4:
            topAreas.append(key)
    
    count = 0
    for a in topAreas:
        for key, value in allAreas[a].t.items():
            count = count + 1
            topSubs[str(count)] = key

    return topSubs

def q2(input):
     for a in topAreas:
        for key, value in allAreas[a].t.items():
            value.updateIndex(input[key])

def q3():
    countS = 0
    for a in topAreas:
        for key, value in allAreas[a].t.items():
            if value.index == 'y':
                countS = countS + 1
                numbering[str(countS)] = key
    return numbering


def finalR(numbering, ranking, total):           
    for a in topAreas:
        for key, value in allAreas[a].t.items():
            if numbering[ranking] == key:
                for c in value.c:
                    allClasses[c].updateIndex(total)

def topC():
    topCourses = {}
    top = {}
    for key, value in allClasses.items():
        topCourses[value.index] = key

    topL = list(topCourses.items())
    topL.sort(reverse=True)
    top5 = topL[0:5]

    count = 0
    for t in top5:
        count = count + 1
        top[str(count)] = t[1]
    
    return top