import numpy as np

def Nanfilling(data, missingindex):

    num  = np.shape(missingindex)[0];

    datanew = data.copy()

    for i in range(num):
        m = missingindex[i, 0]
        n = missingindex[i, 1]
        datanew[m, n] = np.nan
    return datanew

