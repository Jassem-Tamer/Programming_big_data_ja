
# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd


# In[6]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


# In[7]:

s


# In[8]:

s.index


# In[13]:

pd.Series np.random.randn(5)


# In[14]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# In[15]:

d


# In[16]:

pd.Series(d)


# In[17]:

pd.Series(d, index=['b', 'c', 'd', 'a'])


# In[18]:

s


# In[19]:

s[0]


# In[20]:

s[:3]


# In[21]:

s[s>s.median()]


# In[22]:

s[[4, 3, 1]]


# In[23]:

np.exp(s)


# In[26]:

s['a']


# In[27]:

s['e'] = 12.


# In[28]:

s


# In[30]:

s['f']


# In[31]:

'e' in s


# In[32]:

if 'e' in s:
    print(s['e'])


# In[33]:

s.get('e')


# In[34]:

s +s


# In[35]:

s *2


# In[36]:

s/2


# In[37]:

s[1:]


# In[38]:

s[:-1]


# In[39]:

s[1:] + s[:-1]


# In[44]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}


# In[45]:

df = pd.DataFrame(d)


# In[46]:

df


# In[47]:

np.sum(one)


# In[48]:

np.sum(df)


# In[49]:

np.sum(df)/2


# In[51]:

c = {'one' : [1., 2., 3., 4.],'two' : [4., 3., 2., 1.]}


# In[54]:

pd.DataFrame(c)


# In[56]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[57]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]


# In[58]:

data


# In[59]:

pd.DataFrame(data)


# In[60]:

pd.DataFrame(data, index=['first', 'second'])


# In[61]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]


# In[64]:

pd.DataFrame(data2)


# In[65]:

pd.DataFrame(data2, index=['first', 'second'])


# In[66]:

df


# In[67]:

df['three'] = df['one'] * df['two']


# In[68]:

df


# In[69]:

df['flag'] = df['one'] >2


# In[70]:

df


# In[71]:

df.pop('flag')


# In[72]:

df


# In[73]:

df['four'] = 'bar'


# In[74]:

df


# In[ ]:



