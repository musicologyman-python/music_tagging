import json
with open('mahler_symphonies.json') as fp:
    d = json.load(fp)
    

with open('mahler_symphonies_2.json', mode='w', encoding='utf-8') as fp:
    json.dump(d, fp, indent=4)
    
