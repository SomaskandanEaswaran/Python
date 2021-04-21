#!/usr/bin/env python
# coding: utf-8

# Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”

# In[1]:


def check(texts):
    a = texts.lower()
    if a[::-1] == a:
        print(f"The word {texts} is a palindrome")
    else:
        print(f"The word {texts} is not a palindrome")
              
              
check('racecar')


# In[ ]:





# In[ ]:




