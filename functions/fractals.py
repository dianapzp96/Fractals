import numpy as np


def BarnsleyFern(iters=1000000):
    
    x_coords = []
    y_coords = []
    
    # Input matrices
    z = [[1.0],
         [1.0]]
    a = [0.00, 0.85, 0.20, -0.15]
    b = [0.00, 0.04, -0.26, 0.28]
    c = [0.00, -0.04, 0.23, 0.26]
    d = [0.16, 0.85, 0.22, 0.24]
    e = [0.00, 0.00, 0.00, 0.00]
    f = [0.00, 1.60, 1.60, 0.44]
    p = [0.01, 0.85, 0.07, 0.07] # probabilities
    
    # Matrix operations
    for _ in range(iters):
        i = np.random.choice(np.arange(4), p=p)
        A = np.array([[a[i], b[i]],
                      [c[i], d[i]]])
        t = np.array([[e[i]],
                      [f[i]]])
        A_dot_z = A.dot(z)
        z = np.add(A_dot_z, t)
        x_coords.append(z[0][0])
        y_coords.append(z[1][0])
    
    return x_coords, y_coords



def SierpinskiTriangle(size=1024):

    first_row = np.zeros(size, dtype=int)
    first_row[int(size/2)-1] = 1
    rows = np.zeros((int(size/2),size), dtype=int)
    rows[0] = first_row
    
    for i in range(1,int(size/2)):
        rows[i] = (np.roll(rows[i-1],-1) + rows[i-1] + np.roll(rows[i-1],1)) % 2
        
    m = int(np.log(size)/np.log(2))
    rows = rows[0:2**(m-1),0:2**m]
    
    return rows
