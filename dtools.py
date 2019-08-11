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

def explore(filen):
    '''
    writes various data overview csvs
    filen:  eg, 'data.csv
    '''
    # read in
    df = pd.read_csv(filen)
    columns = df.columns
    
    explore = {
                'column': [],
                'datatype': [],
                'notnan': [],
                'isnan': [],
                'unique': [],
                'mean': [],
                'mode[0]': [],
                'median': [],
                'stdev': [],
              } 

    # basic info
    for col in df.columns:
        explore['column'].append(col)
        explore['datatype'].append(df[col].dtype)
        explore['notnan'].append(df[col].count())
        explore['isnan'].append(df[col].isna().sum())
        explore['unique'].append(df[col].nunique())

        # stats for non-objects (non-str)
        if df[col].dtype != 'object':
            explore['mean'].append(df[col].mean().round(decimals=2))
            explore['mode[0]'].append(df[col].mode()[0].round(decimals=2)) # mode returns a list of values (two values could occur equally most)
            explore['median'].append(df[col].median().round(decimals=2))
            explore['stdev'].append(df[col].std().round(decimals=2))

        # stats=None for objects, except for mode. break out categorical data into new csvs?
        else:
            explore['mean'].append(None)
            explore['mode[0]'].append(df[col].mode()[0]) # mode returns a list of values (two values could occur equally most)
            explore['median'].append(None)
            explore['stdev'].append(None)
    
    df_explore = pd.DataFrame(data=explore)
    df_explore.to_csv('explore.csv', index=False)
    #return(df_explore)

explore('data.csv')




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


