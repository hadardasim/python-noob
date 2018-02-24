import numpy as np

# sample
x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.9, 2.1])
A = np.vstack([x, np.ones(len(x))]).T
print(A)
result = np.linalg.lstsq(A, y)

speed = np.zeros((3,3,2), dtype=float)
print(speed.shape)
print(speed)

rot_center = [0.6,0.7]
w = 2.0

avg_lin = [1.2, 3.4]
speed += avg_lin
print(speed)

X, Y = np.meshgrid(range(3), range(3))
print(X)
print(Y)

speed[:,:,0] = w*(rot_center[1]-Y)
speed[:,:,1] = w*(X-rot_center[0])
print(speed)


