def getEndPoint(File, config):
    print(config['E'])
    tab = []
    line = []
    for i in File:
        line.append(i)
    i = 2
    for j in range(0, config['E']):
        tab.append(EndPoint(j))
        tmp = line[i].split(" ")
        tab[j].pingToCenter = int(tmp[0])
        tab[j].nb_cache = int(tmp[1])
        for k in range(0, int(tmp[1])):
            tmp2 = line[i].split(" ")
            tab[j].cache.append(int(tmp2[0]))
            tab[j].pingToCache.append(int(tmp2[1]))
            i += 1
        j += 1

class EndPoint:
    def __init__(self, id):
        self.id = id
        self.nb_cache = -1
        self.cache = []
        self.pingToCache = []
        self.pingToCenter = -1;

    def __str__(self):
        return (str(self.id) + " " + str(self.nb_cache) + " " + str(self.cache) + " " + str(self.pingToCache) + " " + str(self.pingToCenter))
