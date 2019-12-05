#!/usr/bin/env python
# coding: utf-8

# In[20]:


import time
import os
import pandas as pd
import pickle
from piazza_api import Piazza


# In[21]:


# https://github.com/hfaran/piazza-api
# Authenticate into your Piazza Account
p = Piazza()
p.user_login(email=os.environ['PIAZZA_EMAIL'], password=os.environ['PIAZZA_PASSWORD'])


# In[22]:


# Get all of the user's classes
user_classes = p.get_user_classes()


# In[23]:


# Add all of the user's COMP 401 sections to a list 
comp_401_sections = []
for user_class in user_classes:
    if '401' in user_class['num']:
        comp_401_sections.append(user_class)

# Get all the network IDs for the 401 sections 
nids = [section['nid'] for section in comp_401_sections]


# In[24]:


# Pickle all of the posts made for that course
for network_id in nids:
    course = p.network(network_id)
    
    # Get all users and all posts for that course
    posts = course.iter_all_posts(limit=None)
    
    try:
        pickled_posts = []
        for post in posts:
            time.sleep(1)
            pickled_posts.append(post)
    except Exception as e:
        print(e)
                
    # Write all of the posts to a pickle file stored in the data folder
    with open(f"data/posts/{os.environ['PIAZZA_EMAIL']}_posts_{network_id}.p", 'wb') as f:
        pickle.dump(pickled_posts, f)
