# Gerekli kutuphaneleri iceriye aktar
# Veri setini yukle
# Feature ve hedef degiskenlerini elde et
# Train test split
# Standardization
# KNN tanimla ve train et
# KNN modeli test edelim ve dogruluk hesapla


from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

import pandas as pd

cancer = load_breast_cancer()
df = pd.DataFrame(data = cancer.data, columns = cancer.feature_names)
df["target"] = cancer.target

X = cancer.data
y = cancer.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 2)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
y_pred_train = knn.predict(X_train)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy : {accuracy}")
print(f"Training Accuracy: {accuracy_score(y_train, y_pred_train)}")

# %% HYPERPARAMETER TUNING

import matplotlib.pyplot as plt

k_values = []
accuracy_values = []

for k in range(1,21):
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    acccurcy = accuracy_score(y_test, y_pred)
    k_values.append(k)
    accuracy_values.append(acccurcy)
    
plt.figure()
plt.plot(k_values, accuracy_values, marker = "o")
plt.title("K degerine gore dogruluk")
plt.xlabel("K degeri")
plt.ylabel("Dogruluk")
plt.xticks(k_values)
plt.grid(True)

# %% Kullanilacak mesafe metriginin tanimlanmasi

distance_metrics = ["euclidean", "manhattan"]

for distance_metric in distance_metrics:
    knn = KNeighborsClassifier(n_neighbors = 4, metric =distance_metric)
    knn.fit(X_train, y_train)
    
    y_pred = knn.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Distance metric : {distance_metric}")
    print(f"Accuracy : {accuracy}")


distance_metrics = ["euclidean", "manhattan", "chebyshev", "minkowski"]
results = {}

for distance_metric in distance_metrics:
    k_values = []
    accuracy_values = []

    for k in range(1, 21):
        knn = KNeighborsClassifier(n_neighbors=k, metric=distance_metric)
        knn.fit(X_train, y_train)

        y_pred = knn.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        k_values.append(k)
        accuracy_values.append(accuracy)

    results[distance_metric] = (k_values, accuracy_values)

plt.figure()
for distance_metric in distance_metrics:
    k_values, accuracy_values = results[distance_metric]
    plt.plot(k_values, accuracy_values, marker="o", label=f"{distance_metric}")

plt.title("K değerine göre doğruluk (Farklı Mesafe Türleri)")
plt.xlabel("K değeri")
plt.ylabel("Doğruluk")
plt.legend()
plt.grid(True)
plt.show()


# %% KNN REGRESSOR

from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
X = np.sort(5 * np.random.rand(40,1), axis = 0 )
y = np.sin(X).ravel()

plt.figure()
plt.scatter(X,y, label = "Original")

y[::5] += 1 * (0.5 - np.random.rand(8))
plt.scatter(X,y, label = "Noise")
plt.legend()

n_neighbors = 5
T = np.linspace(0, 5, 500)[:, np.newaxis]

plt.figure()

for i, weights in enumerate(["uniform","distance"]):
    knn = KNeighborsRegressor(n_neighbors, weights = weights)
    y_pred = knn.fit(X, y).predict(T)
    
    plt.subplot(1,2,i+1)
    plt.scatter(X, y, color = "orange", label = "Original with noise")
    plt.plot(T, y_pred, color = "blue", label = f"predictions with {weights}")
    plt.legend()