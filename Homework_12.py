data = pd.read_csv(r'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data')
data.columns = ['id', 'Clump Thickness', 'Uniformity of Cell Size', \
                'Uniformity of Cell Shape', 'Marginal Adhesion', \
                'Single Epithelial Cell Size', 'Bare Nuclei', \
                'Bland Chromatin', 'Normal Nucleoli', \
                'Mitoses', 'Class'
				]

# data cleaning
data = data[data['Bare Nuclei'] != '?'].reset_index()
data['Bare Nuclei'] = data['Bare Nuclei'].astype('int64')

data['Class'].replace(4, 1, inplace=True)
data['Class'].replace(2, 0, inplace=True)
data.drop(['index', 'id'], axis=1, inplace=True, errors='ignore')
data


# function to plot ROC curves for each column fit for any SKLearn model

def roc(df, target, model_to_fit, ax):
    from sklearn.model_selection import train_test_split as tts
    from sklearn.metrics import plot_roc_curve
    
    y = df[target].to_numpy()
    predictors = df.drop(target, axis=1)
    model = model_to_fit
    
    for col in predictors.columns:
        X = df[col].to_numpy()
        
        xtrain, xtest, ytrain, ytest = tts(X, y)
        
        fit = model.fit(xtrain.reshape(-1, 1), ytrain)
        
        plot_roc_curve(model, xtest.reshape(-1,1), ytest, ax=ax, label=col)
		

# using the function with LR, KNN, GNB models on the data set to evaluate their regression capabilities
from sklearn.linear_model import LogisticRegression as LR
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.naive_bayes import GaussianNB as GNB
fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(18, 18), sharex=True, sharey=True)
roc(data, 'Class', LR(), ax[0])
roc(data, 'Class', KNN(), ax[1])
roc(data, 'Class', GNB(), ax[2])
