import sys
from endpoint import *

V = -1
R = -1
X = -1
E = -1
C = -1

def getInfo(File):
    for i in File:
        tmp = i
        tab = tmp.split(" ");
        V = tab[0]
        E = tab[1]
        R = tab[2]
        C = tab[3]
        X = tab[4]
        break

if len(sys.argv) <= 1:
    exit(42)
else:
    File = open(sys.argv[1], 'r');
    getInfo(File)
    getEndPoint(File)
