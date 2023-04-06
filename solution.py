import pandas as pd 

import numpy as np 

from scipy.stats import norm 

chat_id = 783729615 

def solution(p: float, x: np.array) -> tuple: 
#x.mean()=C-0.5 
#C=x.mean()+0.5 
E=x.mean() 
s=0 
for c in x: 
s+=(c-E)**2 
s/=len(x)-1 
s=s**0.5 
alpha=1-p 
left=E+norm.ppf(alpha/2)*s/len(x)**0.5+0.5 
right=E-norm.ppf(alpha/2)*s/len(x)**0.5+0.5 
left*=2/68**2 
right*=2/68**2 
return left, right
