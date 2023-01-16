import numpy as np

class MyL2LogisticRegression(object):
    def __init__(self, C=1):
        self.coef_ = None
        self.intercept_ = None
        self.C = C

    def sigmoid(self, t):
        return 1. / (1 + np.exp(-t))

    def basic_term(self, X, y, logits):
        expression= (y * (1-self.sigmoid(y * logits)))
        return (-1/y.size) * (expression @ X)

    def regularization_term(self, weights):
        a = np.array([0])
        return a

    def grad(self, X, y, logits, weights):
        return self.basic_term(X,y,logits) + self.regularization_term(weights)*self.C

    def fit(self, X, y, max_iter=1000, lr=0.1):
        # Принимает на вход X, y и вычисляет веса по данной выборке.
        # Множество допустимых классов: {1, -1}
        # Не забудьте про фиктивный признак, равный 1!
        X = np.array(X)
        y = np.array(y)
        y = 2 * y - 1

        # Добавляем признак из единиц
        X = np.hstack([np.ones([X.shape[0], 1]), X])  # [ell, n]
        
        l, n = X.shape
        # Инициализируем веса
        weights = np.random.randn(n)
                
        losses = []
        
        for iter_num in range(max_iter):
            # calculate grad
            logits = (X @ weights.reshape(n, 1)).ravel()  # [ell]
            grad = self.grad(X, y, logits, weights)
            # update weights    
            weights -= grad * lr

            # calculate loss
            loss = np.mean(np.log(1 + np.exp(-y * logits))) + self.C * np.sum(weights[1:] ** 2)
            losses.append(loss)
        
        # assign coef, intersept
        self.coef_ = weights[1:]
        self.intercept_ = weights[0]

        return losses


    def predict_proba(self, X):
        # Принимает на вход X и возвращает ответы модели
        X = np.array(X)
        X = np.hstack([np.ones([X.shape[0], 1]), X])  # [ell, n]
        weights = np.concatenate([self.intercept_.reshape([1]), self.coef_])
        logits = (X @ weights.reshape(-1, 1))  # [ell, 1]

        return self.sigmoid(logits)


    def predict(self, X, threshold=0.5):
        return self.predict_proba(X) >= threshold

dummy_clf = MyL2LogisticRegression(C=10.)
X = np.arange(6).reshape(2, 3)
y = np.array([0, 1])
weights = np.array([-1., 1., 2])
logits = X @ weights

b_t = dummy_clf.basic_term(X, y, logits)
reg_t = dummy_clf.regularization_term(weights)
grad = dummy_clf.grad(X, y, logits, weights)

print(b_t, '\n', reg_t, '\n', grad)