import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


forests = pd.read_csv('forest_dataset.csv')
labels = forests[forests.columns[-1]].values
data = forests[forests.columns[:-1]].values
train_data, test_data, train_labels, test_labels = train_test_split(data,labels,test_size=0.2,random_state=42)
print(forests.iloc[:,-1].unique())

model = KNeighborsClassifier()
params = {'n_neighbors':np.arange(1,11),
            'metric':['manhattan','euclidean'],
            'weights':['uniform','distance']}


betaModel = KNeighborsClassifier()
betaModel.fit(train_data,train_labels)
betaPrediction = betaModel.predict(test_data)
# print(accuracy_score(test_labels,betaPrediction))


model=GridSearchCV(model,params,cv=5,scoring='accuracy',n_jobs=-1)
model.fit(train_data,train_labels)
prediction = model.predict(test_data)
print(accuracy_score(test_labels,prediction))
print(len(prediction[prediction==3])/len(prediction))
