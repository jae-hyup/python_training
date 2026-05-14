import ssl
ssl._create_default_https_context = ssl._create_unverified_context


from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
df = sns.load_dataset('titanic')

df.head()


def transform_who(x):
    if x == 'man':
        return '남자'
    elif x == 'woman':
        return '여자'
    else:
        return '아이'


#df['who'] = df['who'].apply(transform_who)

def transform_fare(x):
    return x['fare'] / x['age']

df['who'] = df.apply(transform_fare, axis=1)

#Updating file contents for version 2.




