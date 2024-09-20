# Incentivization in Decentralized Cloud Computing Systems with Limited Execution Information
**Henry MONT Internship 2024**

## Internship subject
This internship explores incentivization mechanisms within decentralized cloud computing systems, focusing on the decentralized marketplace developed by iExec. iExec has pioneered a marketplace allowing users to monetize computing resources, including datasets, applications, and server power, while ensuring that no single entity (including iExec itself) can control or censor marketplace operations. Blockchain technology underpins the marketplace, ensuring transparency and traceability for all transactions and their metadata. Trusted Execution Environments (TEEs) further ensure both the integrity of the code execution and the confidentiality of the data, while economic mechanisms incentivize contributors to ensure correct results.

However, the system is not fully immune to malicious actors. Contributors of applications, datasets, and customers alike may introduce low-quality or faulty resources (e.g., buggy applications or poorly formatted datasets) or request tasks with a high likelihood of failure, without facing penalties. Currently the marketplace has no way to incentivize each individual actor to behave in a reliable way and check that they do so. Therefore the marketplace is exposed to potential reliability issues.

The internship’s objective is to analyze the iExec decentralized marketplace, identify system shortcomings that could threaten its proper functioning, and propose solutions. These solutions, which could be cryptographic, economic, or reputation-based, will aim to mitigate the highlighted risks and ensure the system remains robust.

## Repository Structure
The repository is organized chronologically by significant milestones, with each folder representing a key phase of development. Below is a summary of the folders and the contents within.

#### **2024-06-01_Internship-Onboarding**
During the initial phase, I focused on setting up the necessary tools and conducting a literature review on decentralized computing platforms and incentivization mechanisms. This helped me understand the basic architecture of decentralized networks, the role of participants, and the concept of slashing mechanisms.

### **2024-06-10_Finding-Research-Focus**
As the internship progressed, I narrowed my research focus towards incentivization mechanisms, with a particular emphasis on slashing. I also drafted the primary research question and outlined the methodology to explore game theory in decentralized systems.

### **2024-06-17_Getting-Familiar-with-iExec**
I familiarized myself with the iExec decentralized computing platform by completing the "Getting Started" tutorial. This hands-on experimentation helped me understand the platform's capabilities and how decentralized computing operates in practice.

### **2024-06-24_First-Python-Collective-Slashing-Simulation**
I developed a basic Python model to simulate a simple slashing mechanism. Through initial experiments, I gained insights into how slashing functions in practice, exploring key parameters like slashing rates and detection probabilities.

### **2024-07-01_Game-Theoretic-Model-of-Current-System**
I created the first iteration of a game-theoretic model that described the interactions between marketplace participants in decentralized systems. This model laid the foundation for analyzing the strategic behaviors in such environments.

### **2024-07-15_Game-Theoretic-Model-of-Collective-Slashing**
I extended the game-theoretic model to focus specifically on slashing mechanisms and their strategic implications. The updated model included cooperative strategies, reputation effects, and penalties designed to discourage misbehavior among participants.

### **2024-07-17_Ruin-Theoric-Model-of-Collective-Slashing**
I applied ruin theory to the problem of slashing, aiming to understand long-term participant behavior. This approach provided insights into how cumulative penalties and rewards impact the sustainability of participants within the marketplace.

### **2024-08-02_Collective-Slashing-Synthesis**
I introduced the concept of "collective slashing" as an incentivization strategy, synthesizing theoretical aspects of the mechanism.

### **2024-08-22_Collective-Slashing-Simulation**
Using Python, I simulated the collective slashing mechanism, analyzing its performance, fairness, and robustness. This simulation provided valuable data on how blind slashing could function in real-world decentralized systems.

### **2024-09-09_Collective-Reputation-Simulation**
I developed and simulated a reputation mechanism that leverages collective punishment and reward systems. The simulation explored how reputation can act as an alternative to slashing, offering a different approach to incentivize honest behavior in decentralized networks.

### **Material**
Throughout the internship, I consulted a variety of resources, compiling a collection of materials related to decentralized computing, game theory, and incentivization mechanisms.

## Reference

1. Binmore, K. G. (2007). *Game theory: A very short introduction*. Oxford University Press.
2. Hasan, O., Brunie, L., & Bertino, E. (2022). Privacy-preserving reputation systems based on blockchain and other cryptographic building blocks: A survey. *ACM Computing Surveys*, 54(3), 1-36.
3. Dellarocas, C. (n.d.). Analyzing the economic efficiency of eBay-like online reputation reporting mechanisms. *Journal of Economics & Management Strategy*.
4. iExec Technical Documentation. (n.d.). iExec. Retrieved from [iExec Documentation](https://docs.iex.ec).
5. Serban, C., Chen, Y., Zhang, W., & Minsky, N. (2008). The concept of decentralized and secure electronic marketplace. *Proceedings of the 2008 International Conference on E-Commerce and E-Services*.
6. Ramachandran, G. S., Radhakrishnan, R., & Krishnamachari, B. (2018). Towards a decentralized data marketplace for smart cities. *IEEE Transactions on Network and Service Management*, 15(4), 1715-1727.
7. Kaur, J., & Visveswaraiah, B. (2021). A brief survey of token curated registries. *Proceedings of the International Conference on Smart Systems and Inventive Technology (ICSSIT)*.
8. Aral, A., Uriarte, R. B., Simonet-Boulogne, A., & Brandic, I. (2020). Reliability management for blockchain-based decentralized multi-cloud. *Future Generation Computer Systems*, 107, 175-189.
9. Goeschl, T., & Jarke, J. (2013). Non-strategic punishment when monitoring is costly: Experimental evidence on differences between second and third party behavior. *Journal of Economic Behavior & Organization*, 86, 1-14.
10. Fatas, E., Morales, A. J., & Ubeda, P. (2010). Blind justice: An experimental analysis of random punishment in team production. *Journal of Economic Psychology*, 31(2), 265-274.
11. Duell, D., Mengel, F., Mohlin, E., & Weidenholzer, S. (2024). Cooperation through collective punishment and participation. *American Economic Journal: Microeconomics*, 16(2), 1-27.
12. Gao, L., Wang, Z., Pansini, R., Li, Y.-T., & Wang, R.-W. (2015). Collective punishment is more effective than collective reward for promoting cooperation. *Nature Communications*, 6, 7239.
13. Huang, J., Lei, K., Du, M., Zhao, H., Liu, H., Liu, J., & Qi, Z. (2019). Survey on blockchain incentive mechanism. *IEEE Access*, 7, 88770-88784.
14. Maddikunta, P. K. R., Pham, Q.-V., Nguyen, D. C., Huynh-The, T., Aouedi, O., Yenduri, G., Bhattacharya, S., & Gadekallu, T. R. (2022). Incentive techniques for the Internet of Things: A survey. *IEEE Internet of Things Journal*, 9(2), 1325-1342.
15. Li, Z., & Shen, H. (2012). Game-theoretic analysis of cooperation incentive strategies in mobile ad hoc networks. *IEEE Transactions on Wireless Communications*, 11(2), 680-688.