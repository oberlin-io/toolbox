'''
QUALITY Check
Functions to Quality Check a Dataset
John Oberlin

Function defitions should follow a generic business logic for the dataset.
Functions write out Markdown syntax and HTML tables for incorporation into
a Markdown.md file.

Namespace terminology with regard to the dataset:
  dataframe: or df, the single sheet of rows and columns of the dataset
    feature: a column, ie variable
observation: a row
      entry: string or number at an observation-feature intersection, ie cell
      class: one of two or more types of entries (string or integer)
      value: a number entry
   instance: an occurence of an observation with a particular class or value

+---------------------------------------+
| Dataframe                             |
|               | Feature 1 | Feature 2 |
| Observation 1 | Class A   | Value x   |
| Observation 2 | Class B   | Value y   |
+---------------------------------------+

+----------------------------------+
| employees.csv                    |
|            | Level      | Salary |
| Employee 1 | Manager    | 100000 |
| Employee 2 | Specialist |  80000 |
+----------------------------------+

Pseudo Code

QC function (df, features, business logic):
    run check based on generic business logic; return valid|invalid
    if valid
        check box = '- [x] valid\n- [ ] invalid'
        md = '{}\n{}\n{}'.format(business logic, check box, sample cases)
    if invalid
        check box = '- [ ] valid\n- [x] invalid'
        md = '{}\n{}\n{}'.format(business logic, check box, cases)
    Append to .md file function (md)

'''

import pandas as pd
from datetime import datetime

testing = False

class report(object):
    def __init__(self, df, title='Report'):
        self.df = df
        self.title = title
        self.md = '# {}\n'.format(self.title)


    def append_md(self, content, type='string', index=True):
        '''
        Append a dataframe or string content to the Markdown file.
        '''
        if type == 'df':
            html_table = content.to_html(index=index)
            remove = ['\n', ' '*6]
            for i in remove: html_table = html_table.replace(i,'')
            content = html_table + '\n'

        elif type == 'string':
            pass

        self.md += '{}\n'.format(content)


    def write_md(self):
        now = datetime.now()
        #datetime_ = now.strftime("%Y-%m-%d_%H-%M")
        #file_name = '{}_{}.md'.format(self.title, datetime_)
        file_name = '{}.md'.format(self.title) # Datetime off for testing
        path = '/mnt/c/Users/joberlin/Documents/'
        with open(path+file_name, 'w') as f: f.write(self.md)


    def valid_text(self, check):
        '''
        Proide validation check notice via Markdown checkboxes.
        check: True|False
        '''
        if check: checkboxes = '- [x] valid\n- [ ] invalid'
        else: checkboxes = '- [ ] valid\n- [x] invalid'
        return(checkboxes)


    def get_dataframe(self):
        observations = self.df.shape[0]
        if observations > 10:
            sample = True
            df1 = self.df.sample(n=10)
        else:
            sample = False
            df1 = self.df

        section = '## The Data\n'
        if sample:
            section += '*Sample from {} observations*\n'.format(str(observations))

        self.append_md(section)
        self.append_md(df1, type='df', index=False)


    def feature_overview(self):
        '''
        Provide a an overview of all of the features of the dataset.
        '''
        counts = pd.DataFrame(self.df.count(), columns=['count'])
        uniques = pd.DataFrame(self.df.nunique(), columns=['unique'])
        nans = pd.DataFrame(self.df.isna().sum(), columns=['null'])
        datatypes = pd.DataFrame(self.df.dtypes, columns=['data type'])

        overview = counts.join(uniques).join(nans).join(datatypes)

        section = '## Feature Overview'

        self.append_md(section, type='string')
        self.append_md(overview, type='df', index=True)


    def class_feature_consistency(self, identity, class_feature, class_, features, rule):
        '''
        Business logic: All observations of the same class of feature A have
        the same entry for features B, C, etc.

        identity: feature that identifies the observation uniquely
        class_feature: string of feature name A
        class_: sring of class name of feature A
        features: array of feature names B, C, etc.
        '''
        subset = features.copy()
        subset.insert(0, class_feature)

        reduce_to = subset.copy()
        reduce_to.insert(0, identity)
        df1 = df[reduce_to] # Reduce
        df1 = df1[df1[class_feature]==class_] # Filter
        df1 = df1.drop_duplicates(subset=subset) # Dedupe

        observations = df1.shape[0]
        if observations == 1: # Each feature's entries the same
            check = True
            index = False
            df1 = df1.drop(columns='identity')

        if observations > 1: # At least one entry of a feature is different
            check = False
            if observations > 10: # To limit Markdown size
                sample = True
                df1 = df1.sample(n=10)
            else: sample = False

        checkboxes = self.valid_text(check)

        features_text = ''
        for f in features: features_text += '- {}\n'.format(f)
        features_text = 'Class feature: {}\n\nClass: {}\n\nFeatures checked \
        for consistency:\n{}\n'.format(class_feature, class_, features_text)

        section = '## {}\n{}\n\n{}\n\n'.format(rule, checkboxes, features_text)

        if sample:
            section += '*Sample from {} observations*\n'.format(str(observations))

        self.append_md(section)
        self.append_md(df1, type='df', index=False)



if testing:
    df = pd.read_csv('/test_sets/qc_test.csv')
    md = report(df)
    md.get_dataframe()
    md.feature_overview()
    md.class_feature_consistency('name', 'level', 'A', ['income', 'fav_color'],
                                'All observations that have level=A should \
                                have the same income and favorite color.')
    md.write_md()
