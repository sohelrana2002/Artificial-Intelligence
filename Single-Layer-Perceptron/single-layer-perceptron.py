import numpy as np
import matplotlib.pyplot as plt

n_samples = 10

X_class1 = np.array([
    [-1.3, -0.7],
    [-0.8, -1.1],
    [-1.2, -1.4],
    [-0.9, -0.6],
    [-1.5, -1.2],
    [-0.7, -1.3],
    [-1.1, -0.8],
    [-1.4, -1.0],
    [-0.6, -0.9],
    [-1.0, -1.5]
])

X_class2 = np.array([
    [1.2, 0.8],
    [0.9, 1.3],
    [1.4, 1.1],
    [1.0, 0.7],
    [1.5, 1.2],
    [0.8, 1.4],
    [1.3, 0.9],
    [1.1, 1.5],
    [0.7, 1.0],
    [1.6, 1.3]
])

# Combine
X = np.vstack((X_class1, X_class2))
y = np.hstack((np.zeros(n_samples), np.ones(n_samples)))  # Labels: 0 and 1

n_epoch = 50
lines = []

# initialize weights directly
W = np.zeros(X.shape[1])
b = 0.0
lr = 1.0     # learning rate

for epoch in range(n_epoch):

    # show current params before update
    print(f"Epoch {epoch+1}: W = {W}, b = {b:.2f}")

    # ---- one epoch of training ----
    for x_i, target in zip(X, y):

        # ----- forward computation -----
        a = np.dot(W, x_i) + b      # linear combination
        if a >= 0:
            pred = 1
        else:
            pred = 0

        # ----- backward / update -----
        error = target - pred       # (t − ŷ)
        W = W + lr * error * x_i    # update each weight
        b = b + lr * error          # update bias

    # store updated weights after this epoch
    lines.append((W.copy(), b))

# final learned parameters
print("Final learned weights:", W)
print("Final learned bias:", b)
