# coding:utf-8
#%%
import numpy as np
x=np.array([0.3342,0.9565,0.2173]).astype(float)
#xr = np.rollaxis(x, axis=1)
xr -= np.mean(x, axis=1)
xr /= np.std(x, axis=1)
print(x)

# %%
