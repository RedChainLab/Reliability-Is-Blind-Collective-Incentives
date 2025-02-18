# Reliability is Blind - Collective Incentives for Decentralized Computing Marketplaces without Individual Behavior Information (DepWeb3 Workshop, 2025)

This repository contains the code-base to reproduce results for the paper "Reliability is Blind: Collective Incentives for Decentralized Computing Marketplaces without Individual Behavior Information" by Henry Mont, Matthieu Bettinger, Sonia Ben Mokhtar, and Anthony Simonet-Boulogne, accepted for publication at the 
[1st International Workshop on Dependable and Secure Web3, Blockchain and Smart Contracts (DepWeb3)](https://agendablockchain.tecnico.ulisboa.pt/depweb3/).

## Requirements

Python modules like numpy, pandas, matplotlib, and scikit-learn are necessary to run the scripts.

## Reproductibility

Following scripts enable to generate following figures in the paper:
- `stake_survivability.py` generates Figure 3;
- `run_marketplace.py` generates all other figures as well as the data in Table I.

Both scripts accept a parameter giving the number of simulations/jobs to execute in parallel.