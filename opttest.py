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

R_est, t_est = solve(X, Y)
# print((R_est @ X.T).T + t_est.T)

print('R_est',R_est, '\n')
print('t_est',t_est, '\n')