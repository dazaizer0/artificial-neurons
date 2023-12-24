from amadeus import aLib as al, aData as ad

bias_b = 6
accuracy_d = 0.01
outcome_a = 0

xtrain: list = []
answers: list = []

if __name__ == '__main__':
    ad.GEN_2VAL_LISTS_ANSWERS(1000, xtrain, answers)
    print(xtrain)
    print(answers)

    neuron_w = [-2, 0.1]
    n1 = al.NeuronModule([1, 0], neuron_w, False, True)
    mode = al.Mode(False, 0, outcome_a, n1.nreturn)

    for i in range(0, len(xtrain)):
        n1 = al.NeuronModule(xtrain[i], neuron_w, bool(answers[i]), not bool(answers[i]))
        n1.TRAIN_NEURON(outcome_a, bias_b, accuracy_d, mode)
        neuron_w = n1.w
        