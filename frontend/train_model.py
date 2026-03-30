import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def train_models():

    features = ["month","temperature","rainfall","humidity","cases"]

    dengue = pd.read_csv("dengue_processed.csv")
    malaria = pd.read_csv("malaria_processed.csv")

    X_d = dengue[features]
    y_d = dengue["outbreak"]

    X_m = malaria[features]
    y_m = malaria["outbreak"]

    dengue_model = RandomForestClassifier()
    malaria_model = RandomForestClassifier()

    dengue_model.fit(X_d,y_d)
    malaria_model.fit(X_m,y_m)

    return dengue_model, malaria_model