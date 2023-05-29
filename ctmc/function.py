import numpy as np

transition_probabilities = {
    '납부': {
        '납부': 0.7521358828315704,
        '일부 납부': 0.048616761594792515,
        '연체': 0.1992473555736371
    },
    '일부 납부': {
        '납부': 0.038334392879847426,
        '일부 납부': 0.9064844246662428,
        '연체': 0.055181182453909725
    },
    '연체': {
        '납부': 0.1007210455159982,
        '일부 납부': 0.0,
        '연체': 0.8992789544840019
    }
}

interarrival_times = {
    '납부': 1 / 0.2478641171684296,
    '일부 납부': 1 / 0.0935155753337572,
    '연체': 1 / 0.10072104551599814
}

def transition_probability(state_i, state_j, t):
    prob = 0
    for state in transition_probabilities:
        prob += transition_probabilities[state_i][state] * np.exp(-interarrival_times[state] * t) * transition_probabilities[state][state_j]
    return prob

# Example usage
t = 1
prob = transition_probability('납부', '납부', t)
print(f"P('납부' -> '납부') at t={t}: {prob}")
