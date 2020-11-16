import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def cleanData(path):
    df = pd.read_excel(path)
    
    rename_col = {'Cement (component 1)(kg in a m^3 mixture)':'Cement',
       'Blast Furnace Slag (component 2)(kg in a m^3 mixture)':'Blast_Furnace_Slag',
       'Fly Ash (component 3)(kg in a m^3 mixture)':'Fly_Ash',
       'Water  (component 4)(kg in a m^3 mixture)':'Water',
       'Superplasticizer (component 5)(kg in a m^3 mixture)':'Superplasticizer',
       'Coarse Aggregate  (component 6)(kg in a m^3 mixture)':'Coarse_Agg',
       'Fine Aggregate (component 7)(kg in a m^3 mixture)':'Fine_Agg', 
       'Age (day)': 'Age',
       'Concrete compressive strength(MPa, megapascals) ':'Concrete_Compressive_Str'}
    
    df = df.rename(columns = rename_col)
    
    return df