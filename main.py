import sys
from endpoint import *

config = {
    'V' : -1,
    'R' : -1,
    'X' : -1,
    'E' : -1,
    'C' : -1
}

def getInfo(File, config):
    for i in File:
        tmp = i
        tab = tmp.split(" ");
        config['V'] = int(tab[0])
        config['E'] = int(tab[1])
        config['R'] = int(tab[2])
        config['C'] = int(tab[3])
        config['X'] = int(tab[4])
        break

if len(sys.argv) <= 1:
    exit(42)
else:
    File = open(sys.argv[1], 'r');
    getInfo(File, config)
    endPoints = getEndPoint(File, config)
