from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn import metrics
import mlflow 
import os
from mlflow.sklearn import save_model, log_model

mlflow.set_tracking_uri(os.environ["MLFLOW_HOST"])
mlflow.set_experiment("iris-exp")

# Injest data
iris = load_iris()

# Prepare training data
X, y = iris.data, iris.target  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

with mlflow.start_run():
    # Train model
    n_estimators = 150
    mlflow.log_param("n_estimators", n_estimators)
    clf = RandomForestClassifier(n_estimators=n_estimators)
    clf.fit(X_train,y_train)

    # Evaluate
    y_pred=clf.predict(X_test)

    score = metrics.accuracy_score(y_test, y_pred)
    print(f"Accuracy: {score}")
    mlflow.log_metric(key="accuracy", value=score)
    
    # Save model 
    # save_model(clf, 'iris_model') uncomment if you want to save localy
    log_model(clf, 'iris_model')