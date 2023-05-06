import random

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

def predict(model, current):
    if current not in model:
        # 이전 문자열이 모델에 없을 경우, 임의의 문자열 반환
        print('not in')
        return random.choice(list(model.keys()))
    # 이전 문자열이 모델에 있을 경우, 다음 문자열 예측
    next_chars = model[current]
    total = sum(next_chars.values())
    probabilities = {k: v/total for k, v in next_chars.items()}
    return random.choices(list(probabilities.keys()), list(probabilities.values()))[0]

model_1 = create_markov_model(data, 1)
model_2 = create_markov_model(data, 2)
model_3 = create_markov_model(data, 3)

# 테스트
current = "강아지"
print('입력된 문자:', current)
print('1개로 예측된 후행 문자:', predict(model_1, current[-1:]))
print('2개로 예측된 후행 문자:', predict(model_2, current[-2:]))
print('3개로 예측된 후행 문자:', predict(model_3, current[-3:]))
