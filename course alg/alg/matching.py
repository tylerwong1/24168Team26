class Area:
    def __init__(self, type):
        self.type = type
        self.t = {}
        self.c = []
        self.index = 0
    def topics(self, name):
        t1 = Topic(name)
        self.t[name] = t1
    def courses(self, cCode):
        self.c.append(cCode)
    def updateIndex(self, index):
        self.index = index

class Topic:
    def __init__(self, type):
        self.type = type
        self.c = []
        self.index = 'n'
    def courses(self, cCode):
        self.c.append(cCode)
    def updateIndex(self, index):
        self.index = index

class Course:
    def __init__(self, cCode):
        self.cCode = cCode
        self.index = 0
    def updateIndex(self, index):
        self.index += index
