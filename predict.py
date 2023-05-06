import random
import pickle

def predict(model, current):
    if current not in model:
        # 이전 문자열이 모델에 없을 경우, 임의의 문자열 반환
        return random.choice(list(model.keys()))[0]
    # 이전 문자열이 모델에 있을 경우, 다음 문자열 예측
    next_chars = model[current]
    total = sum(next_chars.values())
    probabilities = {k: v/total for k, v in next_chars.items()}
    return random.choices(list(probabilities.keys()), list(probabilities.values()))[0]

with open('model/model_1.pkl', 'rb') as f:
    model_1 = pickle.load(f)
with open('model/model_2.pkl', 'rb') as f:
    model_2 = pickle.load(f)
with open('model/model_3.pkl', 'rb') as f:
    model_3 = pickle.load(f)

# print(model_3)

# 테스트
current = input('문자 입력: ')
print('입력된 문자:', current)
print('1개로 예측된 후행 문자:', predict(model_1, current[-1:]))
print('2개로 예측된 후행 문자:', predict(model_2, current[-2:]))
print('3개로 예측된 후행 문자:', predict(model_3, current[-3:]))
