import sys;

V = -1
R = -1
X = -1
E = -1
C = -1

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
