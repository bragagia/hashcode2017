import sys;

V = -1
R = -1
X = -1
E = -1
C = -1

def get_videos():
    tmp = File[1]
    tab = tmp.split(" ")
    videos = []
    id = 0
    for size in tab:
        videos.append(VideoClass(id, size, 0))
        id += 1
        print(videos)


class VideoClass(object):
    id = 0
    size = 0;
    req_by_end = 0;
    """docstring for VideoClass."""
    def __init__(self, id, size, req):
        super(VideoClass, self).__init__()
        self.id = id
        self.size = size
        self.req_by_end = req


def getInfo():
    tmp = File[0]
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
    getInfo(File)
    get_videos(File)
