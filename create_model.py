import random
import pickle

# 데이터셋
with open('data.txt', 'r') as f:
    data = f.readline()

print('데이터셋 크기:', len(data))

def create_markov_model(data, order):
    model = {}
    for i in range(len(data)-order):
        # 현재 문자와 이전 문자열을 키(key)로 사용하여 딕셔너리에 저장
        current = data[i:i+order]
        next_char = data[i+order]
        if current not in model:
            model[current] = {}
        if next_char not in model[current]:
            model[current][next_char] = 0
        model[current][next_char] += 1
    return model

model_1 = create_markov_model(data, 1)
model_2 = create_markov_model(data, 2)
model_3 = create_markov_model(data, 3)

with open('model/model_1.pkl', 'wb') as f:
    pickle.dump(model_1, f)
with open('model/model_2.pkl', 'wb') as f:
    pickle.dump(model_2, f)
with open('model/model_3.pkl', 'wb') as f:
    pickle.dump(model_3, f)