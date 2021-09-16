import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from scipy import io
import eli5
from eli5.sklearn import PermutationImportance
import pickle

X_all = np.load("../chain_double_clean.npy")
y_all = np.load("../F_double_clean.npy")
print (X_all.shape, y_all.shape)

X_20000 = X_all[0:20000]
y_20000 = y_all[0:20000]

X_train, X_test, y_train, y_test = train_test_split(X_20000, y_20000, shuffle=True, random_state=33467829, test_size=0.2)

# define Fit regression model
svr_rbf = SVR(kernel='rbf', C=5, gamma=0.25, epsilon=0.2)
svr_rbf.fit(X_train,y_train)

y_train_predict = svr_rbf.predict(X_train)
y_test_predict = svr_rbf.predict(X_test)

R2_train = r2_score(y_train, y_train_predict)
MSE_train = mean_squared_error(y_train, y_train_predict)
MAE_train = mean_absolute_error(y_train, y_train_predict)
print ('Train R2:',R2_train, "MSE:",MSE_train, "MAE",MAE_train)
  
R2_test = r2_score(y_test, y_test_predict)
MSE_test = mean_squared_error(y_test, y_test_predict)
MAE_test = mean_absolute_error(y_test, y_test_predict)
print ('Test R2:',R2_test, "MSE:",MSE_test, "MAE",MAE_test)

io.savemat("Train.mat", {'y_train': y_train, 
                         'y_train_predict': y_train_predict, 
                         'R2_train': R2_train, 
                         'MSE_train': MSE_train, 
                         'MAE_train': MAE_train})

io.savemat("Test.mat", {'y_test': y_test, 
                         'y_test_predict': y_test_predict, 
                         'R2_test': R2_test, 
                         'MSE_test': MSE_test, 
                         'MAE_test': MAE_test})



perm = PermutationImportance(svr_rbf).fit(X_test, y_test)
eli5.show_weights(perm)

pickle.dump(svr_rbf, open(svr_rbf.pickle, 'wb'))

