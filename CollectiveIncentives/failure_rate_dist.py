import random
import numpy as np
from scipy.stats import powerlaw
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor as pool
import sys
from functools import partial
from datetime import datetime
import matplotlib.ticker as mtick

params = {'text.usetex' : True,
          'font.size' : 10,
            'font.family' : 'serif',
            'font.serif' : 'Computer Modern Roman',
          }
plt.rcParams.update(params) 

FIG_DIR="out/fig"

N_ACTORS_INITIAL = 100  # Initial number of actors
N_MAX_ACTORS = N_ACTORS_INITIAL # Maximum number of actors
N_MIN_ACTORS_TASK = 4  # Number of maximum actors for each task
N_MAX_ACTORS_TASK = 4  # Number of maximum actors for each task
S0 = 4000  # Initial capital of each actor
N_TASKS = 10000  # Number of tasks to simulate
SLASH_AMOUNT = 400  # Amount slashed for failed tasks
REWARD_AMOUNT = 25  # Reward for successful tasks
NEW_ACTOR_INTERVAL = 500  # Frequency of new actor addition (in tasks)
NEW_ACTOR_FAULTY_COMBOS = 0  # Number of faulty combinations per new actor
MONTE_CARLO_RUNS = 50  # Number of Monte Carlo simulations

# Display
X_MAX = 0.50
Y_MAX = (N_ACTORS_INITIAL + N_TASKS//NEW_ACTOR_INTERVAL) // 10

# Calculate the failure rate target
failure_rate_target = REWARD_AMOUNT / (REWARD_AMOUNT + SLASH_AMOUNT)
individual_failure_rate_target = 1 - (1 - failure_rate_target) ** (1 / N_MAX_ACTORS_TASK)

plt.figure(figsize=(4.5,2))

alphas=[0.1,0.05, 0.01]
colors = ['blue', 'green', 'red']
for alpha, color in zip(alphas,colors):
    p_fail_distribution = powerlaw.rvs(alpha, size=100000)
    mean_fail_rate = np.mean(p_fail_distribution)
    print(f"Mean failure rate: {mean_fail_rate}")

    # Plotting test distribution
    plt.hist(p_fail_distribution, bins=100, density=True, cumulative=True, label=f"$\\alpha = {alpha}$", histtype="step", color=color)
    plt.axvline(mean_fail_rate, color=color, linestyle='--', label="mean($F_a$)", linewidth=0.7)
# plt.axvline(individual_failure_rate_target, color='black', linestyle='--', label="Mean failure rate")
# plt.yscale('log')
plt.xlabel("Failure rate $F_a$")
plt.xticks(np.arange(0, 1.01, 0.1))
plt.xticks(np.arange(0, 1.01, 0.05),minor=True)
plt.ylabel("Cumulative probability")
plt.yticks(np.arange(0, 1.01, 0.2))
plt.yticks(np.arange(0, 1.01, 0.05),minor=True)  
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1))
plt.grid()
plt.xlim(-0.02, 1)
plt.ylim(0, 1)
plt.legend(loc="center right",
            #   bbox_to_anchor=(0.95, 0.5), 
           handletextpad=0.25, 
           labelspacing=0.2, fontsize="small", framealpha=0.7)
plt.tight_layout()
current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
plt.savefig(f"{FIG_DIR}/failure_rate_distribution-{current_time}.pdf", bbox_inches ="tight", dpi=1200)