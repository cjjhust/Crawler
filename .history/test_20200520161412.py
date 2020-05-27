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
print(preprocessing.normalize(x,norm='l2',axis=1))

# %%
from sklearn.preprocessing import LabelEncoder 
label = ['北京','上海','广州','深圳','南京','成都'] 
enc = LabelEncoder().fit(label)
en_lab = enc.transform(label)
print(en_lab)
# %%
enc.classes_

# %%
from PIL import Image
import pytesseract
image=Image.open("7364.jpg")
