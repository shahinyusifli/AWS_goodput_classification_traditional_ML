from sklearn.preprocessing import OneHotEncoder, LabelEncoder, LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

ohe = OneHotEncoder()
lb = LabelBinarizer()
le = LabelEncoder()
std = StandardScaler(with_mean=False)
lda = LinearDiscriminantAnalysis(n_components=2)

class TransformData:

    
    def __init__(self, data):
        self.data = data
        
    
    def encoding(self):
        try:
            self.data['<service (Standard/CloudFront)>'] = le.fit_transform(self.data['<service (Standard/CloudFront)>'])
            self.data['<cloud region>'] = le.fit_transform(self.data['<cloud region>'])
            self.data['<source region>'] = le.fit_transform(self.data['<source region>'])  
            self.X = ohe.fit_transform(self.data[['<service (Standard/CloudFront)>', '<cloud region>', '<source region>']])
            self.y = self.data['<goodput [KiB/s]>'].apply(lambda x: 1 if x < 1587.8199350583818 else 0)
            return self.X, self.y
        except:
            print('There is some problem in ENCODING')

    
    def train_test_split(self):
        try:
            self.X_encoded, self.y_encoded = self.encoding()
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X_encoded, self.y_encoded, test_size=0.33, random_state=42)
            return self.X_train, self.X_test, self.y_train, self.y_test
        except:
            print('There is some problem in TRAN_TEST_SPLIT')

    def scale(self):
        self.X_train, self.X_test, self.y_train, self.y_test = self.train_test_split()
        self.X_train_std = std.fit_transform(self.X_train)
        self.X_test_std = std.transform(self.X_test)
        return self.X_train_std, self.X_test_std, self.y_train, self.y_test

    def dimensionality_reduction(self):
        self.X_train_std, self.X_test_std, self.y_train, self.y_test = self.scale()
        self.X_train_lda = lda.fit_transform(self.X_train_std.toarray(), self.y_train)
        self.X_test_lda = lda.transform(self.X_test_std.toarray())
        return self.X_train_lda, self.X_test_lda, self.y_train, self.y_test
