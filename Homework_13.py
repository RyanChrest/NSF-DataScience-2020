data = pd.read_csv(r'C:\Users\Ryan\Desktop\jupyter\NSF\wine-labeled.csv')
data

wine = data.drop('quality', axis='columns')
wine['type'].replace('red', 1, inplace=True)
wine['type'].replace('white', 0, inplace=True)
wine


X = wine.drop('type', axis='columns')
X

y = wine['type']
y

from sklearn.preprocessing import MinMaxScaler
X = pd.DataFrame(MinMaxScaler().fit_transform(X), columns=X.columns)
X


from sklearn.decomposition import PCA
pca = PCA()
principalComponents = pca.fit_transform(X)
principalDf = pd.DataFrame(data = principalComponents)
principalDf


pca.explained_variance_ratio_

# showing effects of PCA dimensionality
variance_exp_cumsum = pca.explained_variance_ratio_.cumsum().round(2)
fig, axes = plt.subplots(1,1,figsize=(16,7), dpi=100)
plt.plot(variance_exp_cumsum, color='firebrick')
plt.title('Screeplot of Variance Explained %', fontsize=22)
plt.xlabel('# of PCs', fontsize=16)
plt.show()


final = pd.concat([principalDf, y], axis=1)
final

sns.scatterplot(x=0, y=1, hue='type', data=final)

# function to take in data, target, model, percent of variance to fit, a scaling function and ax object for plotting
def pca_fit(df, target, model, pca_percent, scaler = None, ax = None):
    from sklearn.model_selection import train_test_split as tts
    
    y = df[target].to_numpy()
    X = df.drop(target, axis=1)
    label = str(model)
    xtrain, xtest, ytrain, ytest = tts(X, y)
    
    from sklearn.decomposition import PCA
    pca = PCA(pca_percent)
    pca.fit(xtrain)
    xtrain, xtest = pca.transform(xtrain), pca.transform(xtest)

    if scaler is not None:
        scaler.fit(xtrain)
        xtrain, xtest = scaler.transform(xtrain), scaler.transform(xtest)
    
    model.fit(xtrain, ytrain)
    accuracy = model.score(xtest, ytest)
    
    if ax is not None:
        from sklearn.metrics import plot_roc_curve
        plot_roc_curve(model, xtest, ytest, ax=ax, label=label)
    
    return accuracy
    
   
# with no scaling
fig, ax = plt.subplots(nrows=2, figsize=(12, 12))
accuracies = {}
accuracies['Logistic regression'] = pca_fit(wine, 'type', LR(), 0.95, ax=ax[0])
accuracies['KNN'] = pca_fit(wine, 'type', KNN(), 0.95, ax=ax[0])
accuracies['Gaussian NB'] = pca_fit(wine, 'type', GNB(), 0.95, ax=ax[0])
print(accuracies)

# with scaling
fig, ax = plt.subplots(nrows=2, figsize=(12, 12))
accuracies = {}
accuracies['Logistic regression'] = pca_fit(wine, 'type', LR(), 0.95, MinMaxScaler(), ax[0])
accuracies['KNN'] = pca_fit(wine, 'type', KNN(), 0.95, MinMaxScaler(), ax[0])
accuracies['Gaussian NB'] = pca_fit(wine, 'type', GNB(), 0.95, MinMaxScaler(), ax[0])
print(accuracies)
