#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy.random import seed
import numpy as np
from numpy.random import normal
import math
import matplotlib.pyplot as plt
import pandas as pd
q_estimated = 0
T =200
machines = 5
average_reward=0
numbers_of_selections_of_each_machine = [0] * machines
sums_of_rewards_for_each_machine = [0] * machines
data = normal(loc=0, scale=1, size=200)
machines_selected = []
total_rewards = 0


# In[2]:


data
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(data, 30)
plt.show()


# In[10]:



for i in range(1,T):
    if (numbers_of_selections_of_each_machine[i] > 0):
        average_reward = sums_of_rewards_for_each_machine[i] / numbers_of_selections_of_each_machine[i]
        UCB[i] = average_reward + 2(math.log(i)/ numbers_of_selections_of_each_machine[i])
    reward=np.random.choice(data)
    
    i = i+1
    for j in (1,machines):
         j=j+1
    print(reward)
    


# In[ ]:




