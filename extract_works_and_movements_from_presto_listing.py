# coding: utf-8
get_ipython().run_line_magic('load', 'tagging.py')
# %load tagging.py
from pathlib import Path
from mutagen.mp4 import MP4

def get_audio_files(parent=Path.cwd()):
    return [p for p in parent.iterdir() if p.suffix == '.m4a']
    
def get_tags(audio_file):
    match audio_file:
        case MP4() as tag:
            return tag
        case Path() as p:
            return get_tags(MP4(p))
        case str() as s:
            return get_tags(MP4(s))
        case _:
            raise TypeError(f"Cannot get tags for instances of type {audio_file.__class__}.")
            
def get_tag_keys(audio_file):
    return get_tags(audio_file).keys()

def print_tags(tags):
    
    for key, value in tags:
        print(key, end=' ')
        while True:
            match input('Print value? [Y/n] ').lower().strip():
                case 'n':
                    break
                case 'y'| '':
                    print(f'    {value}')
                    break
                case _:
                    print('Invalid response')
                    continue
    
files = get_audio_files()
tags = get_tags(files[0])
print_tag_keys(files[0])
get_ipython().run_line_magic('whos', '')
print_tags(files[1])
print_tag_keys(tags)
print_tags(tags)
get_ipython().run_line_magic('whos', '')
import inspect
inspect.getsource(print_tags)
print(inspect.getsource(print_tags))
get_ipython().run_line_magic('whos', '')
all_tags = [MP4(file) for file in files]
print_tags(all_tags[23])
tags
get_ipython().run_line_magic('history', '-n ')
tags = get_tags(files[1])
print_tag_keys(files[1])
print_tags(files[1])
MP4(files[1])
all_tags[0]
all_tags[1]
all_tags[2]
[(key, val) for key, val in all_tags[2].items() if key != 'covr']
get_ipython().run_line_magic('pip', 'install requests')
import requests
r = requests.get('https://www.prestomusic.com/classical/products/7936240--mahler-complete-symphonies')
dir(r)
r.text
import lxml
get_ipython().run_line_magic('pip', 'install lxml')
from bs4 import BeautifulSoup
import lxml.html as html
dir(html)
doc = html.fromstring(r.text)
doc
dir(doc)
with open('chaiily_mahler.html', mode='w', encoding='utf-8') as fp:
    fp.write(r.text)
    
get_ipython().system('tidy --write-back no --indent yes --indent-spaces 4 --input-html yes --output-xml yes --output-file chailly_mahler.xml chaiily_mahler.html')
doc.findall('p[@class="c-track__title"]')
doc.findall('.//p[@class="c-track__title"]')
track_titles = doc.findall('.//p[@class="c-track__title"]')
dir(doc)
dir(track_titles[0])
tt = track_titles[0]
tt.text
tt.text_content
tt.text_content()
len(track_titles)
import shutil
shutil.get_terminal_size()
for tt in track_titles[:25]:
    print(tt.text.strip())
    
for tt in track_titles[25:50]:
    print(tt.text.strip())
    
for tt in track_titles[50:75]:
    print(tt.text.strip())
    
track_titles_texts = [tt.text for t in track_titles]
track_titles_texts = [(i, tt.text) for i, t in enumerate(track_titles)]
track_titles_texts = [(tt.text, i) for i, t in enumerate(track_titles)]
track_titles_texts[:25]
track_titles
[tt.text for tt in track_titles]
titles = [(tt.text.strip(), i) for i, tt in enumerate(track_titles)]
titles
works = [(t, idx) for t in titles if t.startswith('Mahler')]
works = [(t, idx) for t, idx in titles if t.startswith('Mahler')]
works
from itertools import pairwise
paired_works = list(pairwise(works))
paired_works
track_per_work  = [(title,slice(i+1, j)) for (title, i), (_, j) in paired_works] 
track_per_work
track_titles
get_ipython().run_line_magic('whos', '')
track_titles_texts[:10]
track_titles[:10]
titles[:10]
tracks_per_work = track_per_work
del track_per_work
works_movements = {title:titles[track_range] for title, track_range in tracks_per_work}
works_movements
works_movements = {title:[t for t, _ in titles[track_range]] for title, track_range in tracks_per_work}
works_movements
import json
with open('mahler_symphonies.json', mode='w') as fp:
    json.dump(works_movements, fp, indent=True)
    
get_ipython().run_line_magic('whos', '')
track_titles_texts[:5]
get_ipython().run_line_magic('rm', 'track_titles_texts')
del track_titles_texts
titles[-5:]
titles[-6]
works_movements[titles[-6][0]] = [t for t, _ in titles[-5:]]
works_movements
with open('mahler_symphonies.json', mode='w') as fp:
    json.dump(works_movements, fp, indent=True)
    
