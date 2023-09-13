# -*- coding: utf-8 -*-
"""
Tasks:
    1. Write a class Bayes that takes as initialization arguments the following: a list of hypothesis,
a list with the priors of the hypothesis, a list of possible observations and a likelihood array. 

    2. In Bayes write a function likelihood that takes as arguments an observation (e.g. "vanilla")
and an hypothesis (e.g. "Bowl 1") and returns the likelihood.

    3. In Bayes write a function norm_constant that takes as input an observation and returns
the normalizing constant.

    4. In Bayes write a function single_posterior_update that takes as input an observation and
priors and returns the posterior probabilities.

    5.  In Bayes write a function compute_posterior that takes as input a list of observations and
returns the posterior probabilities.

"""

from typing import List


class Bayes:
    def __init__(self, hypotheses: List[str], priors: List[float], observations: List[str],
                 likelihood_array: List[List[float]]) -> None:

        self.hypotheses = hypotheses  # List of hypothesis
        self.priors = priors  # List of prior probabilities for each hypothesis
        self.observations = observations  # List of possible observations
        self.likelihood_array = likelihood_array  # Likelihood array

    def likelihood(self, observation: str, hypothesis: str) -> float:
        # From Likelihood Table get the index of observation and Hypothesis
        hypothesis_index = self.hypotheses.index(hypothesis)
        observation_index = self.observations.index(observation)

        return self.likelihood_array[hypothesis_index][observation_index]

    def norm_constant(self, observation: str) -> float:
        """

        Given The Bayes Rule, Normalization constant is sum of Likelihood and priors (Read bayes Theorem)

        """

        # Enumerate over the priors and Likelihood
        # perform sum over index => (prior[index] * likelihood[i])
        norm_constant_value = 0
        for index, element in enumerate(self.hypotheses):
            norm_constant_value += self.priors[index] * self.likelihood(observation, element)

        return norm_constant_value

    def single_posterior_update(self, observation) -> List[float]:
        norm_constant = self.norm_constant(observation)
        # Storage for the posterior probabilities for each hypothesis
        posteriors = []
        for index, hypothesis in enumerate(self.hypotheses):
            likelihood = self.likelihood(observation, hypothesis)
            posterior = (self.priors[index] * likelihood) / norm_constant
            posteriors.append(posterior)
        self.priors = posteriors
        return posteriors

    def compute_posterior(self, observations: List[str]) -> List[float]:
        result = []
        for index, observation in enumerate(observations):
            result = self.single_posterior_update(observation)
        return result



def assignment_main():
    hypothesis = ["Bowl1", "Bowl2"]
    priors = [0.5, 0.5]
    observations = ["chocolate", "vanilla"]

    new_file = open("./results.txt", mode="w")
    new_file.write("Cookie example Bayes: \n\n")

    '''
    The likelihood array in Bayesian inference represents the conditional
        probabilities of observing various pieces of evidence (observations) 
        given each possible hypothesis.
     
    '''

    '''
    
    Likelihood Array:
                 | Chocolate | Vanilla |
    ------------------------------------
    Bowl 1       |   0.9     |   0.1   |
    Bowl 2       |   0.5     |   0.5   |
    
    '''
    likelihood_array = [
        [15 / 50, 35 / 50, ],
        [30 / 50, 20 / 50, ],
    ]

    bayes_model = Bayes(hypothesis, priors, observations, likelihood_array)
    ce2_result = bayes_model.likelihood('vanilla', 'Bowl1')
    new_file.write("likelihood(chocolate, Bowl1) =" + str(ce2_result) + "\n")
    ce3_result = bayes_model.norm_constant('vanilla')
    new_file.write("normalizing constant for vanilla: " + str(ce3_result) + "\n")
    ce4_result = bayes_model.single_posterior_update('vanilla')
    new_file.write("vanilla - posterior: " + str(ce4_result) + "\n")

    # incorrect way of representation in assignment, this prior can be changed in the code and the norm_constant will
    # still use priors defined during the class creation
    ce5_result = bayes_model.compute_posterior(['vanilla', 'chocolate', 'chocolate', 'vanilla'])
    new_file.write("'vanilla', 'chocolate', 'chocolate', 'vanilla' - posterior " + str(ce5_result) + "\n")

    new_file.close()




def predict_archer_skills():
    existing_file = open('./results.txt', mode="a")
    existing_file.write('\n\nArches Skills Inference: \n\n')
    observations = ["yellow", "white", "blue", "red", "red", "blue"]
    hypotheses: List[str] = ['beginner', 'intermediate', 'advanced', 'expert']
    priors: List[float] = [0.25, 0.25, 0.25, 0.25]
    likelihood_array: List[List[float]] = [[0.05, 0.1, 0.4, 0.25, 0.2],
                                           [0.1, 0.2, 0.4, 0.2, 0.1],
                                           [0.2, 0.4, 0.25, 0.1, 0.05],
                                           [0.3, 0.5, 0.125, 0.05, 0.025]]
    bayes_model_archer = Bayes(hypotheses, priors, observations, likelihood_array)
    ce6_result = bayes_model_archer.compute_posterior(observations)
    existing_file.write("All Posteriors: " + str(ce6_result) + "\n")
    ce7_result = bayes_model_archer.compute_posterior(observations)[1]
    existing_file.write("Probability That Archer is Intermediate: " + str(ce7_result) + '\n')

    # clean up resourcess
    existing_file.close()
    # Calculate P()


if __name__ == '__main__':
    print("********* Running Assigment Demo Questions *********")
    assignment_main()
    print("********* Assigment Demo Questions Ended *********")
    print("********* Running Archer Problem *********")
    predict_archer_skills()
    print("********* Archer Problem Ended*********")