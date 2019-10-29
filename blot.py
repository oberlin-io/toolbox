import pandas as pd
import numpy as np

class blot(object):
    def __init__(self,width=80):
        '''
        width: width in characters of complete plot space
        '''
        self.plot_spc=''
        self.width=width

    def bar(self,df,feature,labels,char='█',label_spc=12):
        '''
        df: pandas dataframe
        feature: name of feature to plot
        labels: name of feature from which to get labels
        char: character to comprise bars
        '''
        # Set up labels
        labels=df[labels]
        labels_with_pad=[]
        for label in labels:
            if isinstance(label,float):
                label=str(round(label,3))
            if isinstance(label,int):
                label=str(label)
            label_len=len(label)
            if label_len<=label_spc:
                pad=' '*(label_spc-label_len)
                labels_with_pad.append('{}{} '.format(pad,label))
            else:
                labels_with_pad.append('{}{} '.format(label[:label_spc-2], '..'))
        # Scale values
        values=df[feature]
        scale=values.max()/(self.width-label_spc-1) # -1 for space between label and bar
        values_scaled=[]
        for v in values:
            values_scaled.append(int(round(v/scale,0)))
        # Draw bars
        for i in range(len(values)):
            label_=labels_with_pad[i]
            bar=char*values_scaled[i]
            val=values[i]
            self.plot_spc+='{}{}{}\n'.format(label_,bar,val)
        return(self.plot_spc)

test=False
if test:
    df=pd.read_csv('toolbox/test_sets/satellite.csv')
    agg=df[['planet','satelite']].groupby('planet').count()
    agg['planet']=agg.index
    agg=agg.append(pd.DataFrame({'planet':'George Blankenhorn','satelite':40},index=['GB']))
    agg=agg.sort_values(by='satelite')
    blt=blot()
    print(blt.bar(agg,'satelite','planet'))


        
