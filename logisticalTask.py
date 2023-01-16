import pandas as pd
all_data = pd.read_csv('forest_dataset.csv')
all_data.head()
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
labels = all_data[all_data.columns[-1]].values
feature_matrix = all_data[all_data.columns[:-1]].values

train_feature_matrix, test_feature_matrix, train_labels, test_labels = train_test_split(
    feature_matrix, labels, test_size=0.2, random_state=42)

C_grid = np.logspace(-5, 5, 11)

train_accuracies = []
test_accuracies = []

#[{1e-05: 0.6440}, {0.0001: 0.6725}, {0.001: 0.6835}, {0.01: 0.6825}, {0.1: 0.6860}, {1.0: 0.6770}, {10.0: 0.6845}, {100.0: 0.6830}, {1000.0: 0.6835}, {10000.0: 0.6860}, {100000.0: 0.6830}]
#[{1e-05: 0.6445}, {0.0001: 0.6730}, {0.001: 0.6845}, {0.01: 0.6900}, {0.1: 0.6880}, {1.0: 0.6900}, {10.0: 0.6910}, {100.0: 0.6935}, {1000.0: 0.6870}, {10000.0: 0.6905}, {100000.0: 0.6925}]
#[{1e-05: 0.6445}, {0.0001: 0.6745}, {0.001: 0.6875}, {0.01: 0.6915}, {0.1: 0.6885}, {1.0: 0.6920}, {10.0: 0.6940}, {100.0: 0.6935}, {1000.0: 0.6920}, {10000.0: 0.6925}, {100000.0: 0.6915}]
#[{1e-05: 0.6445}, {0.0001: 0.6745}, {0.001: 0.6895}, {0.01: 0.6920}, {0.1: 0.6945}, {1.0: 0.6885}, {10.0: 0.6955}, {100.0: 0.6940}, {1000.0: 0.6915}, {10000.0: 0.6960}, {100000.0: 0.6945}]
#[{1e-05: 0.6445}, {0.0001: 0.6745}, {0.001: 0.6905}, {0.01: 0.6960}, {0.1: 0.6935}, {1.0: 0.6955}, {10.0: 0.6950}, {100.0: 0.6985}, {1000.0: 0.6970}, {10000.0: 0.6985}, {100000.0: 0.7000}]

for c in C_grid:
    model=LogisticRegression(C=c,max_iter=100)
    model.fit(train_feature_matrix,train_labels)

    predict = model.predict(test_feature_matrix)
    test_accuracies.append({c : accuracy_score(test_labels, predict)})
print(test_accuracies)