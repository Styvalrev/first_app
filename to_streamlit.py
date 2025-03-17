import joblib
import pickle

joblib.load("model")
loaded_model = pickle.load(open("model", 'rb'))
