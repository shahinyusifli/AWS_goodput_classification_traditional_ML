from math import log
import pandas as pd 
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot as plt
from dtreeviz.trees import dtreeviz 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import StandardScaler



# ----------- Loading data --------------

test_1 = pd.read_table("aws_data.dat", sep="|", usecols=['<service (Standard/CloudFront)>', '<source region>',
                        '<cloud region>', '<download IP address>', '<object size [KiB]>', '<elapsed download time [s]>',
                        '<goodput [KiB/s]>', '<3x round-trip latencies [ms]>', '<number of hops toward destination>',
                         '<download timestamp>', '<traceroute timestamp>'])
print(test_1[['<goodput [KiB/s]>' , '<service (Standard/CloudFront)>', '<source region>', '<object size [KiB]>']])
print(test_1.isnull().sum())


# ----------- Encoders --------------
 
ohe = OneHotEncoder()
lb = LabelBinarizer()
le = LabelEncoder()

test_1['<service (Standard/CloudFront)>'] = le.fit_transform(test_1['<service (Standard/CloudFront)>'])
test_1['<cloud region>'] = le.fit_transform(test_1['<cloud region>'])
test_1['<source region>'] = le.fit_transform(test_1['<source region>'])

X = ohe.fit_transform(test_1[['<service (Standard/CloudFront)>', '<cloud region>', '<source region>']])
y = test_1['<goodput [KiB/s]>'].apply(lambda x: 1 if x < 1587.8199350583818 else 0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


#StandartScale
std = StandardScaler(with_mean=False)

X_train_std = std.fit_transform(X_train)
X_test_std = std.transform(X_test)


#LDA
lda = LinearDiscriminantAnalysis()
X_train_lda = lda.fit_transform(X_train_std.toarray(), y_train)
X_test_lda = lda.transform(X_test_std.toarray())


# ----------- Models -------------- 

log_rec = LogisticRegression(max_iter=200)
log_rec_model = log_rec.fit(X_train_lda, y_train)
y_predict_log_rec = log_rec.predict(X_test_lda)

dt = DecisionTreeClassifier()
dt_model = dt.fit(X_train_lda, y_train)
y_predict = dt_model.predict(X_test_lda)

rfc = RandomForestClassifier(max_depth=10, random_state=2)
rfc_model = rfc.fit(X_train_lda, y_train)
y_predict_rfc = rfc_model.predict(X_test_lda)


# ----------- Acc scores -------------- 

dt_score = dt_model.score(X_test_lda, y_test)
dt_acc_score = accuracy_score(y_predict, y_test)
rfc_acc_score = accuracy_score(y_predict_rfc, y_test)
log_rec_score = accuracy_score(y_predict_log_rec, y_test)


print('Max:', test_1['<goodput [KiB/s]>'].max())
print('Min:', test_1['<goodput [KiB/s]>'].min())
print('Mean:', test_1['<goodput [KiB/s]>'].mean())
print('Median:', test_1['<goodput [KiB/s]>'].median())


print(dt_score*100)
print(dt_acc_score*100)
print(rfc_acc_score*100)
print(log_rec_score*100)








