import pandas as pd
import numpy as np
import json

class conf(object):
    def __init__(self):
        self.conf = yaml.safe_load('conf.yaml')

class dropped(object):
    ''' Creates an array of dictionaries, written as JSON to directory, of dropped
            data. Each dict an instance of a dropped dataframe.
        catch(): Appends a dropped dataframe to the object. May do this at various
            points throughout processing.
        write(): Writes dropped data out to JSON file. Probably use this once,
            at the end of processing.
    '''


    def __init__(self, fresh=True):
        ''' Initiate the dropped obj
            fresh: wipes existing dropped.json in dir, default True '''

        if fresh == True:
            self.dropped = []
            with open('dropped.json', 'w') as f:
                f.write('')
        elif fresh == False:
            with open('dropped.json', 'r') as f:
                self.dropped = json.load(f) or {}
        else: print('Error: variable fresh must be True|False')


    def catch(self, df_dropped):
        ''' Appends dropped dataframe
            df_dropped: dataframe that was dropped
            To do: Ideally this would happen with df.drop() being called '''

        j = df_dropped.to_json(index=True)
        self.dropped.append(j)


    def write(self):
        ''' Write out dropped object. '''

        with open('dropped.json', 'w') as f:
            json.dump(self.dropped, f, indent=4)



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


"""
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
"""

# Testing
testing=False
if testing:
    df = pd.read_csv('test_sets/iris.csv')





