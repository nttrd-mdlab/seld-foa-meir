import numpy as np
import struct

def fetch_imp(filepath: str, n_mic: int) -> np.ndarray:
    with open(filepath,"rb") as f:
        bin_data = f.read()            
    ret = np.array(struct.unpack( 'd' * (len(bin_data)//8),bin_data))
    ret = ret.reshape((-1,n_mic)).T
    return ret

def convertAB(A):
    #ambiX format
    time = A.shape[1]
    B = np.zeros([4,time],dtype=np.float)
    B[0,:] = A[0] + A[1] + A[2] + A[3] #W
    B[1,:] = A[0] - A[1] + A[2] - A[3] #Y
    B[2,:] = A[0] - A[1] - A[2] + A[3] #Z
    B[3,:] = A[0] + A[1] - A[2] - A[3] #X
    return B