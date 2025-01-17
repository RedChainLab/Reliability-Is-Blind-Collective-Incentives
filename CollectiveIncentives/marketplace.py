import numpy as np
import random

N_ACTORS_INITIAL = 100  # Initial number of assets
N_MAX_ACTORS = N_ACTORS_INITIAL # Maximum number of assets
N_MIN_ACTORS_TASK = 4  # Number of maximum assets for each task
N_MAX_ACTORS_TASK = 4  # Number of maximum assets for each task
S0 = 10  # Initial capital of each actor
N_TASKS = 10000  # Number of tasks to simulate
SLASH_AMOUNT = 1  # Amount slashed for failed tasks
TARGET_TASK_FAILURE_RATE = 0.05  # Target failure rate for each task
REWARD_AMOUNT = TARGET_TASK_FAILURE_RATE/(1-TARGET_TASK_FAILURE_RATE)  # Reward for successful tasks
NEW_ACTOR_INTERVAL = 500  # Frequency of new actor addition (in tasks)
NEW_ACTOR_FAULTY_COMBOS = 0  # Number of faulty combinations per new actor
MONTE_CARLO_RUNS = 50  # Number of Monte Carlo simulations

# Initialize assets and faulty sets
class Actor:
    def __init__(self, id, stake, failure_rate):
        self.id = id
        self.stake = stake
        self.failure_rate = failure_rate
        self.loss = 0
        self.reward = 0
        self.nb_tasks = 0

class FaultySet:
    def __init__(self, assets, p_fail):
        self.assets = assets
        self.p_fail = p_fail

# Add an actor with a faulty set
def add_actor(assets, faulty_sets, p_fail_distribution):
    # Add a new actor
    new_actor = Actor(len(assets), S0, generate_p_fail(p_fail_distribution))
    assets.append(new_actor)

    # Generate a faulty set for the new actor
    faulty_set = FaultySet([new_actor], new_actor.failure_rate)
    faulty_sets.append(faulty_set)
    new_actor.failure_rate = faulty_set.p_fail
    
    # Generate faulty combinations sets for the new actor
    generate_faulty_combinations(new_actor, assets, faulty_sets, p_fail_distribution)

# Generate initial faulty sets
def generate_faulty_combinations(actor, assets, faulty_sets, p_fail_distribution):
    for _ in range(NEW_ACTOR_FAULTY_COMBOS):
        subset_size = random.randint(N_MIN_ACTORS_TASK, N_MAX_ACTORS_TASK-1)
        subset = random.sample(assets, subset_size)
        subset.append(actor)
        p_fail = generate_p_fail(p_fail_distribution)
        faulty_sets.append(FaultySet(subset, p_fail))

# Generate p_fail based on long tail distribution
def generate_p_fail(p_fail_distribution):
    p_fail = np.random.choice(p_fail_distribution)
    while p_fail < 0 or p_fail > 1:
        p_fail = np.random.choice(p_fail_distribution)
    # return max(0, min(1, np.random.choice(p_fail_distribution)))
    return p_fail

# Bins setup for failure rates
def get_failure_rate_bin(p_fail, bin_size=0.05):
    return round(min(max(p_fail, 0), 1) // bin_size * bin_size, 2)

# Function to compute average reward and loss per failure rate bin
def compute_average_reward_and_loss(assets, removed_assets, faulty_sets):
    reward_bins = {round(i * 0.05, 2): [] for i in range(20)}  # Bins of 0.05
    loss_bins = {round(i * 0.05, 2): [] for i in range(20)}    # Bins of 0.05

    # Iterate through all assets
    for actor in assets:
        if actor.nb_tasks == 0:
            continue
        
        bin_key = get_failure_rate_bin(actor.failure_rate)
        
        # Add actor's reward and loss to the corresponding bin
        reward_bins[bin_key].append(actor.reward / actor.nb_tasks)
        loss_bins[bin_key].append(actor.loss / actor.nb_tasks)

    for actor in removed_assets:
        if actor.nb_tasks == 0:
            continue

        bin_key = get_failure_rate_bin(actor.failure_rate)
        
        # Add actor's reward and loss to the corresponding bin
        reward_bins[bin_key].append(actor.reward / actor.nb_tasks)
        loss_bins[bin_key].append(actor.loss / actor.nb_tasks)

    # Compute the averages for each bin
    average_rewards_per_bin = {bin_key: np.mean(values) if values else 0 for bin_key, values in reward_bins.items()}
    average_losses_per_bin = {bin_key: np.mean(values) if values else 0 for bin_key, values in loss_bins.items()}

    return average_rewards_per_bin, average_losses_per_bin