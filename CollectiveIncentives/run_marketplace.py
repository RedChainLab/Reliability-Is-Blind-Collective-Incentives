import random
import numpy as np
from scipy.stats import powerlaw
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor as pool
from functools import partial
from datetime import datetime
import matplotlib.ticker as mtick
from matplotlib import patches
from matplotlib.legend_handler import HandlerTuple
import pandas as pd

from marketplace import *
import coll_stake
import coll_rep
import coll_SR
import coll_free

def run_marketplace(incentive, name, gen_plots=True):
  current_time = datetime.now().strftime("%Y%m%d-%H%M%S")

  # Calculate the failure rate target
  failure_rate_target = REWARD_AMOUNT / (REWARD_AMOUNT + SLASH_AMOUNT)
  individual_failure_rate_target = 1 - (1 - failure_rate_target) ** (1 / N_MAX_ASSETS_TASK)

  print(f"Individual failure rate target: {individual_failure_rate_target}")
  print(f"System failure rate target: {failure_rate_target}")

  p_fail_distribution = powerlaw.rvs(ALPHA, size=N_FAIL_SAMPLES)
  mean_fail_rate = np.mean(p_fail_distribution)

  print(f"Mean failure rate: {mean_fail_rate}")
  print(f"Expected initial system failure rate: {1-(1-mean_fail_rate)**N_MAX_ASSETS_TASK:.4f}")

  # Monte Carlo results storage
  monte_carlo_results = {
      'system_failure_rates': [],
      'average_failure_rates': [],
      'asset_counts': [],
      'final_successful_tasks': [],
      'task_failed_list': [],
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
  with pool(N_JOBS) as p:
      results = list(p.map(partial(incentive, p_fail_distribution=p_fail_distribution), faulty_sets))
  # results = [incentive(faulty_sets[i], p_fail_distribution) for i in range(MONTE_CARLO_RUNS)]

  print("Processing results")
  for result in results:
      monte_carlo_results['system_failure_rates'].append(result['system_failure_rates'])
      monte_carlo_results['average_failure_rates'].append(result['average_failure_rates'])
      monte_carlo_results['asset_counts'].append(result['asset_counts'])
      monte_carlo_results['final_successful_tasks'].append(result['successful_tasks'])
      monte_carlo_results['task_failed_list'].append(result['task_failed_list'])
      monte_carlo_results['final_failed_tasks'].append(result['failed_tasks'])
      monte_carlo_results['final_number_of_assets'].append(result['final_number_of_assets'])
      monte_carlo_results['precisions'].append(result['precision'])
      monte_carlo_results['accuracies'].append(result['accuracy'])
      monte_carlo_results['recalls'].append(result['recall'])
      monte_carlo_results['assets'].extend(result['assets'])
      monte_carlo_results['removed_assets'].extend(result['removed_assets'])
      monte_carlo_results['all_assets'].extend(result['all_assets'])

  # Compute average reward and loss per failure rate bin
  #average_rewards_per_bin, average_losses_per_bin = compute_average_reward_and_loss(monte_carlo_results['assets'], monte_carlo_results['removed_assets'], faulty_sets)

  # Count the number of uncompleted simulations
  # uncompleted_simulations = 0
  # for i in range(MONTE_CARLO_RUNS):
  #     if len(monte_carlo_results['system_failure_rates'][i]) < N_TASKS:
  #         uncompleted_simulations += 1

  # Pad the lists with zeros to the maximum length
  # padded_system_failure_rates = [extend_list(run, N_TASKS) for run in monte_carlo_results['system_failure_rates']]
  # padded_average_failure_rates = [extend_list(run, N_TASKS) for run in monte_carlo_results['average_failure_rates']]
  # padded_asset_counts = [extend_list(run, N_TASKS) for run in monte_carlo_results['asset_counts']]
  padded_task_failed_list = [extend_list(run, N_TASKS) for run in monte_carlo_results['task_failed_list']]

  # Aggregate the results
  # avg_system_failure_rates = np.mean(padded_system_failure_rates, axis=0)
  # avg_average_failure_rates = np.mean(padded_average_failure_rates, axis=0)
  # avg_asset_counts = np.mean(padded_asset_counts, axis=0)
  window_avg_task_failed = [moving_average(avg_task_failed, n=WINDOW_SIZE) for avg_task_failed in padded_task_failed_list]
  # avg_window_avg_task_failed = np.mean(window_avg_task_failed, axis=0)

  # avg_final_successful_tasks = np.mean(monte_carlo_results['final_successful_tasks'])
  # avg_final_failed_tasks = np.mean(monte_carlo_results['final_failed_tasks'])
  # avg_final_number_of_assets = np.mean(monte_carlo_results['final_number_of_assets'])
  avg_precision = np.mean(monte_carlo_results['precisions'])
  # avg_accuracy = np.mean(monte_carlo_results['accuracies'])
  avg_recall = np.mean(monte_carlo_results['recalls'])

  print(f"Average precision;recall: {avg_precision:.4f} {avg_recall:.4f}")

  if gen_plots:

    fig, ax = plt.subplots(figsize=(4.5, 2.5))

    percentiles=[50, 25, 50, 75, 95]
    percentiles_values = np.percentile(window_avg_task_failed, percentiles, axis=0)
    ax.fill_between(range(N_TASKS), percentiles_values[0], percentiles_values[-1], color='b', alpha=0.2, label='5-95\%', edgecolor="none")
    # ax.fill_between(range(N_TASKS), percentiles_values[1], percentiles_values[-2], color='b', alpha=0.4, label='25-75\%', edgecolor="none")
    ax.plot(range(N_TASKS), percentiles_values[2], 'b-', label=f'{name}', linewidth=1)
    ax.axhline(y=failure_rate_target, color='r', linestyle='--', label='$F_t^{\\mathit{target}}='+f'{failure_rate_target*100:.0f}\%$', linewidth=1)
    ax.set_xlabel("Task number")
    ax.set_ylabel("System failure rate $F_t$")
    ax.set_yscale("log")
    ax.set_ylim(0.001, 1)
    # ax.set_yticks(np.arange(0, 0.61, 0.2))
    # ax.set_yticks(np.arange(0, 0.61, 0.05),minor=True)
    ax.grid(True, which="major")
    ax.grid(True, which="minor", linestyle='-', alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    handles = [
      (patches.Rectangle(xy=(0,0), width=1, height=1, color='b', alpha=0.2),
      # patches.Rectangle(xy=(0,0), width=1, height=0.25, color='b', alpha=0.4),
      plt.Line2D([0], [0], color='b', label='50%', linewidth=1)),
      plt.Line2D([0], [0], color='r', linestyle='--', label=f'$F_t={failure_rate_target*100:.0f}%$', linewidth=1)
    ]
    labels=[labels[1], labels[2]]
    # ax.yaxis.set_major_formatter(mtick.PercentFormatter(1))
    ax.legend(handles=handles, labels=labels, loc='upper right',
                bbox_to_anchor=(1, 1),
                  handletextpad=0.25, 
                  labelspacing=0.2, fontsize="small")
    fig.tight_layout()
    plt.savefig(f"{FIG_DIR}/system_failure_rate-{name}-{N_TASKS}-{N_ASSETS_INITIAL}-{TARGET_TASK_FAILURE_RATE}-{S0}-{ALPHA}-{current_time}.pdf", dpi=1200)

    # Individual failure rate
    plt.figure(figsize=(4.5, 2))
    ax1 = plt.gca()
    n_all,bins,_=ax1.hist([a.failure_rate for a in monte_carlo_results['all_assets']], bins=np.arange(0,1,0.01), label='Remaining assets', histtype="stepfilled", edgecolor='black', color="lightcyan", linewidth=.5)
    n_rm,bins,_=ax1.hist([a.failure_rate for a in monte_carlo_results['removed_assets']], bins=np.arange(0,1,0.01), label='Removed assets', histtype="stepfilled", edgecolor='black', color="salmon", linewidth=.5)
    ratios=[ 100*r_asset/a_asset for r_asset, a_asset in zip(n_rm,n_all)]
    ax1.set_xlabel('Individual asset failure rate $F_{a}$')
    ax1.set_ylabel('Number of assets')
    ax1.set_yscale('log')
    ax1.set_xticks(np.arange(0, 1.01, 0.1))
    ax1.set_xticks(np.arange(0, 1.01, 0.02),minor=True)
    handles1, labels1 = ax1.get_legend_handles_labels()
    ax2 = ax1.twinx()
    ax2.step(bins[:-1], ratios, color="royalblue", label='Removed assets (\%)', where="post", linewidth=1.5)
    ax2.set_ylim(0,100)
    ax2.set_ylabel('Removed assets (\%)', color="royalblue")
    ax2.tick_params(axis='y', labelcolor="royalblue")
    ax2.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax2.set_yticks(np.arange(0, 101, 20))
    ax2.set_yticks(np.arange(0, 101, 5), minor=True)
    ax2.axvline(x=individual_failure_rate_target, color='k', linestyle=':', label='$F_{a}^{target}$', linewidth=1)
    ax2.axvline(x=failure_rate_target, color='k', linestyle='--', label='$F_{t}^{target}$', linewidth=1)
    handles2, labels2 = ax2.get_legend_handles_labels()
    legend=ax2.legend(handles=handles1+handles2, labels=labels1+labels2, loc='upper right',
              bbox_to_anchor=(1, 0.95),
                handletextpad=0.25, 
                labelspacing=0.2, fontsize="small")
    legend.get_texts()[2].set_color("royalblue")
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/individual_failure_rate-{name}-{N_TASKS}-{N_ASSETS_INITIAL}-{TARGET_TASK_FAILURE_RATE}-{S0}-{ALPHA}-{current_time}.pdf", dpi=1200)

    # Effective failure rate
    plt.figure(figsize=(4.5, 2))
    ax1 = plt.gca()
    n_all,bins,_=plt.hist([a.loss/(a.nb_tasks*SLASH_AMOUNT) if a.nb_tasks>0 else 0 for a in monte_carlo_results['all_assets']], 
                          bins=np.arange(0,1,0.01), label='Remaining assets', histtype="stepfilled", edgecolor='black', color="lightcyan", linewidth=.5)
    n_rm,bins,_=plt.hist([a.loss/(a.nb_tasks*SLASH_AMOUNT) if a.nb_tasks>0 else 0 for a in monte_carlo_results['removed_assets']], 
                        bins=np.arange(0,1,0.01), label='Removed assets', histtype="stepfilled", edgecolor='black', color="salmon", linewidth=.5)
    ratios=[ 100*r_asset/a_asset for r_asset, a_asset in zip(n_rm,n_all)]
    ax1.set_xlabel('Task failure rate $F_{t}$')
    ax1.set_ylabel('Number of assets')
    ax1.set_yscale('log')
    ax1.set_xticks(np.arange(0, 1.01, 0.1))
    ax1.set_xticks(np.arange(0, 1.01, 0.02),minor=True)
    handles1, labels1 = ax1.get_legend_handles_labels()
    ax2 = ax1.twinx()
    ax2.step(bins[:-1], ratios, color="royalblue", label='Removed assets (\%)', where="post", linewidth=1.5)
    ax2.set_ylim(0,100)
    ax2.set_ylabel('Removed assets (\%)', color="royalblue")
    ax2.tick_params(axis='y', labelcolor="royalblue")
    ax2.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax2.set_yticks(np.arange(0, 101, 20))
    ax2.set_yticks(np.arange(0, 101, 5), minor=True)
    ax2.axvline(x=individual_failure_rate_target, color='k', linestyle=':', label='$F_{a}^{target}$', linewidth=1)
    ax2.axvline(x=failure_rate_target, color='k', linestyle='--', label='$F_{t}^{target}$', linewidth=1)
    handles2, labels2 = ax2.get_legend_handles_labels()
    legend=ax2.legend(handles=handles1+handles2, labels=labels1+labels2, loc='upper right',
              bbox_to_anchor=(1, 0.95),
                handletextpad=0.25, 
                labelspacing=0.2, fontsize="small")
    legend.get_texts()[2].set_color("royalblue")
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/effective_failure_rate-{name}-{N_TASKS}-{N_ASSETS_INITIAL}-{TARGET_TASK_FAILURE_RATE}-{S0}-{ALPHA}-{current_time}.pdf", dpi=1200)

  return {
    'precision': avg_precision,
    'recall': avg_recall,
    'window_avg_task_failed': window_avg_task_failed,
  }

if __name__ == '__main__':
  current_time = datetime.now().strftime("%Y%m%d-%H%M%S")

  # Calculate the failure rate target
  failure_rate_target = REWARD_AMOUNT / (REWARD_AMOUNT + SLASH_AMOUNT)
  individual_failure_rate_target = 1 - (1 - failure_rate_target) ** (1 / N_MAX_ASSETS_TASK)

  results=[]
  incentives = [#coll_free, 
                coll_stake, 
                #coll_rep, 
                coll_SR]
  for incentive in incentives:
    results.append(run_marketplace(incentive.run_simulation, incentive.name, True))

  print("Finished running simulations")

  all_window_avg_task_failed = [result['window_avg_task_failed'] for result in results]
  all_precision = [result['precision'] for result in results]
  all_recall = [result['recall'] for result in results]

  fig, ax = plt.subplots(figsize=(4.5, 2.5))
  all_handles, all_labels = [], []
  colors=['purple', 'blue', 'orange', 'green']
  for window_avg_task_failed, name, color in zip(all_window_avg_task_failed, [incentive.name for incentive in incentives], colors):
    print("Plotting", name)
    percentiles=[50, 25, 50, 75, 95]
    percentiles_values = np.percentile(window_avg_task_failed, percentiles, axis=0)
    ax.plot(range(N_TASKS),  percentiles_values[-1], color=color, alpha=0.5, label='5-95\%', linewidth=0.7, linestyle='-')
    ax.plot(range(N_TASKS), percentiles_values[2], color, alpha=0.9, label=f'{name}', linewidth=1)
    ax.set_xlabel("Task number")
    ax.set_ylabel("System failure rate $F_t$")
    ax.set_yscale("log")
    ax.set_ylim(0.001, 1)
    # ax.set_yticks(np.arange(0, 0.61, 0.2))
    # ax.set_yticks(np.arange(0, 0.61, 0.05),minor=True)
    ax.grid(True, which="major")
    ax.grid(True, which="minor", linestyle='-', alpha=0.3)

    all_handles.append((plt.Line2D([0], [0], color=color, alpha=0.9, linewidth=1),
                       plt.Line2D([0], [0], color=color, alpha=0.5, linewidth=0.7))
                      )
    all_labels.append(name)
  ax.axhline(y=failure_rate_target, color='r', linestyle=':', label='$F_t^{\\mathit{target}}='+f'{failure_rate_target*100:.0f}\%$', linewidth=1.5)
  all_handles.append(plt.Line2D([0], [0], color='r', linestyle=':', label=f'$F_t={failure_rate_target*100:.0f}%$', linewidth=1.5))
  all_labels.append('$F_t^{\\mathit{target}}='+f'{failure_rate_target*100:.0f}\%$')
  ax.legend(handles=all_handles, labels=all_labels, loc='center right',
                ncols=3,
                bbox_to_anchor=(1, 0.6),
                borderpad=0.2,
                handlelength=1,
                columnspacing=0.5,
                handletextpad=0.25, 
                labelspacing=0.2, fontsize="small",
                handler_map={tuple: HandlerTuple(ndivide=None)}
                )
  fig.tight_layout()
  plt.savefig(f"{FIG_DIR}/system_failure_rate-ALL-{N_TASKS}-{N_ASSETS_INITIAL}-{TARGET_TASK_FAILURE_RATE}-{S0}-{ALPHA}-{current_time}.pdf", dpi=1200)
  print(f"Saved file {FIG_DIR}/system_failure_rate-ALL-{N_TASKS}-{N_ASSETS_INITIAL}-{TARGET_TASK_FAILURE_RATE}-{S0}-{ALPHA}-{current_time}.pdf")

  print(all_window_avg_task_failed[0])
  df=pd.DataFrame(zip([incentive.name for incentive in incentives], 
                      all_precision, all_recall, [np.mean(np.mean(config, axis=0)[:-WINDOW_SIZE]) for config in all_window_avg_task_failed]),
                      columns=['Incentive', 'Precision', 'Recall', 'Failure_Rate'])
  print(df)
  df.to_csv(f"{DATA_DIR}/precision_recall-{N_TASKS}-{N_ASSETS_INITIAL}-{TARGET_TASK_FAILURE_RATE}-{S0}-{ALPHA}-{current_time}.csv", index=False)
  