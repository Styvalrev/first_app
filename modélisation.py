import joblib
joblib.dump(clf, "model")

import pickle
pickle.dump(clf, open("model", 'wb'))