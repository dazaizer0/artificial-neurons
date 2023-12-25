import sys
sys.path.append('alib')
from alib import aLib as al, aData as ad, aRandom as ar
import random

# Setup variables
bias_b = random.randint(0, 10)
accuracy_d = 0.01
outcome_a = 0

xtrain: list = []
answers: list = []

train_amount = 1000

# Main
if __name__ == '__main__':
    try:
        # Generate data to train
        ad.GEN_2VAL_LISTS_ANSWERS(train_amount, xtrain, answers)

        # Print generated data
        print(f'Random variabled generated for training: -> {xtrain} <-')
        print(f'Answers generated to random variables: -> {answers} <-\n')

        # Setup neuron's properties
        neuron_w = [random.randint(-5, 5), random.randint(-5, 5)]
        n1 = al.NeuronModule([1, 0], neuron_w, False, True) # x1[] = y, x2[] = x
        # Setup training mode
        mode = al.Mode(False, 0, outcome_a, n1.nreturn)

        # Train neurons by TRAIN_NEURON function
        for i in range(0, len(xtrain)):
            n1 = al.NeuronModule(xtrain[i], neuron_w, bool(answers[i]), not bool(answers[i]))
            n1.TRAIN_NEURON(outcome_a, bias_b, accuracy_d, mode)
            neuron_w = n1.w

        # Print the number of training sessions performed
        print(f'\nTests were carried out on -> {train_amount} <- modules')
        print(f'-> The module was trained properly. <-')
    except Exception as e:
        print(f"An error occurred while training the neuron: -> {e} <-")
