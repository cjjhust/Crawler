# coding:utf-8
#%%
import numpy as np
x=np.array([0.3342,0.9565,0.2173]).astype(float)
xr = np.rollaxis(x, axis=axis)
    xr -= np.mean(x, axis=axis)
    xr /= np.std(x, axis=axis)
    # print(x)

# %%
