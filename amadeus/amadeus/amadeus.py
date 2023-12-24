from ailib import AILib as ai
from ailib import AIData as aid

bias_b = 6
accuracy_d = 0.01
outcome_a = 0

xtrain: list = []
answers: list = []

if __name__ == '__main__':
    aid.GEN_2VAL_LISTS_ANSWERS(1000, xtrain, answers)
    print(xtrain)
    print(answers)

    neuron_w = [-2, 0.1]
    n1 = ai.NeuronModule([1, 0], neuron_w, False, True)
    mode = ai.Mode(False, 0, outcome_a, n1.nreturn)

    for i in range(0, len(xtrain)):
        n1 = ai.NeuronModule(xtrain[i], neuron_w, bool(answers[i]), not bool(answers[i]))
        n1.TRAIN_NEURON(outcome_a, bias_b, accuracy_d, mode)
        neuron_w = n1.w

    COM = ""
    while COM != "end":
        print("com | com = any = start, com = end = end")
        COM = input("com :: ")
        if COM == "end":
            break
        else:
            X1 = float(input("x1 [o-y][mm]: "))
            X2 = float(input("x2 [o-x][mm]: "))
            TEMP_X = [X1, X2]

            n2 = ai.NeuronModule([X1, X2], n1.w, False, not False)
            print(n1)

            a_Result = n2.ACTIVATE(bias_b)

            # ai.LOG_OTHER(TEMP_X, n1.w, bias_b, a_Result, False, not False, 'data/aidata.txt')

            if a_Result > 0:
                print(f'False / RING, A: {a_Result}')
            else:
                print(f'True / PEN, A: {a_Result}')