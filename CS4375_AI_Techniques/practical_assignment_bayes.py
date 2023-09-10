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

"""

class Bayes:
    def __init__(self, hypotheses, priors, observations, likelihood_array):
        
        self.hypotheses = hypotheses # List of hypothesis
        self.priors = priors  # List of prior probabilities for each hypothesis
        self.observations = observations  # List of possible observations
        self.likelihood_array = likelihood_array # Likelihood array
    
    def likelihood(self, observation, hypothesis):
        # From Likelihood Table get the index of observation and Hypothesis
        hypothesis_index = self.hypotheses.index(hypothesis);
        observation_index = self.observations.index(observation);
        
        return self.likelihood_array[hypothesis_index][observation_index];
    
    def norm_constant(self, observation):
        '''
        
        Given The Bayes Rule, Normalizaiton constant is sum of Likelihood and priors (Read bayes Theorm)
        
        '''
        
        # Enumerate over the priors and Likelihood
        # perform sum over index => (prior[index] * likelihhod[i])
        norm_constant_value = 0;
        for index, element in enumerate(self.hypotheses):
            norm_constant_value += self.priors[index] * self.likelihood(observation, element)
        
        return norm_constant_value;
    
    def single_posterior_update(self, observation, priors):
        norm_constant =  self.norm_constant(observation);
        # Storage for the posterior probabilities for each hypothesis
        posteriors = []
        for index, hypothesis in enumerate(self.hypotheses):
            likelihood = self.likelihood(observation, hypothesis);
            posterior = (priors[index] * likelihood) / norm_constant;
            posteriors.append(posterior);     
        return posteriors;
            
hypothesis = ["bowl1", "bowl2"]
priors = [0.5, 0.5]
observations = ["chocolate", "vanilla"]


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
    [0.9, 0.1,],
    [0.5, 0.5,],
]

bayes_model = Bayes(hypothesis, priors, observations, likelihood_array)
#print(bayes_model.likelihood('vanilla', 'bowl1'));
#print(bayes_model.norm_constant('vanilla'));
print(bayes_model.single_posterior_update('vanilla', [0.8, 0.2]));













