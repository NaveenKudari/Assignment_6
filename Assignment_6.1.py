
# coding: utf-8

# In[30]:


import math
list1=[1550,1700,900,850,1000,950]
mean= sum(list1)/sum([1 for i in list1])
value=0
for i in list1:
    value+=(i-mean)**2
variance=value/(sum([1 for i in list1])-1)
print(math.sqrt(variance))

