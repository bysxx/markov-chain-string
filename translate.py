import pickle
import json

with open('model/model_3.pkl', 'rb') as f:
    data = pickle.load(f)

with open('model_3.json', 'w') as f:
    json.dump(data, f)