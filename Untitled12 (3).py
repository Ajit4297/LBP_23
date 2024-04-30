#!/usr/bin/env python
# coding: utf-8

# In[5]:


n=int(input())
a=n%10
b=(n//10)%10
c=(a+b)+(a*b)
print("Yes" if c==n else "No")


# In[ ]:




