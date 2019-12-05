def validate_instructor_counts(df):
    '''Confirm that a post is either tagged as `instructor` or `student` but not both.

    Args: 
        df: Pandas DataFrame

    Returns:
        tuple: Tuple representing the counts of `is_instructor` and `is_student` labeled posts.
    '''

    return df['is_instructor'].value_counts(), df['is_student'].value_counts()

def num_nested_dicts(d: dict, column: str):
    '''Function that will send the number of nested dictionaries with a specified key back to the caller.
    Used with len(list(.)) later on in the data pipeline.

    Args: 
        d dict: Outermost dictionary 
        column str: Key upon which we wish to match 

    Usage: 
        df['num_children'] = df['children'].apply(lambda x: len(list(num_nested_dicts(x[0], 'children'))) if len(x) > 0 else 0)
    '''

    if column in d:
        yield d['created']
    for k in d:
        if isinstance(d[k], list) and k == 'column':
            for i in d[k]:
                for j in num_nested_dicts(i):
                    yield j