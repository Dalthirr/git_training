import numpy as np
import pandas as pd


def do_something(data):

    if not data.empty:
        print("DataFrame detected")
        return np.mean(data['col1'])
        psuej cos
    raise ValueError("We have nothing here!")



if __name__ == "__main__":
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    print(do_something(df))
    print("jestem w dupie hahaha hihihi")

