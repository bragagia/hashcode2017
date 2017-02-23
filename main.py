import sys
from endpoint import *

V = -1
R = -1
X = -1
E = -1
C = -1

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

    def add_req_end(end, req):
        self.endpoint.append(end)
        self.request.append(req)

def req_by_endpoint(video, Line):
    for i in range(len(Line) - R, len(Line)):
        tmp = Line[i]
        tmp.split(" ")
        if int(tmp[0]) == video.id:
            video.add_req_end(tmp[1], tmp[2])



def get_videos(Line):
    tmp = Line[1]
    tab = tmp.split(" ")
    videos = []
    id = 0
    for size in tab:
        video = VideoClass(id, int(size))
        req_by_endpoint(video, Line)
        videos.append(video)
        print(video.endpoint, ":", video.request)
        id += 1
        if id > V:
            print("fini")
            break

def getInfo(Line):
    tmp = Line[0]
    tab = tmp.split(" ");
    V = tab[0]
    E = tab[1]
    R = tab[2]
    C = tab[3]
    X = tab[4]

if len(sys.argv) <= 1:
    exit(42)
else:
    File = open(sys.argv[1], 'r');
    Line = []
    for i in File:
        Line.append(i)
    getInfo(Line)
    get_videos(Line)
#    getEndPoint(File)
