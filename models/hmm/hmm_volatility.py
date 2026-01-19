from hmmlearn.hmm import GaussianHMM
import numpy as np


class HMMVolatilityModel:
    def __init__(self, params: dict):
        self.params = params
        self.model = GaussianHMM(
            n_components=params.get("n_states", 2),
            covariance_type=params.get("covariance_type", "full"),
            n_iter=200,
        )
        self.fitted_ = False

    def fit(self, series):
        """Fit HMM to returns or volatility proxy."""
        X = np.array(series).reshape(-1, 1)
        self.model.fit(X)
        self.fitted_ = True
        return self

    def regime_probabilities(self, series):
        """Return smoothed regime probabilities."""
        X = np.array(series).reshape(-1, 1)
        _, posteriors = self.model.score_samples(X)
        return posteriors
