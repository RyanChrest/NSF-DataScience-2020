data = pd.read_csv(r'C:\Users\Ryan\Desktop\jupyter\regression-data-set.csv')
data.plot(kind='scatter', x='x', y='y')


from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import mean_squared_error as mse
def fit_poly(X, Y, degrees, runs):
    mean_error = []; std_error = []
    for degree in range(degrees):
        errors = []
        for run in range(runs):
            xtrain, xtest, ytrain, ytest = tts(X, Y)
            model = np.polyfit(xtrain, ytrain, degree)
            predicted = np.polyval(model, xtest)
            error = mse(ytest, predicted, squared=False)
            errors.append(error)
        mean_error.append(np.mean(errors)); std_error.append(np.std(errors))
    return (mean_error, std_error)

mean, std= fit_poly(data['x'], data['y'], 15, 100)


plt.plot(range(len(mean)), [mean[index] + std[index] for index in range(len(mean))], color='orange')
plt.plot(range(len(mean)), mean, marker='o', color='blue')
plt.plot(range(len(mean)), [mean[index] - std[index] for index in range(len(mean))], color='green')
plt.yscale('log')
plt.show()


data.plot.scatter('x', 'y')
model = np.polyfit(data['x'], data['y'], 9)
values = np.polyval(model, data['x'])
plt.plot(data['x'], values, color='red')
