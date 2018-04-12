import pandas as pd
import numpy as np

def csv_mat(path):

    datos  = pd.read_csv(path, index_col=False, header=1, delimiter = ' ')
    X = []
    for row in datos.iterrows():
        index, data = row
        X.append( [int(e, 16) for e in data.tolist()[:]])

    return np.array(X)


def text_to_int(text):
    t = np.array([ord(e) for e in text])
    return t


def completar(v):
    c = 16 - len(v) % 16
    return np.concatenate([v ,np.array([0] * c)])


sbox = csv_mat("s-box.csv")
etable = csv_mat("e-table.csv")
ltable = csv_mat("e-table.csv")
