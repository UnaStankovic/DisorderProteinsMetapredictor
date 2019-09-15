import matplotlib.pyplot as plt

def consensus_treshold(cons, treshold=0.5):
    new = []
    print(treshold)
    for c in cons:
        if c >= treshold:
            new.append(1)
        else:
            new.append(0)
    return new

def plot_consensus(score, sequence):
    plt.plot([i for i in range(len(sequence))], score)
    plt.xlabel('Position in sequence')
    plt.ylabel('Score')
    plt.axhline(y=0.5, color='r', linestyle='-')
    plt.savefig('predicted.png')
    plt.clf()
    return 


def consensus(sequence, predictors):
    num_of_preds = len(predictors)
    score = []
    for i in range(0, len(sequence)):
        val = 0
        for pred in predictors:
            if pred[i] == 'D':
                val += 1
        score.insert(i, val / num_of_preds)
    plot_consensus(score, sequence)
    return score
