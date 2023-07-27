# coding: utf-8
import json
with open('mahler_symphonies.json', encoding='utf-8') as fp:
    works_and_movements = json.load(fp)
    
from dataclasses import dataclass, field

    
@dataclass
class Work():
    composer: str
    title: str
    movement_number: int
    movement: str
    genres: list[str]
    
works_and_movements = list(works_and_movements.items())
works_and_movements[0]
for work, _ in works_and_movements:
    print(work)
    
works = [for work, _ in works_and_movements]
works = [work for work, _ in works_and_movements]
keys = ['C minor', 'D minor', 'G major', 'C-sharp minor', 'A minor', 'E minor', 'E-flat major', 'D major', 'F-sharp major']
keys.insert('D major', 0)
keys.insert(0, 'D major')
keys
list(zip(works, keys))
works
works_and_movements
d
get_ipython().run_line_magic('history', '-n 1-4')
get_ipython().run_line_magic('rep', '2')
with open('mahler_symphonies.json', encoding='utf-8') as fp:
    works_and_movements = json.load(fp)
    
works_and_movements
keys = list(works_and_movements.keys())
keys
keys[7:8]
keys[7:9]
works_and_movements[keys[8]]
[f'Part II. {incipit}' for incipit in works_and_movements[keys[8]]]
symphony_8_part_ii_movements = [f'Part II. {incipit}' for incipit in works_and_movements[keys[8]]]
symphony_8_part_ii_movements
symphony_8_part_ii_movements[0].replace(':','.')
symphony_8_part_ii_movements[0] = symphony_8_part_ii_movements[0].replace(':','.')
symphony_8_part_ii_movements
symphony_8_part_ii_movements[0].replace('Waldung', '"Waldung').replace('heran', 'heran"')
symphony_8_part_ii_movements[0] = symphony_8_part_ii_movements[0].replace('Waldung', '"Waldung').replace('heran', 'heran"')
symphony_8_part_ii_movements
works_and_movements[keys[7]]
[f'Part I. {incipit}' for in incipt in works_and_movements[7]]
[f'Part I. {incipit}' for incipit in works_and_movements[7]]
[f'Part I. {incipit}' for incipit in works_and_movements[keys[7]]]
symphony_8 = [f'Part I. {incipit}' for incipit in works_and_movements[keys[7]]] + symphony_8_part_ii_movements
symphony_8
[{'order': i, 'incipit': incipit} for i, incipit in enumerate(symphony_8, start=1)]
symphony_8 = [{'order': i, 'incipit': incipit} for i, incipit in enumerate(symphony_8, start=1)]
works_and_movements
works_and_movements['Mahler, Symphony No. 8'] = symphony_8
works_and_movements
works_and_movements[8]
works_and_movements[keys[8]]]
works_and_movements[keys[8]]
keys[8]
del works_and_movements[keys[8]]
del works_and_movements[keys[7]]
works_and_movements
keys
tonalities = ['D c d G c-sharp a e E-flat D f-sharp'].split()
tonalities = 'D c d G c-sharp a e E-flat D f-sharp'.split()
[f'{t} {"major" if t[0].isupper() else "minor"}' for t in tonalities]
[f'{t.upper()} {"major" if t[0].isupper() else "minor"}' for t in tonalities]
[f'{t[0].upper()}{t[1:] if len(t) > 1 else ""} {"major" if t[0].isupper() else "minor"}' for t in tonalities]
tonalities = [f'{t[0].upper()}{t[1:] if len(t) > 1 else ""} {"major" if t[0].isupper() else "minor"}' for t in tonalities]
keys
keys = list(works_and_movements.keys())
keys
keys.sort()
keys
import regex
def get_sort_key(s):
    match regex.search('\d+', s):
        case regex.Match as m():
            return int(m[0])
def get_sort_key(s):
    match regex.search('\d+', s):
        case regex.Match() as m:
            return int(m[0])
            
keys.sort(key=get_sort_key)
keys
list(zip(keys, tonalities))
list(zip(keys, enumerate(tonalities, start=1)))
tonalities[1]
tonalities[1] = tonalities[1] + ' "Resurrection"'
tonalities
get_ipython().run_line_magic('rep', '72')
list(zip(keys, enumerate(tonalities, start=1)))
tonalities[1] = 'C minor ("Resurrection")'
list(zip(keys, enumerate(tonalities, start=1)))
format_string = "Symphony No. {} in {}"
{old_name, format_string.format(new_name) for old_name, new_name in zip(keys, enumerate(tonalities, start=1)))}
{old_name, format_string.format(new_name) for old_name, new_name in zip(keys, enumerate(tonalities, start=1))}
{old_name: format_string.format(new_name) for old_name, new_name in zip(keys, enumerate(tonalities, start=1))}
format_string
format_string = 'Symphony No. {0} in {1}'
{old_name: format_string.format(new_name) for old_name, new_name in zip(keys, enumerate(tonalities, start=1))}
(old_name, new_name for old_name, new_name in zip(keys, enumerate(tonalities, start=1)))
((old_name, new_name) for old_name, new_name in zip(keys, enumerate(tonalities, start=1)))
[(old_name, new_name) for old_name, new_name in zip(keys, enumerate(tonalities, start=1))]
(1, 'D major').format(format_string)
format_string.format(*(1, 'D major'))
get_ipython().run_line_magic('rep', '86')
{old_name: format_string.format(*new_name) for old_name, new_name in zip(keys, enumerate(tonalities, start=1))}
key_mapping = {old_name: format_string.format(*new_name) for old_name, new_name in zip(keys, enumerate(tonalities, start=1))}
for key, value in works_and_movements.items():
    print((key_mapping[key], value))
    
[(key_mapping[key], value) for key, value in works_and_movements.items()]

 
works_and_movements = [(key_mapping[key], value) for key, value in works_and_movements.items()]
get_ipython().run_line_magic('history', '-n 1-10')
get_ipython().run_line_magic('history', '-n 11-20')
get_ipython().run_line_magic('history', '-n 21-30')
get_ipython().run_line_magic('history', '-n 31-40')
get_ipython().run_line_magic('history', '-n 41-50')
get_ipython().run_line_magic('history', '-n 51-60')
get_ipython().run_line_magic('history', '-n 61-70')
get_ipython().run_line_magic('rep', '68')
def get_sort_key(kvp):
    match regex.search('\d+', kvp[0]):
        case regex.Match() as m:
            return int(m[0])
            
sorted(works_and_movements, key=get_work_key)
sorted(works_and_movements, key=get_sort_key)
works_and_movements = {key:value for key, value in sorted(works_and_movements, key=get_sort_key)}
works_and_movements
keys = list(works_and_movements.keys())
keys[1]
works_and_movements[keys[1]]
roman = {f'{i}: s for i, s in enumerate('I II III IV V VI'.split(), start=1)}
roman = {f'{i}': s for i, s in enumerate('I II III IV V VI'.split(), start=1)}
roman
works_and_movements
MVMT_TITLE_RE = regex.compile(r'(?P<mvmt>\d\).\s*(?P<title>.+)')
MVMT_TITLE_RE = regex.compile(r'(?P<mvmt>\d)\.\s*(?P<title>.+)')
works_and_movements[keys[0]]
def extract_mvmt_title(movement_title):
    match MVMT_TITLE_RE.search(movement_title):
        case re.Match() as m:
            return m.groupdict()
        case _:
            return movement_title
            
[extract_mvmt_title(movement_title) for movement_title in works_and_movements[keys[0]]]
def extract_mvmt_title(movement_title):
    match MVMT_TITLE_RE.search(movement_title):
        case regex.Match() as m:
            return m.groupdict()
        case _:
            return movement_title
            
[extract_mvmt_title(movement_title) for movement_title in works_and_movements[keys[0]]]
get_ipython().run_line_magic('rep', '123')
def extract_mvmt_title(movement_title):
    match MVMT_TITLE_RE.search(movement_title):
        case regex.Match() as m:
            return {'\xa9mvi': int(m['mvmt']), '\xa9mvn': m['title']}
        case _:
            return movement_title
            
get_ipython().run_line_magic('rep', '124')
[extract_mvmt_title(movement_title) for movement_title in works_and_movements[keys[0]]]
works_and_movements[keys[0]] = [extract_mvmt_title(movement_title) for movement_title in works_and_movements[keys[0]]]
works_and_movements
get_ipython().run_line_magic('history', '-n 110-120')
get_ipython().run_line_magic('history', '121-130')
get_ipython().run_line_magic('history', '121-130 -n')
for i in [1, 2, 3, 4, 5, 6, 8, 9]:
    print(keys[i])
    
for i in [1, 2, 3, 4, 5, 6, 8, 9]:
    works_and_movements[keys[i]] = [extract_mvmt_title(movement_title) for movement_title in works_and_movements[keys[i]]]
    
works_and_movements
get_ipython().run_line_magic('ls', '*.json')
import json
with open('mahler_symphonies.json', encoding='utf-8') as fp:
    json.dump(works_and_movements, fp, indent=4)
    
with open('mahler_symphonies.json', encoding='utf-8', mode='w') as fp:
    json.dump(works_and_movements, fp, indent=4)
    
