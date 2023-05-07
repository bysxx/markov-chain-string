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

with open('model/model_3.pkl', 'rb') as f:
    model_3 = pickle.load(f)

# 테스트
current = input('문자 입력: ')
print('입력된 문자:', current)
sententce_len = int(input('문장 길이 입력: '))

for i in range(sententce_len):
    current += predict(model_3, current[-3:])

print('생성된 문장:', current)