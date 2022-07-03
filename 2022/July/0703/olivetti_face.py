from sklearn import datasets
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier, ExtraTreesClassifier, RandomForestClassifier
from sklearn.linear_model import PassiveAggressiveClassifier, SGDClassifier, RidgeClassifier
import os
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.model_selection import train_test_split
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"


dataset = datasets.fetch_olivetti_faces()
print(dataset['data'].shape)
fig = plt.figure()
plt.imshow(dataset["data"][0].reshape(64,64))
plt.savefig('data0.png')

X = dataset["data"]
y = dataset["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

svc = SVC()
svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)
print(' SVC acc:', sum(y_pred==y_test)/len(y_pred))

ada = AdaBoostClassifier(n_estimators=1000)
ada.fit(X_train, y_train)
y_pred = ada.predict(X_test)
print('Ada acc:', sum(y_pred==y_test)/len(y_pred))

ex = ExtraTreesClassifier()
ex.fit(X_train, y_train)
y_pred = ex.predict(X_test)
print('ExtraTrees acc:', sum(y_pred==y_test)/len(y_pred))

rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print(' RandomForest acc:', sum(y_pred==y_test)/len(y_pred))

pa = PassiveAggressiveClassifier()
pa.fit(X_train, y_train)
y_pred = pa.predict(X_test)
print(' PassiveAgressive acc:', sum(y_pred==y_test)/len(y_pred))

sgd = SGDClassifier(max_iter=1000)
sgd.fit(X_train, y_train)
y_pred = sgd.predict(X_test)
print('SGD acc:', sum(y_pred==y_test)/len(y_pred))

