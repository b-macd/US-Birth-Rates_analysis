import pandas as pd
from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn.objects as so
import matplotlib.ticker as ticker
import matplotlib.collections as clt

birth_rates_df = pd.read_csv("../data/us_births_2016_2021.csv")
b_r_extended_df = pd.read_csv('../data/Natality, 2007-2021.txt',header=0,delimiter="\t")

def create_df_from_csv(filepath):
    '''
    function takes a filepath and checks whether 
    it is a csv or txt file then returns a data frame
    from the file
    '''
    if filepath.endswith('csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith('.txt'):
        df = pd.read_csv(filepath,header=0,delimiter="\t")
    return df

def remove_field(field, df):
    '''
    function takes a data frame 
    and removes redundant fields
    such as state codes or others'''
    df = df.drop(columns=field)
    return df

def grams_to_lbs_in_df(df, field):
    '''
    takes a df and a field with values in grams
    and returns the df with a new field containing 
    values in lbs.'''
    ave = df[field].astype(float)
    z= []
    for grams in ave:
        z.append(grams / 453.6)
    df['Weight (lbs)'] = z
    return  df
    


if __name__ == '__main__':

    pass