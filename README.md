# Learned-Pricing

## Problem
We start with the problem of setting a price for a single good that will be offered to a set of n people each with their own price threshold that determines whether they make a purchase at a given price.
We use a POMDP to model the problem with a discretized state and action space (action is price set and state is each individual's price threshold).
We assume price thresholds don't fluctuate for individuals, so our POMDP has only one state.

## Aproach
We use particle filtering for state estimation, which is helpful for problems with large discrete state spaces, which we may make use of in future iterations expanding the state space to allow for fluctuations in individual's price threshold, which more naturally models consumer behavior and market fluctuations.
