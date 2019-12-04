'''
Topic
    Stacks
    Src
'''

class Topic(object):
        
    def __init__():

        # matrices
        import pandas as pd
        import numpy as np
        import itertools

        # viz
        from matplotlib import pyplot as plt
        import seaborn as sns

        # prep, eng
        from sklearn.model_selection import train_test_split
        from sklearn.feature_extraction.text import CountVectorizer

        # models
        from sklearn.linear_model import LogisticRegression
        from sklearn.svm import SVC
        from sklearn.ensemble import RandomForestClassifier as rfc

        # metrics
        from sklearn.metrics import roc_curve
        from sklearn.metrics import auc
        from sklearn.metrics import accuracy_score
        from sklearn.metrics import confusion_matrix


class README(self):

    def __init__(self):
        self.readme = {}


class Stacks(Topic):

    def __init__(self):
        # Feature: coolout grabs DB in cloud
        self.coolout = [
            '''<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/190477381&color=%23bcbcac&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>''',
            '''<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/274404811&color=%23bcbcac&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>''',
            '''<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/575603208&color=%23bcbcac&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>''',

        ]

    def serve_up(self):
        html = list[]
        for i in self.coolout: html.append(i)
        self.html = '\n'.join(html)
        
        with open('stacks.html', 'w') as f: f.write(self.html)


class Src(Topic):

    def __init__(self):
        pass
