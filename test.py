#import matrix tool
import numpy as np
from sklearn.preprocessing import LabelEncoder   #import machine learning set
import pandas as pd


# import the required data
le = LabelEncoder()
dresses= pd.read_excel ("Attribute DataSet new.xls")



#transform
dresses['Style'] = le.fit_transform(dresses['Style'])
dresses['Price'] = le.fit_transform(dresses['Price'])
dresses['Size'] = le.fit_transform(dresses['Size'])
dresses['Season'] = le.fit_transform(dresses['Season'])
dresses['NeckLine'] = le.fit_transform(dresses['NeckLine'])
dresses['SleeveLength'] = le.fit_transform(dresses['SleeveLength'])
dresses['waiseline'] = le.fit_transform(dresses['waiseline'])
dresses['Material'] = le.fit_transform(dresses['Material'])
dresses['FabricType'] = le.fit_transform(dresses['FabricType'])
dresses['Decoration'] = le.fit_transform(dresses['Decoration'])
dresses['Pattern Type'] = le.fit_transform(dresses['Pattern Type'])