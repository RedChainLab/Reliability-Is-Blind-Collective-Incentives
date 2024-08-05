# Decentralized Computing Marketplace Incentivization - Internship Project

## Overview

This repository contains the work done during my internship on incentivization mechanisms in a decentralized computing marketplace, specifically focusing on the iExec platform. iExec has developed and deployed the first decentralized marketplace for computing resources, enabling anyone to monetize computing power (servers, virtual machines, etc.), decentralized applications (DApps), and data sets.

## Table of Contents
- [Introduction](#introduction)
- [Background](#background)
- [Objectives](#objectives)
- [Project Structure](#project-structure)
- [References](#references)

## Introduction

In contrast to classical cloud computing platforms such as Amazon or Google, the iExec marketplace operates without the need for a trusted third party and cannot be controlled or censored by any entity, including iExec itself. In the iExec marketplace, applications, data, and resources are published as orders, which include crucial information such as pricing details, governance rules, and other relevant specifications. The matching between these orders is done on-chain and generates a deal, which triggers the execution of the corresponding task off-chain. The execution is carried out by a worker selected from the iExec network within a Trusted Execution Environment (TEE) to ensure privacy and integrity. The result and an attestation confirming the secure execution within a TEE are then provided to the client.

## Background

PoCo (Proof-of-Contribution) is a protocol created by iExec that acts as the decentralized trust party in the marketplace. Its duty is to ensure that a worker who contributes correctly to a computing task is rewarded, while ensuring that a requester is not charged unless a consensus is achieved on the task result. This mechanism involves locking the requester's funds for the duration of the consensus, and unlocking them based on the outcome. PoCo also uses a staking mechanism to prevent bad behavior and encourage good contributions from workers.

## Objectives

The primary goal of this project is to incentivize correct behavior in a decentralized computing marketplace. Specific objectives include:
1. Assessing threats posed by actors in the decentralized computing marketplace.
2. Studying the state-of-the-art on incentivization mechanisms (e.g., economic incentives, reputation) in this context.
3. Proposing and evaluating mechanisms to mitigate identified threats.

## Project Structure

The repository is structured in the following chronological order:

### 2024-06-01: Beginning of the Internship
I read articles and iExec documentation to get a better idea of the problem, the possible solutions, and the related fields of research.

### 2024-06-10: Finding a Focus
I explored possible solutions and leads to aim and specify my research. We decided to explore a system where everyone is slashed if a task fails. The purpose is to see if this is feasible and if it would incentivize people to behave correctly.

### 2024-06-17: Testing the iExec Platform
This week was spent following the iExec documentation and attempting to write, compile, and push a basic dApp on the iExec marketplace to better understand the system and prepare for creating Proof of Concepts (PoCs) on the platform.

### 2024-06-24: First Python Slashing Simulation
During this week, I attempted to model the marketplace as an object-oriented system and ran numerous tasks to see whether slashing everyone could theoretically deter malicious actors. The simulation is not perfect and is still performed in a static system.

### 2024-07-01: Game Theoretic Model of the System
After meeting with Matthieu, we decided to focus first on a game-theoretic model of the system.

### 2024-07-15: Game Theoretic Model of Slashing
Explored further into the game-theoretic implications of slashing mechanisms within the decentralized marketplace, aiming to understand its impact on participant behavior and system resilience.  

Also explored the iExec blockchain (graphQL) to look at possible error analysis thanks to the informations logged on blockchain.  

### 2024-07-17: Ruin Theory
Investigated the application of ruin theory to assess how fast actors can get ruined within the decentralized computing marketplace using a slashing strategie.

### 2024-08-02: Blind Slashing Synthesis
A comprehensive synthesis of all work completed to date, aimed at enhancing clarity and readability.

### Material
A collection of all relevant external resources provided to support the completion of the mission.  

## References

1. iExec Documentation: [https://protocol.docs.iex.ec/]
