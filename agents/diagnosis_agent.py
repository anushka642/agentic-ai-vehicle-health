import pickle

class DiagnosisAgent:
    def __init__(self):
        self.model = pickle.load(open("models/failure_model.pkl", "rb"))

    def predict_failure(self, data):
        if "failure" in data.index:
            data = data.drop("failure")  

        X = data.values.reshape(1, -1)
        return self.model.predict(X)[0]
