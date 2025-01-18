import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor as pool
import sys
from functools import partial

params = {'text.usetex' : True,
          'font.size' : 10,
            'font.family' : 'serif',
            'font.serif' : 'Computer Modern Roman',
          }
plt.rcParams.update(params) 

FIG_DIR="out/fig"

# Parameters
mean_claim = 1          # P: Mean size of claims
claim_std_dev = 0       # Standard deviation of claims
mean_premium = 0.25     # R: Mean size of premiums
premium_std_dev = 0     # Standard deviation of premiums
time_periods = 1000     # N_{t}: Number of time periods to simulate
num_simulations = 1000  # Number of simulations

# Simulation
# np.random.seed(23)

# Function to perform one simulation of the risk process
def simulate_risk_process(initial_capital, claim_frequency):
    capital_over_time = np.zeros(time_periods)
    capital_over_time[0] = initial_capital

    for t in range(1, time_periods):
        # Number of claims in this period
        num_claims = np.random.poisson(claim_frequency)
        # Total claim amount for this period
        total_claims = np.sum(np.random.normal(mean_claim, claim_std_dev, num_claims))
        # Total premium for this period
        total_premiums = np.random.normal(mean_premium, premium_std_dev)
        # Update capital
        capital_over_time[t] = capital_over_time[t-1] + total_premiums - total_claims

    return capital_over_time


# Loop through different initial capital amounts
def run_simulations(initial_capital, claim_frequency):
    ruin_count = 0  # Counter for number of simulations resulting in ruin
    for _ in range(num_simulations):
        capital_over_time = simulate_risk_process(initial_capital, claim_frequency)
        if np.any(capital_over_time < 0):  # Check if capital goes below zero at any point
            ruin_count += 1
    
    # Probability of ruin
    ruin_probability = ruin_count / num_simulations
    print(f'Claim frequency: {claim_frequency}; Initial Capital = {initial_capital}; Ruin Probability = {ruin_probability:.4f}')
    return ruin_probability

if __name__ == '__main__':
    N_JOBS = int(sys.argv[1]) if len(sys.argv) > 1 else 1

    claim_frequencies= [0.1, 0.15, 0.19, 0.2, 0.21, 0.25, 0.3][::-1] # F_{t}: Task failure / Claim frequency
    initial_capitals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # S_{0}: Different initial stake / capital amounts
    colors=['b', 'g', 'r', 'c', 'm', 'y', 'k']

    min_ruin_prob=1
    fig, ax = plt.subplots(figsize=(3.5,2))
    for claim_frequency, color in zip(claim_frequencies, colors):
        ruin_probabilities = []
        with pool(N_JOBS) as p:
            ruin_probabilities=list(p.map(partial(run_simulations,claim_frequency=claim_frequency), initial_capitals))
        print(f"Claim frequency: {claim_frequency}; Ruin probabilities: {ruin_probabilities}")

        ax.plot(initial_capitals, ruin_probabilities, '+', markersize=7, markeredgewidth=1, label=f'$F_t={int(claim_frequency*100)}\%$', color=color)
        filtered_ruin_probabilities = []
        filtered_initial_capitals = []
        for i in range(len(ruin_probabilities)):
            if ruin_probabilities[i] > 0:
                filtered_ruin_probabilities.append(ruin_probabilities[i])
                filtered_initial_capitals.append(initial_capitals[i])
        coefs = np.polyfit(filtered_initial_capitals, np.log(filtered_ruin_probabilities), 1)
        ax.plot(initial_capitals, np.exp(coefs[1]) * np.exp(coefs[0] * np.array(initial_capitals)), '--', label=f'$e^{{{coefs[0]:.4f}x{"+"if coefs[1]>=0 else ""}{coefs[1]:.4f}}}$', color=color)

        last_non_zero_idx = 0
        for i in range(len(ruin_probabilities)):
            if ruin_probabilities[i] != 0:
                last_non_zero_idx = i
        min_ruin_prob = min(min_ruin_prob, min(filtered_ruin_probabilities))

    ax.set_xlabel('Initial stake/penalty proportion $x$')
    ax.set_ylabel('Probability of ruin')

    ax.grid(True, which="major", linestyle='-')
    ax.set_xticks([x for x in range(0, max(initial_capitals)+1, 1)])
    ax.set_yscale('log')
    ax.set_ylim(min_ruin_prob/10,1)
    box = ax.get_position()
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.45),
                handletextpad=0.25, 
                labelspacing=0.2, fontsize="small", framealpha=0.7)

    current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    fig.savefig(f'{FIG_DIR}/ruin_probabilities-{current_time}.pdf', bbox_inches ="tight", dpi=1200)