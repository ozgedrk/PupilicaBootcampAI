from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas as pd


olivetti = fetch_olivetti_faces()

plt.figure(figsize = (10,5))
for i in range(2):
    plt.subplot(1, 2,i+1)
    plt.imshow(olivetti.images[i], cmap = "gray")
    plt.title(f"goruntu {i+1}")
    plt.axis("off")
    
plt.show()


X = olivetti.data
y = olivetti.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state =  42)

rf_clf = RandomForestClassifier(n_estimators = 100)
rf_clf.fit(X_train, y_train)

y_pred = rf_clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"RF Accuracy: {accuracy}")

# %%
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

california_housing = fetch_california_housing()


X = california_housing.data
y = california_housing.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state =  42)

rf_reg = RandomForestRegressor()
rf_reg.fit(X_train, y_train)

y_pred = rf_reg.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"RF rmse : {rmse}")

























