from sklearn import datasets
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.utils import shuffle
iris_dataset=datasets.load_iris()
X=iris_dataset['data']
y=iris_dataset['target']
X,y=shuffle(X,y,random_state=0)
skf=StratifiedKFold(n_splits=5,shuffle=True)
for i,(train_index,valid_index) in enumerate(skf.split(X,y)):
    X_train,X_valid=X[train_index],X[valid_index]
    y_train,y_valid=y[train_index],y[valid_index]
    if i==0:
        break

lr=LogisticRegression()
lr.fit(X_train,y_train)
y_pred=lr.predict(X_valid)

print('accuracy:',(y_pred==y_valid).sum()/len(y_pred))
