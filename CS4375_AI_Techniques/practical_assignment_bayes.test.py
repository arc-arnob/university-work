import unittest
from practical_assignment_bayes import Bayes


class TestBayes(unittest.TestCase):
    def setUp(self):
        # Define test data for Bayes instance
        self.hypotheses = ["Bowl1", "Bowl2"]
        self.priors = [0.5, 0.5]
        self.observations = ["chocolate", "vanilla"]
        self.likelihood_array = [
            [15 / 50, 35 / 50],
            [30 / 50, 20 / 50],
        ]

        self.bayes_model = Bayes(self.hypotheses, self.priors, self.observations, self.likelihood_array)

    def test_likelihood(self):
        self.assertAlmostEqual(self.bayes_model.likelihood("vanilla", "Bowl1"), 0.7)
        self.assertAlmostEqual(self.bayes_model.likelihood("chocolate", "Bowl2"), 0.6)

    def test_norm_constant(self):
        observation = "chocolate"
        norm_constant = self.bayes_model.norm_constant(observation)
        self.assertAlmostEqual(norm_constant, 0.45)

    def test_single_posterior_update(self):
        observation = "chocolate"
        posteriors = self.bayes_model.single_posterior_update(observation)
        expected_posteriors = [0.334, 0.667]
        tolerance = 0.01
        for a, b in zip(posteriors, expected_posteriors):
            self.assertAlmostEqual(a, b, delta=tolerance)

    def test_compute_posterior(self):
        observations = ["chocolate", "vanilla"]
        posteriors = self.bayes_model.compute_posterior(observations)
        expected_posteriors = [0.4667, 0.5333]
        tolerance = 0.001
        for a, b in zip(posteriors, expected_posteriors):
            self.assertAlmostEqual(a, b, delta=tolerance)



unittest.main()
