import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# dummy data
X = np.array([[10, 20], [20, 30], [30, 40], [40, 50]])
y = np.array([100, 200, 300, 400])

model = LinearRegression()
model.fit(X, y)

# save model
pickle.dump(model, open("model.pkl", "wb"))

print("model.pkl created successfully")