
# coding: utf-8

# ### Problem Statement 1:
# Write a function to compute 5/0 and use try/except to catch the exceptions.

# In[12]:


def division(num1,num2):
    result = None
    try:
        result = num1/num2
    except ZeroDivisionError as z:
        print("There is a exception : {}".format(z))
    return result
    


# In[13]:


division(5,0)

