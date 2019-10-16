import pandas as pd
import numpy as np
import json
import yaml
from random import randint
from time import sleep

class conf(object):
    def __init__(self):
        with open('toolbox/conf.yaml', 'r') as f: c = f.read()
        self.params = yaml.safe_load(c)

class html(object):
    """ Run any content through to write out an HTML page  """
    def __init__(self, content, title=None, refresh=None, file_path='/mnt/c/Users/joberlin/Documents/html.html'):
        """
        content: whatever string or df.to_html()
        title: string or default None
        refresh: an integer to auto refresh by, default None
        file_path: file name and optionally with path
        """
        from bs4 import BeautifulSoup as bs

        if title == None:
            title_meta = ''
            title_h1 = ''
        else:
            title_meta = '<title>{}</title>'.format(title)
            title_h1 = '<h1>{}</h1>'.format(title)

        if refresh == None:
            refresh = ''
        else: refresh = "<meta http-equiv='refresh' content='{}'>".format(int(refresh))

        style = "<style>body {background-color: white; color: black; \
                font-family: monospace;} .dataframe {border-collapse: collapse; border: 1px solid black; \
                /*width: 90%;*/} .dataframe.th {text-align: left;}</style>"

        html = "<!DOCTYPE html><html><head><meta charset='UTF-8'>{}{}{} \
                </head><body>{}{}</body></html>\n" \
                .format(refresh, title_meta, style, title_h1, content)
        
        html = bs(html, 'lxml').prettify()

        with open(file_path, 'w') as f:
            f.write(html)


class ref(object):
    ''' Get items from ref.txt while coding in Python in terminal '''
    def __init__(self):
        self.entries = []
        with open('{}ref.txt'.format(conf().params['path_to_toolbox']), 'r') as f: txt = f.read()
        for entry in txt.split('###'):
            self.entries.append(entry)
    def find(self, string):
        results = ''
        for entry in self.entries:
            if string in entry:
                results += entry
        print(results)

    def add(self, ref_, code):
        with open('{}ref.txt'.format(conf().params['path_to_toolbox']), 'a') as f:
            f.write('{}\n{}\n###\n'.format(ref_, code))
        # Update ref object with new entry
        self.entries = []
        with open('{}ref.txt'.format(conf().params['path_to_toolbox']), 'r') as f: txt = f.read()
        for entry in txt.split('###'):
            self.entries.append(entry)


class dropped(object):
    ''' Creates an array of dictionaries, written as JSON to directory, of dropped
            data. Each dict an instance of a dropped dataframe.
        __init__(): wipes existing dropped.json in dir by default
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
            df_dropped: dataframe that was dropped '''

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



class schema(object):
    ''' bqtools > make json schema for google Big Query '''
    def __init__(self, features, dtypes,):
        '''
        features:   one-line csv string
        dtypes:     one-line csv string
        '''
        '''
        if df:
            for c in df.columns:
                features +=
        '''
        #else:
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

class thumb(object):
    '''Thumb through random observations of a Pandas dataframe'''
    def __init__(self,df,qty=5):
        '''Appends an initial quantity of randome observations.'''
        self.observations=[]
        index_list=df.index
        x_list_len=len(index_list)
        for i in range(qty):
            list_index=randint(0,x_list_len)
            # bug: if df index has been set, then out-of-bounds error
            self.observations.append(df.iloc[index_list[list_index]])

    def through(self):
        '''Thumbs through '''
        for o in self.observations:
            print(o)
            print('===============================================\n')
            sleep(4)



def split_expand_row(df, column, sep=',', keep=False):
    """
    Split the values of a column and expand so the new DataFrame has one split
    value per row. Filters out rows where the column is missing.

    Params
    ------
    df : pandas.DataFrame
        dataframe with the column to split and expand
    column : str
        the column to split and expand
    sep : str
        the string used to split the column's values
    keep : bool
        whether to retain the presplit value as it's own row

    Returns
    -------
    pandas.DataFrame
        Returns a dataframe with the same columns as 'df'.
    """
    indexes, new_values = list(), list()
    df = df.dropna(subset=[column])
    for i, presplit in enumerate(df[column].astype(str)):
        values = presplit.split(sep)
        if keep and len(values) > 1:
            indexes.append(i)
            new_values.append(presplit)
        for value in values:
            indexes.append(i)
            new_values.append(value)
    new_df = df.iloc[indexes, :].copy()
    new_df[column] = new_values
    return new_df

################################################################################
testing=False
if testing == True:
    df=pd.read_csv('test_sets/asa_shooter.csv')
    thumb=thumb(df)
    thumb.through()
