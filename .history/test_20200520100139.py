# coding:utf-8
#%%
import numpy as np
x=np.random.random((2,3))
print(x)

# %%
from sklearn.preprocessing import Normalizer
nor_scaler=Normalizer().fit(x).transform(x)
print(nor_scaler)
# %%
from sklearn import preprocessing
print(preprocessing.normalize(x,norm='l1'))

# %%
