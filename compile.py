import sys, os, subprocess, re, json
from pprint import pprint

os.chdir(os.path.split(os.path.abspath( __file__ ))[0])

def readf(p):
    f = open(p, 'r')
    c = f.read()
    f.close()
    return c

def getpaths():
    paths = os.listdir(".")
    for p in paths:
        try:
            if p.startswith('.'):
                continue
            subpaths = os.listdir(p)
            for sp in subpaths:
                if sp.startswith('.'):
                    continue
                
                sp2 = p + '/' + sp
                yield (sp2, p, sp)
        except Exception:
            pass

allthings = {}

for sp2, p, sp in getpaths():
    selector = p
    identifier = sp.split('.')[0]
    extension = sp.split('.')[1]
    
    k = selector + '/' + identifier
    if k not in allthings:
        allthings[k] = {
            'identifier': identifier,
            'selector': selector,
            'files': [],
        }
    
    if len(sp.split('.')) == 2:
        # json
        allthings[k]['definition'] = json.loads(readf(sp2))
    elif len(sp.split('.')) == 3:
        # file
        allthings[k]['files'].append({
            'extension': extension,
            'template': readf(sp2),
        })
    
    else:
        print "WOULD YOU CARE FOR SOME TEA?"
        continue

open('data.json', 'w').write(json.dumps(allthings) + '\n')
