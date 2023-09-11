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
    def __init__(self, hypotheses: List[str], priors: List[float], observations: List[str], likelihood_array: List[List[float]]) -> None:
        
        self.hypotheses = hypotheses # List of hypothesis
        self.priors = priors  # List of prior probabilities for each hypothesis
        self.observations = observations  # List of possible observations
        self.likelihood_array = likelihood_array # Likelihood array
    
    def likelihood(self, observation: str, hypothesis: str) -> float:
        # From Likelihood Table get the index of observation and Hypothesis
        hypothesis_index = self.hypotheses.index(hypothesis);
        observation_index = self.observations.index(observation);
        
        return self.likelihood_array[hypothesis_index][observation_index];
    
    def norm_constant(self, observation: str) -> float:
        '''
        
        Given The Bayes Rule, Normalizaiton constant is sum of Likelihood and priors (Read bayes Theorm)
        
        '''
        
        # Enumerate over the priors and Likelihood
        # perform sum over index => (prior[index] * likelihhod[i])
        norm_constant_value = 0;
        for index, element in enumerate(self.hypotheses):
            norm_constant_value += self.priors[index] * self.likelihood(observation, element)
        
        return norm_constant_value;
    
    def single_posterior_update(self, observation, priors) -> List[float]:
        norm_constant =  self.norm_constant(observation);
        # Storage for the posterior probabilities for each hypothesis
        posteriors = []
        for index, hypothesis in enumerate(self.hypotheses):
            likelihood = self.likelihood(observation, hypothesis);
            posterior = (priors[index] * likelihood) / norm_constant;
            posteriors.append(posterior);     
        return posteriors;
    

    def compute_posterior(self, observations: List[str]) -> List[float]:
        
        posteriors = self.priors;
        for index, observation in enumerate(observations):
            posteriors = self.single_posterior_update(observation, posteriors);
        
        return posteriors;
    

import unittest

class TestBayes(unittest.TestCase):
    def setUp(self):
        # Define test data for Bayes instance
        self.hypotheses = ["HypothesisA", "HypothesisB"]
        self.priors = [0.4, 0.6]
        self.observations = ["Observation1", "Observation2"]
        self.likelihood_array = [
            [0.2, 0.8],
            [0.7, 0.3]
        ]

        self.bayes_model = Bayes(self.hypotheses, self.priors, self.observations, self.likelihood_array)

    def test_likelihood(self):
        self.assertAlmostEqual(self.bayes_model.likelihood("Observation1", "HypothesisA"), 0.2)
        self.assertAlmostEqual(self.bayes_model.likelihood("Observation2", "HypothesisB"), 0.3)

    
    def test_norm_constant(self):
        observation = "Observation1";
        norm_constant = self.bayes_model.norm_constant(observation)
        self.assertAlmostEqual(norm_constant, 0.38)

            
    def test_single_posterior_update(self):
        observation = "Observation1"
        priors = self.bayes_model.priors
        posteriors = self.bayes_model.single_posterior_update(observation, priors)
        expected_posteriors = [0.11764705882352941, 0.8823529411764706]
        tolerance = 0.001
        for a, b in zip(posteriors, expected_posteriors):
            self.assertAlmostEqual(a, b, delta=tolerance)

    def test_compute_posterior(self):
        observations = ["Observation1", "Observation2"]
        posteriors = self.bayes_model.compute_posterior(observations)
        expected_posteriors = [0.11764705882352941, 0.8823529411764706]
        tolerance = 0.001
        for a, b in zip(posteriors, expected_posteriors):
            self.assertAlmostEqual(a, b, delta=tolerance)

def assignmentMain():
    hypothesis = ["Bowl1", "Bowl2"]
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
        [15/50, 35/50,],
        [30/50, 20/50,],
    ]
    
    bayes_model = Bayes(hypothesis, priors, observations, likelihood_array)
    print("likelihood(chocolate, Bowl1) =", bayes_model.likelihood('vanilla', 'Bowl1'))
    print("normalizing constant for vanilla: ", bayes_model.norm_constant('vanilla'));
    print("vanilla - posterior: ", bayes_model.single_posterior_update('vanilla', [0.8, 0.2]));
    print("'vanilla', 'chocolate', 'chocolate', 'vanilla' - postereior ", bayes_model.compute_posterior(['vanilla', 'chocolate', 'chocolate', 'vanilla']));


if __name__ == '__main__':
    
    unittest.main();
    assignmentMain();
            
    
    

    
    













