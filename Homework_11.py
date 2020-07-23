from sklearn.linear_model import LogisticRegression as LR
from sklearn.metrics import plot_roc_curve
# test train split
fig, ax = plt.subplots(figsize=(18, 10))
for i in range(10):
    xtrain, xtest, ytrain, ytest = tts(covid.age.to_numpy(), covid.death.to_numpy())
    model = LR()
    fit = model.fit(xtrain.reshape(-1, 1), ytrain)
    plot_roc_curve(model, xtest.reshape(-1,1), ytest, ax=ax)
    
    
from sklearn.model_selection import cross_validate
# leave out one
fig, ax = plt.subplots(figsize=(18, 10))
model = LR()
results = cross_validate(model, 
                         covid.age.to_numpy().reshape(-1, 1), covid.death.to_numpy(), 
                         cv=10, return_estimator=True, scoring='roc_auc')
for i in range(len(results['estimator'])):
    _, xtest, _, ytest = tts(covid.age.to_numpy().reshape(-1, 1), covid.death.to_numpy())
    plot_roc_curve(results['estimator'][i], 
                    xtest, 
                    ytest,
                    ax=ax)
