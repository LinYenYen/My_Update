import pandas as pd
import numpy as np
import typing

df = pd.DataFrame({'key': ['k1', 'k2', 'k3', 'k4', 'k5'],
                   'A': [1, 2, 3, 4, 5],
                   'B': ['a', 'b', 'c', 'd', 'e']})
df_up = pd.DataFrame({'key': ['k2', 'k8', 'k3', 'k4', 'k5', 'k6', 'k1'],
                      'A': [5, 4, 3, 1, 2, 6, 8],
                      'D': ['x', 'y', 'z', 't', 's', 'a', 'b']})

def my_update(left, right, left_on, right_on, add_columns: typing.Union[str, list, None] = 'All'):
    left = left.set_index(left_on)
    right = right.set_index(right_on)
    if add_columns == 'All':
        left_columns = list(left.columns)
        right_columns = list(right.columns)
        for col in right_columns:
            if col not in left_columns:
                left[col] = np.NaN
    elif isinstance(add_columns, list):
        for col in add_columns:
            left[col] = np.NaN
    elif add_columns is None:
        pass
    else:
        print('Error type of given argument！')
        return None
    left.update(right, join='left', overwrite=True)
    left = left.reset_index(left_on)
    return left

df = my_update(df, df_up, left_on=['key'], right_on=['key'], add_columns=None)
print(df)
print(df_up)
