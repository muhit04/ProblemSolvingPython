# Following along simple machine learning tutorial
# Source: https://bit.ly/2wJXuXz

import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

class SimpleMachineLearningTutorial:
    def __init__(self):
        # Load dataset
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
        names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
        self.dataset = pandas.read_csv(url, names=names)

    def get_dataset_shape(self):
        return self.dataset.shape

    def get_dataset_head(self):
        return self.dataset.head(10)

    def get_statistical_summary(self):
        return self.dataset.describe()

    def get_class_dist(self):
        return self.dataset.groupby('class').size()

    def univariate_boxplot(self):
        self.dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
        plt.show()

    def univariate_hist(self):
        self.dataset.hist()
        plt.show()

    def multivariate_scatter(self):
        scatter_matrix(self.dataset)
        plt.show()
        
    def evaluate_models(self):
        array = self.dataset.values
        X = array[:,0:4]
        Y = array[:,4]
        validation_size = 0.20
        seed = 7
        X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
        scoring = 'accuracy'
        models = []
        models.append(('LR', LogisticRegression()))
        models.append(('LDA', LinearDiscriminantAnalysis()))
        models.append(('KNN', KNeighborsClassifier()))
        models.append(('CART', DecisionTreeClassifier()))
        models.append(('NB', GaussianNB()))
        models.append(('SVM', SVC()))
        # evaluate each model in turn
        results = []
        names = []
        for name, model in models:
            kfold = model_selection.KFold(n_splits=10, random_state=seed)
            cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
            results.append(cv_results)
            names.append(name)
            msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
            print(msg)

        return (results, names, X_train, X_validation, Y_train, Y_validation)

    def compare_algorithms(self):
        results = self.evaluate_models()[0]
        names = self.evaluate_models()[1]
        fig = plt.figure()
        fig.suptitle('Algorithm Comparison')
        ax = fig.add_subplot(111)
        plt.boxplot(results)
        ax.set_xticklabels(names)
        plt.show()

    def make_predictions(self):
        X_train = self.evaluate_models()[2]
        X_validation = self.evaluate_models()[3]
        Y_train = self.evaluate_models()[4]
        Y_validation = self.evaluate_models()[5]
        knn = KNeighborsClassifier()
        knn.fit(X_train, Y_train)
        predictions = knn.predict(X_validation)
        print(accuracy_score(Y_validation, predictions))
        print(confusion_matrix(Y_validation, predictions))
        print(classification_report(Y_validation, predictions))


