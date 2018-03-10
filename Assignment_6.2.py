
# coding: utf-8

# In[38]:


list1=[3,21,98,203,17,9]
mean = sum(list1)/sum([1 for i in list1])
value=0
for i in list1:
    value+=(i-mean)**2
variance=value/(sum([1 for i in list1])-1)
print("variance is:"+" "+str(variance))

