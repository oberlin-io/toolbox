import pandas as pd
import numpy as np




def mkdropped():
    '''
    write initial dropped.json as a dropped data archive
    overwrites any existing dropped.json, so use only initially
    '''
    with open('dropped.json', 'w') as f:
        #yeswrite = input('overwrite existing dropped.json? y/n')
        #if yeswrite = 'y':
        f.write('{\n')

def capdropped():
    '''
    cap off dropped.json to make json valid
    use after data cleaning and transformation
    '''
    with open('dropped.json', 'r') as f:
        dropped = f.read()
        capdropped = dropped[:-2] + '\n}\n'
    with open('dropped.json', 'w') as f:
        f.write(capdropped)
        print('dropped.json finalized\n')


def testout(df, kind, max_rows):
    '''
    test output quickly by refreshing web browser tab
    or write out to csv
    df:         dataframe object
    kind:       'web'|'csv'
    max_rows:   int or None, for web only, ie max_rows=1000
    '''
    if kind == 'web':
        df.to_html('testout.html', border=0, max_rows=max_rows)
        print('open testout.html in browser\n')
    elif kind == 'csv':
        df.to_csv('testout.csv')
        print('testout.csv written\n')
    else:
        print("argument 'kind' must be 'web' or 'csv'\n")


def add_row(df):
    '''
    Append row to a Pandas dataframe, with same columns,
    ignoring new row index. Returns new dataframe.
    
    df: dataframe with column names
    '''
    
    new_entry = {}
    for c in df.columns:
        new_entry[c] = [input('{} ({}): '.format(c, df[c].dtype))]

    df_entry = pd.DataFrame(new_entry)

    return(df.append(df_entry, ignore_index=True))


test=False
if test:
    df = pd.read_csv('test_sets/iris.csv')
    add_row(df)

# bqtools > make json schema for google Big Query
python3 -c "from bqtools import schema; schema('feature_1,feature_2', 'f1_dtype,f2_dtype')"
import json

class schema(object):
    def __init__(self, features, dtypes):
        '''
        features:   one-line csv string
        dtypes:     one-line csv string
        '''
        features = features.split(',')
        dtypes = dtypes.split(',')
        if len(features) == len(dtypes):
            schema = []
            for i in range(len(features)):
                featobj = {}
                featobj['name'] = features[i]
                featobj['type'] = dtypes[i]
                schema.append(featobj)
            print(schema)
            with open('schema.json', 'w') as f:
                json.dump(schema, f, indent=2)
        else:
            print('ERROR: features and dtypes lengths are unequal')
