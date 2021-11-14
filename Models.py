from numpy.core.fromnumeric import size
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV 
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import TruncatedSVD
from sklearn.svm import SVC
import numpy as np
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from ExtractData import ExtractData



test_columns = ['duration'
,'protocol_type'
,'service'
,'flag'
,'src_bytes'
,'dst_bytes'
,'land'
,'wrong_fragment'
,'urgent'
,'hot'
,'num_failed_logins'
,'logged_in'
,'num_compromised'
,'root_shell'
,'su_attempted'
,'num_root'
,'num_file_creations'
,'num_shells'
,'num_access_files'
,'num_outbound_cmds'
,'is_host_login'
,'is_guest_login'
,'count'
,'srv_count'
,'serror_rate'
,'srv_serror_rate'
,'rerror_rate'
,'srv_rerror_rate'
,'same_srv_rate'
,'diff_srv_rate'
,'srv_diff_host_rate'
,'dst_host_count'
,'dst_host_srv_count'
,'dst_host_same_srv_rate'
,'dst_host_diff_srv_rate'
,'dst_host_same_src_port_rate'
,'dst_host_srv_diff_host_rate'
,'dst_host_serror_rate'
,'dst_host_srv_serror_rate'
,'dst_host_rerror_rate'
,'dst_host_srv_rerror_rate'
,'attack'
,'level']


test_80 = pd.read_csv('KDDTest+.txt', names=test_columns, header=None)
test_20 = pd.read_csv('KDDTest-21.txt', names=test_columns, header=None)
test_main = pd.concat([test_80, test_20])
test_main.columns = test_columns
#print(test_main)


train_80 = pd.read_csv('KDDTrain+.txt', names=test_columns, header=None)
train_20 = pd.read_csv('KDDTrain+_20Percent.txt', names=test_columns, header=None)
train_main = pd.concat([train_80, train_20])
train_main.columns = test_columns
#print(train_main)

#print(test_main.isnull().sum())
#print(train_main.isnull().sum())

main_dataset = pd.concat([train_main, test_main])
#print(main_dataset)

y = main_dataset['attack']
y = y.apply(lambda x: 0 if x == 'normal' else 1)
X = main_dataset.drop(columns=['attack'])
#print(y)
#print(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, train_size=0.67, random_state=42)


 
# --------------------- LOGISTIC REGRESSION --------------------------------
#pipe_lr = make_pipeline( OneHotEncoder(handle_unknown='ignore'), 
 #                       StandardScaler(with_mean=False),
  #                     
   #                     LogisticRegression(random_state=1, ))
#pipe_lr.fit(X_train, y_train)
#y_pred = pipe_lr.predict(X_test)
#scores_lr = cross_val_score(estimator=pipe_lr, X=X_train,
 #                           y=y_train, cv=10, n_jobs=1)
#print('LR ', pipe_lr.score(X_test, y_test), np.mean(scores_lr))
#y_pred = pipe_lr.predict(X_test)
#confmat = confusion_matrix(y_true=y_test, y_pred=y_pred)
#print('Confision matrix:', confmat)




# --------------------- DECISION TREE --------------------------------
#pipe_dt = make_pipeline(OneHotEncoder(handle_unknown='ignore'),  DecisionTreeClassifier(random_state=0))
#pipe_dt.fit(X_train, y_train)
#scores_dt = cross_val_score(estimator=pipe_dt, X=X_train,
 #                           y=y_train, cv=10, n_jobs=1)
#print('DT ', pipe_dt.score(X_test, y_test), np.mean(scores_dt))
#y_pred = pipe_dt.predict(X_test)
#confmat = confusion_matrix(y_true=y_test, y_pred=y_pred)
#print(confmat)

#plot_confusion_matrix(pipe_dt, X_test, y_test) 
#plt.show()



# --------------------- RANDOM FORREST --------------------------------
pipe_rf = make_pipeline(OneHotEncoder(handle_unknown='ignore'), RandomForestClassifier(max_depth=2, random_state=0))
pipe_rf.fit(X_train, y_train)
scores_rf = cross_val_score(estimator=pipe_rf, X=X_train,
                            y=y_train, cv=2, n_jobs=1)
print('RF ', pipe_rf.score(X_test, y_test), np.mean(scores_rf))
y_pred_rf = pipe_rf.predict(X_test)
confmat_rf = confusion_matrix(y_true=y_test, y_pred=y_pred_rf)
print(confmat_rf)



# --------------------- SUPPORT VECTOR MACHINE --------------------------------
pipe_svc = make_pipeline(OneHotEncoder(handle_unknown='ignore'), StandardScaler(with_mean=False), SVC(gamma='auto'))
pipe_svc.fit(X_train, y_train)
y_pred_svc = pipe_svc.predict(X_test)
confmat_svc = confusion_matrix(y_true=y_test, y_pred=y_pred_svc)
print(confmat_svc)
scores_svc = cross_val_score(estimator=pipe_svc, X=X_train,
                            y=y_train, cv=2, n_jobs=1)
print('SVC ', pipe_svc.score(X_test, y_test), np.mean(scores_svc))
