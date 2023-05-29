import pandas as pd

# 데이터 로드 및 필요한 열 선택
data = pd.read_csv("credit.csv")

def preprocess_pay_values(value):
    if value <= -1:  # -2를 -1로 변환
        return -1
    elif value >=1:
        return 1
    else:  
        return 0

# PAY_0, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6 열에 대해 변환 함수 적용
data['PAY_1'] = data['PAY_1'].apply(preprocess_pay_values)
data['PAY_2'] = data['PAY_2'].apply(preprocess_pay_values)
data['PAY_3'] = data['PAY_3'].apply(preprocess_pay_values)
data['PAY_4'] = data['PAY_4'].apply(preprocess_pay_values)
data['PAY_5'] = data['PAY_5'].apply(preprocess_pay_values)
data['PAY_6'] = data['PAY_6'].apply(preprocess_pay_values)

# 위는 전처리

data = data[['PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6']]

# 전이 확률 계산
transition_counts = {
    "-1": {
        "-1": ((data['PAY_2'] == -1) & (data['PAY_1'] == -1)).sum(),
        "0": ((data['PAY_2'] == -1) & (data['PAY_1'] == 0)).sum(),
        "1": ((data['PAY_2'] == -1) & (data['PAY_1'] == 1)).sum(),
    },
    "0": {
        "-1": ((data['PAY_2'] == 0) & (data['PAY_1'] == -1)).sum(),
        "0": ((data['PAY_2'] == 0) & (data['PAY_1'] == 0)).sum(),
        "1": ((data['PAY_2'] == 0) & (data['PAY_1'] == 1)).sum(),
    },
    "1": {
        "-1": ((data['PAY_2'] == 1) & (data['PAY_1'] == -1)).sum(),
        "0": ((data['PAY_2'] == 1) & (data['PAY_1'] == 0)).sum(),
        "1": ((data['PAY_2'] == 1) & (data['PAY_1'] == 1)).sum(),
    }
}

transition_probabilities = {}

transition_probabilities["납부 -> 납부"] = transition_counts["-1"]["-1"] / (transition_counts["-1"]["-1"] + transition_counts["-1"]["0"] + transition_counts["-1"]["1"])
transition_probabilities["납부 -> 일부 납부"] = transition_counts["-1"]["0"] / (transition_counts["-1"]["-1"] + transition_counts["-1"]["0"] + transition_counts["-1"]["1"])
transition_probabilities["납부 -> 연체"] = transition_counts["-1"]["1"] / (transition_counts["-1"]["-1"] + transition_counts["-1"]["0"] + transition_counts["-1"]["1"])

transition_probabilities["일부 납부 -> 납부"] = transition_counts["0"]["-1"] / (transition_counts["0"]["-1"] + transition_counts["0"]["0"] + transition_counts["0"]["1"])
transition_probabilities["일부 납부 -> 일부 납부"] = transition_counts["0"]["0"] / (transition_counts["0"]["-1"] + transition_counts["0"]["0"] + transition_counts["0"]["1"])
transition_probabilities["일부 납부 -> 연체"] = transition_counts["0"]["1"] / (transition_counts["0"]["-1"] + transition_counts["0"]["0"] + transition_counts["0"]["1"])

transition_probabilities["연체 -> 납부"] = transition_counts["1"]["-1"] / (transition_counts["1"]["-1"] + transition_counts["1"]["0"] + transition_counts["1"]["1"])
transition_probabilities["연체 -> 일부 납부"] = transition_counts["1"]["0"] / (transition_counts["1"]["-1"] + transition_counts["1"]["0"] + transition_counts["1"]["1"])
transition_probabilities["연체 -> 연체"] = transition_counts["1"]["1"] / (transition_counts["1"]["-1"] + transition_counts["1"]["0"] + transition_counts["1"]["1"])

print("전이 확률:", transition_probabilities)

v = {}
v["납부"] = (1 - transition_probabilities["납부 -> 납부"])
v["일부 납부"] = (1 - transition_probabilities["일부 납부 -> 일부 납부"])
v["연체"] = (1 - transition_probabilities["연체 -> 연체"])

print("v:", v)

instantaneous_transition_rates = {}
instantaneous_transition_rates["납부 -> 일부 납부"] = transition_probabilities["납부 -> 일부 납부"] * v["납부"]
instantaneous_transition_rates["납부 -> 연체"] = transition_probabilities["납부 -> 연체"] * v["납부"]

instantaneous_transition_rates["일부 납부 -> 납부"] = transition_probabilities["일부 납부 -> 납부"] * v["일부 납부"]
instantaneous_transition_rates["일부 납부 -> 연체"] = transition_probabilities["일부 납부 -> 연체"] * v["일부 납부"]

instantaneous_transition_rates["연체 -> 납부"] = transition_probabilities["연체 -> 납부"] * v["연체"]
instantaneous_transition_rates["연체 -> 일부 납부"] = transition_probabilities["연체 -> 일부 납부"] * v["연체"]

print(instantaneous_transition_rates)