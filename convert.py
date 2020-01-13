'''
Convert Yelp Academic Dataset from JSON to CSV

Requires Pandas (https://pypi.python.org/pypi/pandas)

By Paul Butler, No Rights Reserved
'''

import json
import pandas as pd
from glob import glob

def convert(x):
    ''' Convert a json string to a flat python dictionary
    which can be passed into Pandas. '''
    ob = json.loads(x)
    for k in list(ob):
        v = ob[k]
        if isinstance(v, list):
            ob[k] = ','.join(v)
        elif isinstance(v, dict):
            for kk, vv in v.items():
                ob['%s_%s' % (k, kk)] = vv
            del ob[k]
    return ob

for json_filename in glob('*.json'):
    csv_filename = '%s.csv' % json_filename[:-len('.json')]
    print('Converting ' + json_filename  + ' to ' + csv_filename)
    res=[]
    with open(json_filename) as fp:
        line = fp.readline()
        while line:
            res.append(convert(line))
            line = fp.readline()
    df = pd.DataFrame(res)
    df.to_csv(csv_filename, encoding='utf-8', index=False)
