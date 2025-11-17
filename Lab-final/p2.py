import numpy as np

dataset = 5

X0_Class = np.array([
    [-1.3, -0.7, 0.45],
    [-0.8, -1.1, 0.12],
    [-1.2, -1.4, 0.77],
    [-0.9, -0.6, 0.33],
    [-1.0, -1.5, 0.72],
])


X1_Class = np.array([
    [1.2, 0.8, 0.51],
    [0.9, 1.3, 0.26],
    [1.4, 1.1, 0.88],
    [1.0, 0.7, 0.37],
    [1.1, 1.5, 0.42],
])

X = np.vstack((X0_Class, X1_Class))
Y = np.hstack((np.zeros(dataset), np.ones(dataset))) 

n_epoch = 15
lines = []


W = np.zeros(X.shape[1])
b = 0.0
lr = 1.0

for epoch in range(n_epoch):

    print(f"Epoch {epoch+1}: W = {W}, b = {b:.2f}")

    for x_i, target in zip(X, Y):

        a = np.dot(W, x_i) + b  
        if a >= 0:
            pred = 1
        else:
            pred = 0

        error = target - pred      
        W = W + lr * error * x_i    
        b = b + lr * error          

    lines.append((W.copy(), b))

print("Final learned weights:", W)
print("Final learned bias:", b)


