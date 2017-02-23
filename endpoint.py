def getEndPoint(File):
    tab = []
    for i, line in enumerate(File):
        if i > 2:
            break

class EndPoint:
    def __init__(self, id, cache, pingToCache):
        self.id = -1
        self.cache = []
        self.pingToCache = []
