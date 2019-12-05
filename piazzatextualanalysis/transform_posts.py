import os
import re
import glob
import pickle
import pandas as pd

from utils.transform_utils import *

# Get all posts within the data directory
posts = glob.glob('data/posts/*.p')

# Iterate over all posts within a class
for fp in posts:
    # Load each post into a DataFrame and store its networkid
    df = pd.DataFrame(pickle.load(open(fp, "rb")))
    network_id = re.search("posts_(.*).p", fp).group(1)
    
    # Compute different metrics about the class
    df['created'] = pd.to_datetime(df['created'])
    df['num_revisions'] = df['history'].apply(lambda x: len(x))
    df['subject'] = df['history'].apply(lambda x: x[0]['subject'])
    df['is_student'] = df['tags'].apply(lambda x: 'student' in x)
    df['is_instructor'] = df['tags'].apply(lambda x: 'instructor-note' in x)
    df['is_announcement'] = df['config'].apply(lambda x: 1 if 'is_announcement' in x else 0)
    df['num_children'] = df['children'].apply(lambda x: len(list(num_nested_dicts(x[0], 'children'))) if len(x) > 0 else 0)

    # Remove HTML from text column
    df['text'] = df['history'].apply(lambda x: re.sub('<[^<]+?>|\n', ' ', x[0]['content']))
        
    # Reorder the columns
    df = df[['id', 'created', 'type', 'folders', 'tags', 'is_announcement', 'history', 'children', 'tag_good', 'is_student', 'no_answer', 'num_children', 'num_favorites', 'num_revisions', 'unique_views', 'subject','text']]
    
    with open(f"data/dataframes/{fp[11:-23]}_dataframe_{network_id}.p", 'wb') as f:
        pickle.dump(df, f)