from mmap import ALLOCATIONGRANULARITY
from numpy import allclose
import matching
import csv

file = open("areas.csv")

csvreader = csv.reader(file)

header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)

file.close()

allAreas = {}
allClasses = {}

for i in rows:
    if i[0] not in allAreas:
        a1 = matching.Area(i[0])
        allAreas[i[0]] = a1
    a1.topics(i[1])
    for j in range(2,len(i)):
        a1.t[i[1]].courses(i[j])
        if i[j] not in allClasses:
            c1 = matching.Course(i[j])
            allClasses[i[j]] = c1

file = open("courses.csv")

csvreader = csv.reader(file)

header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)

file.close()

for i in rows:
    for j in range(1,len(i)):
        allAreas[i[0]].courses(i[j])

for key, value in allAreas.items():
    print()
    print(key)
    rate = input("Rate 1-5 ")
    allAreas[key].updateIndex(int(rate))
    for c in value.c:
        allClasses[c].updateIndex(int(rate) - 3)

topAreas = []
for key, value in allAreas.items():
    for c in value.c:
        allClasses[c].updateIndex(0.25)
    if value.index == 5 or value.index == 4:
        topAreas.append(key)

for a in topAreas:
    for key, value in allAreas[a].t.items():
        print()
        print(key)
        res = input("Are you interested in this topic? ")
        value.updateIndex(res)

count = 0
numbering = {}
for a in topAreas:
    for key, value in allAreas[a].t.items():
        if value.index == 'y':
            count += 1
            numbering[count] = value
            print(count, " ", key)

ranking = input("Rank the topics ")
total = count * .2
for r in ranking:
    total -= 0.2
    for c in numbering[int(r)].c:
        allClasses[c].updateIndex(count)

topCourses = {}
for key, value in allClasses.items():
    topCourses[value.index] = key

topL = list(topCourses.items())
topL.sort(reverse=True)
top5 = topL[0:5]
for t in top5:
    print(t[1])

        
    




