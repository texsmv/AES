import pandas as pd
import numpy as np

def csv_mat(path):

    datos  = pd.read_csv(path, index_col=False, header=None, delimiter = ' ')
    #print(datos)
    X = []
    for row in datos.iterrows():
        index, data = row
        X.append( [int(e, 16) for e in data.tolist()[:]])

    return np.array(X)


def text_to_int(text):
    t = np.array([ord(e) for e in text])
    return t


def completar(v):
    if len(v) % 16 == 0:
        return v
    c = 16 - len(v) % 16
    return np.concatenate([v ,np.array([0] * c)])


sbox = csv_mat("s-box.csv")
etable = csv_mat("e-table.csv")
ltable = csv_mat("l-table.csv")

def mult(v, j):
    v1 , v2 = indices(v)
    j1, j2 = indices(j)

    v = ltable[v1][v2]
    j = ltable[j1][j2]

    val = (v + j) % 255


    i1, i2 = indices(val)
    return etable[i1][i2]



def indices(v):
    v = hex(v)[2:]
    if len(v) == 1:
        return 0, int(v[0], 16)
    else:
        return  int(v[0], 16), int(v[1], 16)
