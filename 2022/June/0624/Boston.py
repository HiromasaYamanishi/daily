from sklearn import datasets
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import lightgbm as lgb
boston = datasets.load_boston()
X = boston['data']
y = boston['target']
y=y.reshape(-1,1)
ss = StandardScaler()
X = ss.fit_transform(X)

kf = KFold(n_splits = 5, random_state=42, shuffle=True)

for i, (train_index, valid_index) in enumerate(kf.split(X)):
    X_train, X_valid = X[train_index], X[valid_index]
    y_train, y_valid = y[train_index], y[valid_index]
    if i==0:
        break


train_dataset=lgb.Dataset(X_train,y_train)
valid_dataset=lgb.Dataset(X_valid, y_valid)
Dataset=lgb.Dataset(X,y)
params = {
            'task': 'train',
            'boosting_type': 'gbdt',
            'objective': 'regression',
            'metric': 'rmse',
            'learning_rate':0.1,
        }


model = lgb.train(
                params=params,
                train_set=train_dataset, 
                valid_sets=valid_dataset,
                num_boost_round = 500,
                early_stopping_rounds = 50,
                )

y_pred = model.predict(X_valid)
print(mean_squared_error(y_valid, y_pred))

#print(X_valid.shape,y_valid.shape)
#lgbmReg=lgb.LGBMRegressor()
#lgbmReg.fit(X_train, y_train,eval_set=[X_valid, y_valid])



