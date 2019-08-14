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


