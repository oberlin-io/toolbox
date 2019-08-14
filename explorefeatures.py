import pandas as pd

class Columns():
    def __init__(self):
        self.cols = [
            'column',
            'dtype',
            'nonnan',
            'nan',
            'unique',
            'min',
            'max',
            'mean',
            'median',
            'mode',
            'stdev',
        ]

class Feature():
    def __init__(self, feature, df):
        self.series = df[feature]
        if self.series.dtype != 'object': # add: other datatypes, eg date
            stats = [
                feature,
                self.series.dtype,
                self.series.count(),
                self.series.isna().sum(),
                self.series.nunique(),
                self.series.min(),
                self.series.max(),
                self.series.mean().round(decimals=2),
                self.series.median().round(decimals=2),
                self.series.mode()[0],
                self.series.std().round(decimals=2),
            ]
        else:
            stats = [
                feature,
                self.series.dtype,
                self.series.count(),
                self.series.isna().sum(),
                self.series.nunique(),
                None,
                None,
                None,
                None,
                self.series.mode()[0],
                None,
            ]
        #stats = []       
        self.stats_df = pd.DataFrame([stats], columns=Columns().cols)

class Explore():
    def __init__(self):
        self.df = pd.DataFrame(columns = Columns().cols)    

    def set_feats(self, df):
        #self.df.append([['a','b','c','d','e','f','g','h']], Columns().cols)
        for col in df.columns:
            f = Feature(col, df)
            self.df = self.df.append(f.stats_df)
            #self.df.append(['a','b','c','d','e','f','g','h'], Columns().cols)
            #Feature(col, df)

    #def get_expdf(self):
        #return(self.df)

if __name__ == '__main__':
    
    filen = input('csv dataset name: ')
    df = pd.read_csv(filen)

    exp_df = Explore()
    exp_df.set_feats(df)
    exp_df.df.to_csv(filen[:4]+'features.csv', index=False)

