# Incentivization in Decentralized Cloud Computing Systems with Limited Execution Information
**Internship Project 2024**

## Internship subject
This project explores incentivization mechanisms within decentralized cloud computing systems, focusing on the decentralized marketplace developed by iExec. iExec has pioneered a marketplace allowing users to monetize computing resources, including datasets, applications, and server power, while ensuring that no single entity (including iExec itself) can control or censor marketplace operations. Blockchain technology underpins the marketplace, ensuring transparency and traceability for all transactions and their metadata. Trusted Execution Environments (TEEs) further ensure both the integrity of the code execution and the confidentiality of the data, while economic mechanisms incentivize contributors to ensure correct results.

However, the system is not fully immune to malicious actors. Contributors of applications, datasets, and customers alike may introduce low-quality or faulty resources (e.g., buggy applications or poorly formatted datasets) or request tasks with a high likelihood of failure, without facing penalties. Currently the marketplace has no way to incentivize each individual actor to behave in a reliable way and check that they do so. Therefore the marketplace is exposed to potential reliability issues.

The project’s objective is to analyze the iExec decentralized marketplace, identify system shortcomings that could threaten its proper functioning, and propose solutions. These solutions, which could be cryptographic, economic, or reputation-based, will aim to mitigate the highlighted risks and ensure the system remains robust.

## Internship summary

**June 2024:** During the initial weeks of my internship, I worked on understanding the iExec decentralized marketplace. My primary focus was on how the protocol operates, particularly its use of blockchain technology for transparency and Trusted Execution Environments (TEEs) for secure task execution. This foundational phase also involved a deep dive into iExec’s economic mechanisms and protocols. With this knowledge, I began defining the key objectives of my internship.

**Late June 2024:** I shifted my attention to testing the iExec platform to get a better understanding of the workings of it. This hands-on investigation involved following the iExec introduction course which teach how to develop, upload and run applications on their platform. I also started developing an early Python simulation to model a slashing mechanism, which aimed to explore how economic penalties could be used to deter bad actors from submitting faulty resources or requesting infeasible tasks.

**July 2024:** By mid-July, I began constructing a game-theoretic model of the decentralized marketplace. This model allowed me to analyze the interactions between requesters, asset providers, application providers and workers, and to assess the incentives and potential for misbehavior within the system. I extended this model to include slashing mechanisms, evaluating how various penalty structures could influence behavior. Additionally, I explored Ruin Theory to understand the potential of a collective slashing mechanism on users wealth.

**August 2024:** In August, my research led me to develop the concept of "blind slashing," a mechanism designed to penalize bad actors while maintaining privacy. I synthesized this idea in a document and implemented a simulation of it in Python to assess its effectiveness.

**September 2024:** In September, I shifted my work on a "blind reputation" simulation, focusing on how reputation scores could influence marketplace behavior and improve overall reliability. For that purpose I removed all notions of slashing and stake from the simulation and focused on prioritizing high reputations actors for task executions.

## Repository Structure
The project is organized chronologically by significant milestones, with each folder representing a key phase of development. Below is a summary of the folders and the contents within.

### 1. **2024-06-01_Beginning-of-the-Internship**
   - Initial setup and literature review on decentralized computing platforms and incentivization mechanisms.
   - Understanding the basic architecture of decentralized networks, the role of participants, and slashing mechanisms.

### 2. **2024-06-10_Finding-a-Focus**
   - Narrowed the focus towards incentivization mechanisms, particularly around slashing.
   - Draft of the primary research question and methodology for exploring game theory in decentralized systems.

### 3. **2024-06-17_Testing-the-iExec-Platform**
   - Experimentation with the iExec decentralized computing platform (following the iExec "Getting started" tutorial).

### 4. **2024-06-24_First-Python-Slashing-Simulation**
   - Development of a basic Python model to simulate a simple slashing mechanism.
   - Initial experiments to understand slashing in action, focusing on various parameters like slashing rates and detection probabilities.

### 5. **2024-07-01_Game-Theoretic-Model-of-the-System**
   - First iteration of the game-theoretic model describing interactions between marketplace participants.

### 6. **2024-07-15_Game-Theoretic-Model-of-Slashing**
   - Extension of the game-theoretic model, focusing on slashing mechanisms and their strategic implications.
   - Incorporation of cooperative strategies, reputation effects, and penalties for misbehavior.

### 7. **2024-07-17_Ruin-Theory**
   - Application of ruin theory to the slashing problem, with the aim of understanding long-term participant behavior.
   - Insights into how cumulative penalties and rewards affect the sustainability of participants in the marketplace.

### 8. **2024-08-02_Blind-Slashing-Synthesis**
   - Introduction of the concept of "blind slashing" as a form of incentivization.
   - Theoretical synthesis of blind slashing mechanisms.

### 9. **2024-08-22_Blind-Slashing-Simulation**
   - Simulated the blind slashing mechanism using Python.
   - Analysis of the performance, fairness, and robustness of blind slashing.

### 10. **2024-09-09_Blind-Reputation-Simulation**
   - Development and simulation of a reputation mechanism based on collective punishment and reward.
   - Simulated scenarios where reputation can serve as an alternative to slashing in incentivizing honest behavior.

### 11. **Material**
   - A collection of resources consulted during the project.

## Reference

**Game Theory:**
- Binmore, K. G. (2007). *Game theory: A very short introduction*. Oxford University Press.

**Reputation Systems:**
- Hasan, O., Brunie, L., & Bertino, E. (2022). Privacy-preserving reputation systems based on blockchain and other cryptographic building blocks: A survey. *ACM Computing Surveys*, 54(3), 1-36.
- Dellarocas, C. (n.d.). Analyzing the economic efficiency of eBay-like online reputation reporting mechanisms. *Journal of Economics & Management Strategy*.

**Decentralized Systems:**
- iExec Technical Documentation. (n.d.). iExec. Retrieved from [iExec Documentation](https://docs.iex.ec).
- Serban, C., Chen, Y., Zhang, W., & Minsky, N. (2008). The concept of decentralized and secure electronic marketplace. *Proceedings of the 2008 International Conference on E-Commerce and E-Services*.
- Ramachandran, G. S., Radhakrishnan, R., & Krishnamachari, B. (2018). Towards a decentralized data marketplace for smart cities. *IEEE Transactions on Network and Service Management*, 15(4), 1715-1727.
- Kaur, J., & Visveswaraiah, B. (2021). A brief survey of token curated registries. *Proceedings of the International Conference on Smart Systems and Inventive Technology (ICSSIT)*.
- Aral, A., Uriarte, R. B., Simonet-Boulogne, A., & Brandic, I. (2020). Reliability management for blockchain-based decentralized multi-cloud. *Future Generation Computer Systems*, 107, 175-189.

**Incentives and Punishment:**
- Goeschl, T., & Jarke, J. (2013). Non-strategic punishment when monitoring is costly: Experimental evidence on differences between second and third party behavior. *Journal of Economic Behavior & Organization*, 86, 1-14.
- Fatas, E., Morales, A. J., & Ubeda, P. (2010). Blind justice: An experimental analysis of random punishment in team production. *Journal of Economic Psychology*, 31(2), 265-274.
- Duell, D., Mengel, F., Mohlin, E., & Weidenholzer, S. (2024). Cooperation through collective punishment and participation. *American Economic Journal: Microeconomics*, 16(2), 1-27.
- Gao, L., Wang, Z., Pansini, R., Li, Y.-T., & Wang, R.-W. (2015). Collective punishment is more effective than collective reward for promoting cooperation. *Nature Communications*, 6, 7239.
- Huang, J., Lei, K., Du, M., Zhao, H., Liu, H., Liu, J., & Qi, Z. (2019). Survey on blockchain incentive mechanism. *IEEE Access*, 7, 88770-88784.
- Maddikunta, P. K. R., Pham, Q.-V., Nguyen, D. C., Huynh-The, T., Aouedi, O., Yenduri, G., Bhattacharya, S., & Gadekallu, T. R. (2022). Incentive techniques for the Internet of Things: A survey. *IEEE Internet of Things Journal*, 9(2), 1325-1342.
- Li, Z., & Shen, H. (2012). Game-theoretic analysis of cooperation incentive strategies in mobile ad hoc networks. *IEEE Transactions on Wireless Communications*, 11(2), 680-688.