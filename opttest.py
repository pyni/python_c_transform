import numpy as np
import cv2

def solve(X, Y):
    """
    Solve Y = RX + t

    Input:
        X: Nx3 numpy array of N points in camera coordinate
        Y: Nx3 numpy array of N points in world coordinate
    Returns:
        R: 3x3 numpy array describing camera orientation in the world (R_wc)
        t: 1x3 numpy array describing camera translation in the world (t_wc)

    """
    # equation (2)
    cx, cy = X.sum(axis=0) / Y.shape[0], Y.mean(axis=0)

    # equation (6)
    x, y = np.subtract(X, cx), np.subtract(Y, cy)

    # equation (13)
    w = x.transpose() @ y

    # equation (14)
    u, s, vh = np.linalg.svd(w)

    # equation (20)
    ide = np.eye(3)
    ide[2][2] = np.linalg.det(vh.transpose() @ u.transpose())
    R = vh.transpose() @ ide @ u.transpose()

    # compute equation (4)
    t = cy - R @ cx

    return R, np.array([t]).transpose()


R, _ = cv2.Rodrigues(np.array([-5, 1, 3], dtype=np.float))
t = np.array ([0.5, 1, 3])
print('R_ori',R, '\n')
print('t_ori',t , '\n')

X = np.random.randint(0, 10, [10, 3])
Y = (R @ X.T).T + t
print('X',X, '\n')
print('Y',Y  , '\n')


R_est, t_est = solve(X, Y)
print('Y_calculated', (R_est @ X.T).T + t_est.T)

print('R_est',R_est, '\n')
print('t_est',t_est, '\n')




X=np.array([[-0.163, -0.132, 0.614],[0.114, -0.129, 0.553],[0.112, 0.142, 0.542],[-0.173, 0.150, 0.525],[-0.014, -0.015, 0.464]])
Y=np.array([[-0.534, -0.475, -0.008],[-0.422, -0.229, 0.010],[-0.173, -0.347, 0.031],[-0.295, -0.605, 0.028],[-0.381, -0.399, 0.084] ])

R_est, t_est = solve(X, Y)
print('Y_calculated', (R_est @ X.T).T + t_est.T)

print('R2_est',R_est, '\n')
print('t2_est',t_est, '\n')


query_X=np.array([-0.026, 0.003, 0.538])

query_Y = np.dot(R_est,query_X)+t_est.T

print('query_Y',query_Y, '\n')


