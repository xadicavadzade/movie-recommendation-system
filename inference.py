import pickle
import numpy as np

# model yüklə
with open("catboost_model.pkl", "rb") as f:
    loaded_model = pickle.load(f)

model = pickle.load(open('catboost_model.pkl', 'rb'))

def inference(user_data):
    # Dummy inference functionexit
    return model.predict(user_data)

sample_user_data = [1996, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 197.0, 4.017766]

print(inference(sample_user_data))