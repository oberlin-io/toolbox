import pandas as pd
import numpy as np
import json

class Columns():
    def __init__(self):
        self.cols = [
            'column',
            'dtype',
            'mean',
            'mode',
            'median',
            'stdev',
            'min',
            'max',
        ]

class Explore():
    def __init__(self, df):
        self.df = pd.DataFrame(columns = Columns().cols)    
        for col in df.columns(): ### !!! issue
            self.df.append(Feature(col, df))

class Feature():
    def __init__(self, name, df):
        self.series = df[name]
        
       # self.name = name
       # self.dtype = self.series.dtype
       # self.min = self.series.min()
       # self.max = self.series.max()
       # self.mean = self.series.mean()
       # self.median = self.series.median()
       # self.mode = self.series.mode()[0]
       # self.std = self.series.std()
        
        stats = [
            name,
            self.series.dtype,
            self.series.min(),
            self.series.max(),
            self.series.mean(),
            self.series.median(),
            self.series.mode()[0],
            self.series.std(),
        ]
        
        return(pd.DataFrame(stats, Columns().cols))
    
print(Explore(pd.read_csv('data.csv')).df.head())

"""
class Feature(object):

    def __init__(self, name, df):
        self.series = df[name]

        self.name = name
        #self.df = df
        self.dtype = self.series.dtype

        self.mode = self.series.mode()[0]
        
        '''
        if self.dtype == 'object':
            self.mean = np.isnan()
            self.median = np.isnan()
            self.std = np.isnan()
        else:
        ''' 
        self.mean = self.series.mean()
        self.median = self.series.median()
        self.std = self.series.std()
        self.min = self.series.min()
        self.max = self.series.max()

    def get_stats(self, out, rnd):
        if out == 'csv':
            csv = '{},{},{},{},{},{},{},{}\n'.format(
                                self.name,
                                self.dtype,
                                round(self.mean, rnd),
                                self.mode,
                                round(self.median, rnd),
                                round(self.std, rnd),
                                self.min,
                                self.max,
            )
            return(csv)

        elif out == 'json':
            stats = {}
            stats['mean'] = round(self.mean, rnd)
            stats['mode'] = self.mode
            stats['median'] = round(self.median, rnd)
            stats['std'] = round(self.std, rnd)
            stats['min'] = self.min
            stats['max'] = self.max
            return(stats)
            #return(json.dumps(stats, sort_keys=True, indent=2))
        else:
            return('Error')
    
class Field(object):
    pass

# test
df = pd.read_csv('data.csv')

shots = Feature('Shots', df)

#print(shots.get_stats(out='csv', rnd=2))
#print(shots.std)




"""


