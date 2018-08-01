import numpy as np
import transform_base as tb

#FROM euler TO ROTATION MATRIX
A= np.eye(4,4)
A[0:3,0:3] =  tb.euler2rotm([3.14,3.14,3.14]) 
A[0,-1] = 1
A[1,-1] = 2
A[2,-1] = 3 
