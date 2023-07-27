# coding: utf-8
import json
from yaml import load, dump
with open('mahler_symphonies.json', encoding='utf-8') as fp:
    d = json.load(fp)
    
with open('mahler_symphonies.json', encoding='utf-8', mode='w') as fp:
    json.dump(d, fp, indent=2)
    
with open('mahler_symphonies.yaml', mode='w', encoding='utf-8') as fp:
    dump(d, fp)
    
