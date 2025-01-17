import random
import numpy as np
from scipy.stats import powerlaw
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor as pool
import sys
from functools import partial
from datetime import datetime
import matplotlib.ticker as mtick

from marketplace import *

params = {'text.usetex' : True,
          'font.size' : 10,
            'font.family' : 'serif',
            'font.serif' : 'Computer Modern Roman',
          }
plt.rcParams.update(params) 

N_JOBS = int(sys.argv[1]) if len(sys.argv) > 1 else 1

FIG_DIR="out/fig"

# Display
X_MAX = 0.50
Y_MAX = (N_ACTORS_INITIAL + N_TASKS//NEW_ACTOR_INTERVAL) // 10

# Function to pad a list with zeros up to a target length
def pad_list_with_zeros(lst, target_length):
    return lst + [0] * (target_length - len(lst))

# Function extend list to desired length by repeatinig the last element
def extend_list(lst, target_length):
    return lst + [lst[-1]] * (target_length - len(lst))

# Function to run a single simulation
def run_simulation(faulty_sets, p_fail_distribution):
    
    # Calculate the failure rate target
    failure_rate_target = REWARD_AMOUNT / (REWARD_AMOUNT + SLASH_AMOUNT)
    individual_failure_rate_target = 1 - (1 - failure_rate_target) ** (1 / N_MAX_ACTORS_TASK)

    # Initialize assets and faulty sets
    total_assets = N_ACTORS_INITIAL
    assets = [Actor(i, S0, generate_p_fail(p_fail_distribution)) for i in range(N_ACTORS_INITIAL)]
    all_assets = assets.copy()

    for actor in assets:
        faulty_set = FaultySet([actor], actor.failure_rate)
        actor.failure_rate = faulty_set.p_fail
        faulty_sets.append(faulty_set)

    # Generate faulty combinations for the initial assets
    for actor in assets:
        generate_faulty_combinations(actor, assets, faulty_sets, p_fail_distribution)

    successful_tasks = 0
    failed_tasks = 0
    true_positive = 0
    false_positive = 0
    false_negative = 0

    removed_assets = []
    system_failure_rates = []
    actor_counts = []
    average_failure_rates = []

    # Task simulation loop
    for task_id in range(1, N_TASKS + 1):
        for _ in range(max(0,N_MIN_ACTORS_TASK-len(assets))):
            add_actor(assets, faulty_sets, p_fail_distribution)
            all_assets.append(assets[-1])
            total_assets += 1
        
        # Pick a random subset of assets for the task
        task_assets = random.sample(assets, random.randint(N_MIN_ACTORS_TASK, N_MAX_ACTORS_TASK))
        
        # Check for faulty subsets within the chosen assets
        task_failed = False
        for faulty_set in faulty_sets:
            # Find if faulty set is a subset of task_assets
            if set(faulty_set.assets).issubset(task_assets):
                # Random chance to see if this faulty set triggers a failure
                if random.random() < faulty_set.p_fail:
                    # Task failed, slash all assets involved
                    task_failed = True
                    failed_tasks += 1
                    for actor in task_assets:
                        actor.stake -= SLASH_AMOUNT
                        actor.nb_tasks += 1
                        actor.loss += SLASH_AMOUNT
                    break

        if not task_failed:
            # Task succeeded, reward all assets involved
            successful_tasks += 1
            for actor in task_assets:
                actor.stake += REWARD_AMOUNT
                actor.nb_tasks += 1
                actor.reward += REWARD_AMOUNT
        
        # Remove assets and corresponding faulty sets with zero or negative stake
        to_remove = [actor for actor in assets if actor.stake <= 0]
        removed_assets.extend(to_remove)
        for actor in to_remove:
            removed_failure_rate = [fs.p_fail for fs in faulty_sets if actor in fs.assets and len(fs.assets) == 1]
            if removed_failure_rate and removed_failure_rate[0] > individual_failure_rate_target:
                true_positive += 1
            else:
                false_positive += 1
            assets.remove(actor)
        # faulty_sets = [fs for fs in faulty_sets if all(actor in assets for actor in fs.assets)]

        # Every few tasks, add a new actor and corresponding faulty sets
        if task_id % NEW_ACTOR_INTERVAL == 0 and (N_MAX_ACTORS<=0 or len(assets) < N_MAX_ACTORS):
            add_actor(assets, faulty_sets, p_fail_distribution)
            all_assets.append(assets[-1])
            total_assets += 1
        
        # Track system evolution metrics
        system_failure_rate = failed_tasks / task_id
        average_failure_rate = np.mean([fs.p_fail for fs in faulty_sets])
        
        system_failure_rates.append(system_failure_rate)
        average_failure_rates.append(average_failure_rate)
        actor_counts.append(len(assets))
        print(f"Task {task_id}: System Failure Rate = {system_failure_rate:.4f}; Average Failure Rate = {average_failure_rate:.4f}; Number of assets = {len(assets)}", end='\r')
    
    # Calculate precision, accuracy, and recall
    for faulty_set in faulty_sets:
        if len(faulty_set.assets) == 1 and faulty_set.p_fail > individual_failure_rate_target:
            false_negative += 1

    if true_positive + false_positive != 0:
        precision = true_positive / (true_positive + false_positive)
    accuracy = (true_positive + (len(assets) - false_negative)) / total_assets
    recall = 0
    if true_positive + false_negative != 0:
        recall = true_positive / (true_positive + false_negative)

    return {
        'system_failure_rates': system_failure_rates,
        'average_failure_rates': average_failure_rates,
        'actor_counts': actor_counts,
        'successful_tasks': successful_tasks,
        'failed_tasks': failed_tasks,
        'final_number_of_assets': len(assets),
        'precision': precision,
        'accuracy': accuracy,
        'recall': recall,
        'assets': assets,
        'removed_assets': removed_assets,
        'all_assets': all_assets
    }

if __name__ == '__main__':
  current_time = datetime.now().strftime("%Y%m%d-%H%M%S")

  alpha=0.05

  # Calculate the failure rate target
  failure_rate_target = REWARD_AMOUNT / (REWARD_AMOUNT + SLASH_AMOUNT)
  individual_failure_rate_target = 1 - (1 - failure_rate_target) ** (1 / N_MAX_ACTORS_TASK)

  print(f"Individual failure rate target: {individual_failure_rate_target}")
  print(f"System failure rate target: {failure_rate_target}")

  p_fail_distribution = powerlaw.rvs(alpha, size=1000000)
  mean_fail_rate = np.mean(p_fail_distribution)

  print(f"Mean failure rate: {mean_fail_rate}")

  # Monte Carlo results storage
  monte_carlo_results = {
      'system_failure_rates': [],
      'average_failure_rates': [],
      'actor_counts': [],
      'final_successful_tasks': [],
      'final_failed_tasks': [],
      'final_number_of_assets': [],
      'precisions': [],
      'accuracies': [],
      'recalls': [],
      'assets': [],
      'removed_assets': [],
      'all_assets': []
  }

  faulty_sets = [[] for _ in range(MONTE_CARLO_RUNS)]
  # Run Monte Carlo simulations
  with pool(N_JOBS) as p:
      results = list(p.map(partial(run_simulation, p_fail_distribution=p_fail_distribution), faulty_sets))
  # print(results)
  for result in results:
      monte_carlo_results['system_failure_rates'].append(result['system_failure_rates'])
      monte_carlo_results['average_failure_rates'].append(result['average_failure_rates'])
      monte_carlo_results['actor_counts'].append(result['actor_counts'])
      monte_carlo_results['final_successful_tasks'].append(result['successful_tasks'])
      monte_carlo_results['final_failed_tasks'].append(result['failed_tasks'])
      monte_carlo_results['final_number_of_assets'].append(result['final_number_of_assets'])
      monte_carlo_results['precisions'].append(result['precision'])
      monte_carlo_results['accuracies'].append(result['accuracy'])
      monte_carlo_results['recalls'].append(result['recall'])
      monte_carlo_results['assets'].extend(result['assets'])
      monte_carlo_results['removed_assets'].extend(result['removed_assets'])
      monte_carlo_results['all_assets'].extend(result['all_assets'])

  # Compute average reward and loss per failure rate bin
  average_rewards_per_bin, average_losses_per_bin = compute_average_reward_and_loss(monte_carlo_results['assets'], monte_carlo_results['removed_assets'], faulty_sets)

  # Count the number of uncompleted simulations
  uncompleted_simulations = 0
  for i in range(MONTE_CARLO_RUNS):
      if len(monte_carlo_results['system_failure_rates'][i]) < N_TASKS:
          uncompleted_simulations += 1

  # Pad the lists with zeros to the maximum length
  padded_system_failure_rates = [extend_list(run, N_TASKS) for run in monte_carlo_results['system_failure_rates']]
  padded_average_failure_rates = [extend_list(run, N_TASKS) for run in monte_carlo_results['average_failure_rates']]
  padded_actor_counts = [extend_list(run, N_TASKS) for run in monte_carlo_results['actor_counts']]

  # Aggregate the results
  avg_system_failure_rates = np.mean(padded_system_failure_rates, axis=0)
  avg_average_failure_rates = np.mean(padded_average_failure_rates, axis=0)
  avg_actor_counts = np.mean(padded_actor_counts, axis=0)

  avg_final_successful_tasks = np.mean(monte_carlo_results['final_successful_tasks'])
  avg_final_failed_tasks = np.mean(monte_carlo_results['final_failed_tasks'])
  avg_final_number_of_assets = np.mean(monte_carlo_results['final_number_of_assets'])
  avg_precision = np.mean(monte_carlo_results['precisions'])
  avg_accuracy = np.mean(monte_carlo_results['accuracies'])
  avg_recall = np.mean(monte_carlo_results['recalls'])

  fig, axes = plt.subplots(nrows=2, figsize=(4.5, 5), layout='constrained')

  num_series = MONTE_CARLO_RUNS
  x=np.arange(0, len(padded_system_failure_rates[0]))
  Y=np.array(padded_system_failure_rates)
  print(x.shape, Y.shape)

  x= np.broadcast_to(x, (num_series, len(x))).ravel()
  Y = Y.ravel()
  print(x.shape, Y.shape)
  # Plot (x, y) points in 2d histogram with log colorscale
  # It is pretty evident that there is some kind of structure under the noise
  # You can tune vmax to make signal more visible
  cmap = plt.colormaps["plasma"]
  cmap = cmap.with_extremes(bad=cmap(0))
  h, xedges, yedges = np.histogram2d(x, Y, bins=[5000, 200])
  pcm = axes[0].pcolormesh(xedges, yedges, h.T, cmap=cmap,
                          norm="log", rasterized=True)
  fig.colorbar(pcm, ax=axes[0], label="Number of  points", pad=0)
  axes[0].set_title("2d histogram and log color scale")

  pcm = axes[1].pcolormesh(xedges, yedges, h.T, cmap=cmap, rasterized=True)
  fig.colorbar(pcm, ax=axes[1], label="Number of points", pad=0)
  axes[1].set_title("2d histogram and linear color scale")
  plt.savefig(f"{FIG_DIR}/2dhistogram.png", dpi=300)

  # Individual failure rate
  plt.figure(figsize=(4.5, 2))
  ax1 = plt.gca()
  n_all,bins,_=ax1.hist([a.failure_rate for a in monte_carlo_results['all_assets']], bins=np.arange(0,1,0.01), alpha=0.5, label='Remaining assets')
  n_rm,bins,_=ax1.hist([a.failure_rate for a in monte_carlo_results['removed_assets']], bins=np.arange(0,1,0.01), label='Removed assets')
  ratios=[ 100*r_actor/a_actor for r_actor, a_actor in zip(n_rm,n_all)]
  ax1.set_xlabel('Individual asset failure rate $F_{a}$')
  ax1.set_ylabel('Number of assets')
  ax1.set_yscale('log')
  ax1.set_xticks(np.arange(0, 1.01, 0.1))
  ax1.set_xticks(np.arange(0, 1.01, 0.02),minor=True)
  handles1, labels1 = ax1.get_legend_handles_labels()
  ax2 = ax1.twinx()
  ax2.step(bins[:-1], ratios, 'b-', label='Removed assets (\%)', where="post", linewidth=1.5)
  ax2.set_ylim(0,100)
  ax2.set_ylabel('Removed assets (\%)', color='b')
  ax2.tick_params(axis='y', labelcolor='b')
  ax2.yaxis.set_major_formatter(mtick.PercentFormatter())
  ax2.set_yticks(np.arange(0, 101, 20))
  ax2.set_yticks(np.arange(0, 101, 5), minor=True)
  ax2.axvline(x=individual_failure_rate_target, color='k', linestyle=':', label='$F_{a}^{target}$')
  ax2.axvline(x=failure_rate_target, color='k', linestyle='--', label='$F_{t}^{target}$')
  handles2, labels2 = ax2.get_legend_handles_labels()
  ax2.legend(handles=handles1+handles2, labels=labels1+labels2, loc='upper right',
             bbox_to_anchor=(1, 0.95),
              handletextpad=0.25, 
              labelspacing=0.2, fontsize="small")
  plt.tight_layout()
  plt.savefig(f"{FIG_DIR}/individual_failure_rate-{current_time}.pdf", dpi=1200)

  # Effective failure rate
  plt.figure(figsize=(4.5, 2))
  n_all,bins,_=plt.hist([a.loss/(a.nb_tasks*SLASH_AMOUNT) if a.nb_tasks>0 else 0 for a in monte_carlo_results['all_assets']], bins=np.arange(0,1,0.01), alpha=0.5, label='Remaining assets')
  n_rm,bins,_=plt.hist([a.loss/(a.nb_tasks*SLASH_AMOUNT) if a.nb_tasks>0 else 0 for a in monte_carlo_results['removed_assets']], bins=np.arange(0,1,0.01), label='Removed assets')
  ratios=[ 100*r_actor/a_actor for r_actor, a_actor in zip(n_rm,n_all)]
  ax1 = plt.gca()
  ax1.set_xlabel('Task failure rate $F_{t}$')
  ax1.set_ylabel('Number of assets')
  ax1.set_yscale('log')
  ax1.set_xticks(np.arange(0, 1.01, 0.1))
  ax1.set_xticks(np.arange(0, 1.01, 0.02),minor=True)
  handles1, labels1 = ax1.get_legend_handles_labels()
  ax2 = ax1.twinx()
  ax2.step(bins[:-1], ratios, 'b-', label='Removed assets (\%)', where="post", linewidth=1.5)
  ax2.set_ylabel('Removed assets (\%)', color='b')
  ax2.tick_params(axis='y', labelcolor='b')
  ax2.yaxis.set_major_formatter(mtick.PercentFormatter())
  ax2.set_yticks(np.arange(0, 101, 20))
  ax2.set_yticks(np.arange(0, 101, 5), minor=True)
  ax2.set_ylim(0,100)
  ax2.axvline(x=individual_failure_rate_target, color='k', linestyle=':', label='$F_{a}^{target}$')
  ax2.axvline(x=failure_rate_target, color='k', linestyle='--', label='$F_{t}^{target}$')
  handles2, labels2 = ax2.get_legend_handles_labels()
  ax2.legend(handles=handles1+handles2, labels=labels1+labels2, loc='upper right',
             bbox_to_anchor=(1, 1),
              handletextpad=0.25, 
              labelspacing=0.2, fontsize="small")
  plt.tight_layout()
  plt.savefig(f"{FIG_DIR}/effective_failure_rate-{current_time}.pdf", dpi=1200)

  # # Intrinsic vs effective failure rate for all assets
  # plt.figure(figsize=(4.5, 2.5))
  # effective_failure_rate=[a.loss/(a.nb_tasks*SLASH_AMOUNT) if a.nb_tasks>0 else 0 for a in monte_carlo_results['all_assets']]
  # intrinsic_failure_rate=[a.failure_rate for a in monte_carlo_results['all_assets']]
  # plt.hist2d(intrinsic_failure_rate, effective_failure_rate, bins=200, cmap='plasma')
  # plt.colorbar(label='Number of assets')
  # plt.xlabel('Intrinsic Failure Rate')
  # plt.ylabel('Effective Failure Rate')
  # plt.title('Intrinsic vs Effective Failure Rate')
  # plt.axvline(x=individual_failure_rate_target, color='g', linestyle='--', label='assets Failure Rate Target')
  # plt.axvline(x=failure_rate_target, color='r', linestyle='--', label='System Failure Rate Target')
  # plt.axhline(y=individual_failure_rate_target, color='g', linestyle='--')
  # plt.axhline(y=failure_rate_target, color='r', linestyle='--')
  # plt.savefig(f"{FIG_DIR}/intrinsic_vs_effective_failure_rate-{current_time}.pdf", dpi=1200)