#!/usr/bin/env python
# coding: utf-8

# Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.

# In[1]:


def count(text):
    counta = countb =counti =counto = countu= 0
    a = text.lower()
    #b = ['a','e','i','o', 'u','A','E','I','U','O']
    for i in a:
        if i == 'a' :
            counta = a.count(i)
        elif i =='e' :
            countb =a.count(i)
        elif i =='i' :
            counti =a.count(i)
        elif i == 'o' :
            counto =a.count(i)
        elif i == 'u' :
            countu =a.count(i)
    print("A: " , counta)
    print("E: " , countb)
    print("I: " , counti)
    print("O: " , counto)
    print("U: " , countu)

count('Aaeioouu')


# In[ ]:





# In[ ]:





# In[ ]:




