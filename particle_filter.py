import numpy as np
from numpy.random import uniform

# number of particles
# TODO set/scale
N = 50

# vector of state samples
def ParticleFilter:
    particles

# generate particles - randomly sample from transition model a collection of particles representing initial belief
def particle_init(belief_states, T):
    for i in range(N):
        # sample a state
        # TODO adjust range of distribution sampling from... make it a variable
        ParticleFilter.particles[i] = uniform(0, 100)

def update_filter():
    # update particles using transition model
    states = []
    # update weights using observation model
    # create distribution over discrete sets based on above particles and their weights
    # create new particles by sampling from distribution above (setting particles in ParticleFilter)

