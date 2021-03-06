import sys
from endpoint import *

config = {
    'V' : -1,
    'R' : -1,
    'X' : -1,
    'E' : -1,
    'C' : -1
}

class VideoClass(object):
    id = 0
    size = 0
    endpoint = []
    request = []
    """docstring for VideoClass."""
    def __init__(self, id, size):
        super(VideoClass, self).__init__()
        self.id = id
        self.size = size

    def add_req_end(self, end, req):
        self.endpoint.append(end)
        self.request.append(req)

def req_by_endpoint(video, Line):
    for i in range(len(Line) - config["R"], len(Line)):
        tmp = Line[i]
        tmp.split(" ")
        if int(tmp[0]) == int(video.id):
            video.add_req_end(tmp[1], tmp[2])



def get_videos(Line, config):
    tmp = Line[1]
    tab = tmp.split(" ")
    videos = []
    id = 0
    print("V:", config["V"])
    for size in tab:
        video = VideoClass(id, int(size))
        req_by_endpoint(video, Line)
        videos.append(video)
        id += 1
        if id > config["V"]:
            break

def getInfo(Line, config):
    i = Line[0]
    tmp = i
    tab = tmp.split(" ");
    config['V'] = int(tab[0])
    config['E'] = int(tab[1])
    config['R'] = int(tab[2])
    config['C'] = int(tab[3])
    config['X'] = int(tab[4])

if len(sys.argv) <= 1:
    exit(42)
else:
    File = open(sys.argv[1], 'r');
    Line = []
    for i in File:
        Line.append(i)
    getInfo(Line, config)
    get_videos(Line, config)
    endPoints = getEndPoint(Line, config)
