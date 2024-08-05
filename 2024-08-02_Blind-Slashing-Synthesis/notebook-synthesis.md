# Blind Slashing: Moderation of Multi-Party Interaction in Decentralized Systems with Limited Individual Information

We are working in the context of a decentralized marketplace for cloud computing. The purpose of this marketplace is to bring together people who need assets (such as datasets, dApps) and computing power, and those who can provide them. The idea is that transactions can be conducted in a fully confidential and decentralized manner, thanks to blockchain and smart contracts. This ensures that asset providers can "rent" their assets without fear of leaks or theft, as everything occurs within the marketplace and is regulated by smart contracts. In practice, a requester chooses a dApp and dataset to execute, pays the required fees and predicted computing power, and all assets are transferred to a selected pool of workers who complete the task and upload the encrypted results for the requester to retrieve.

In this marketplace, we can identify three types of actors:

1. **Requesters**: Choose a dApp, select a dataset, set a confidence level, and pay fees.
2. **Asset Providers**: Upload dApps/datasets and receive fees.
3. **Computing Providers**: Run tasks, validate results, and receive fees.

The problem with this system is that if a task fails, we have very little information about the cause of the failure.

Currently, the computing provider is blamed every time a task fails and endures a penalty on the money they staked. This is a double penalty since they already provided the computing power and are punished additionally.

This system could be considered fair if the error truly originated from the computing provider. However, in practice, errors could be induced by other actors such as the requester with faulty requests, the dApp provider with faulty dApps, or the dataset provider with faulty datasets.

In such a system with limited individual information about the execution process and errors, we need a solution to incentivize good behavior.

For this purpose, we are working on blind slashing. A method where every time a task fails, we slash the stake of everyone involved in the task. The rationale is that actors causing faults will be involved more frequently in failed tasks since they are the ones at fault. In contrast, innocent actors will be involved less often in failed tasks and therefore will lose less money. This way, we hope to incentivize correct behavior and penalize incorrect behavior.

We will study the feasibility of this system using Game Theory and then a Ruin Theory approach.  

# Showing Blind Slashing necessity under game theoric model

In the context of a decentralized marketplace for cloud computing, where various actors such as requesters, asset providers, and computing providers interact, ensuring the integrity and success of tasks is crucial. To understand the behaviors and strategic interactions of users within this decentralized marketplace, we study our system within a game-theoretic framework. This approach allows us to analyze how different actors (requesters, asset providers, and computing providers) formulate their strategies based on potential payoffs and penalties.  

## Game theory basics

Game theory is a mathematical framework used to analyze strategic interactions among rational decision-makers, known as players. Each player in a game has a set of possible strategies and makes decisions to maximize their own payoff, considering the potential choices of other players. Key concepts in game theory include the **payoff matrix**, which outlines the rewards or penalties for each combination of strategies chosen by the players; **Nash equilibrium**, a state where no player can benefit by unilaterally changing their strategy given the strategies of others; and **dominant strategy**, a strategy that results in the highest payoff for a player regardless of what the other players do. By modeling these interactions, game theory helps predict outcomes in competitive and cooperative scenarios, providing insights into the optimal strategies and potential equilibria in complex systems.

## Game theory applied to our system

### Players

We'll only consider 3 different actors: Requesters, Assets provider (dApp Providers or Data Providers) and Computing Providers.  

1. **Requesters**: Choose a dApp, choose a dataset, set a confidence level, pay fees.
   - Honest: Follow the protocol, choose appropriate dApp and data.
   - Malicious: Choose inappropriate dApp or data to disrupt the system.

2. **Assets providers**: Upload dApps/datasets, receive fees.
   - Honest: Upload functional, correct dApps / accurate, useful datasets.
   - Malicious: Upload faulty or harmful dApps / incorrect or harmful datasets.

3. **Computing Providers**: Run tasks, validate results, receive fees.
   - Honest: Execute tasks correctly and report accurate results.
   - Malicious: Manipulate task execution or results.

### Strategies

A very naïve setup where we consider that people would either fail on accident or successfuly complete their task would leave us with two strategies:
* **S**: Success
* **F**: Fail  

### Payoffs

  * **S**: Successfuly completing task
    * $P_r = U_r - (Price_a + Price_c)$
    * $P_a = Price_a$
    * $P_c = Price_c - Cost_c$
  * **F**: Failing task
    * $P_r = 0$
    * $P_a = 0$
    * $P_c = -(Cost_c + Slash_c)$

$U_r$: Utility from the result  
$P_r$: Requester payoff  
$P_a$: Assets provider payoff  
$P_c$: Computing provider payoff  
$Slash_c$: Computing provider slash   
$Price_a$: Asset price  
$Price_c$: Computing price  
$Cost_c$: Computing cost  

For the requester, we consider that "utility from the result" is strictly positive, hence $P_r > Total Cost$.  

### Payoff Matrix and Nash Equilibria

We'll write payoffs in the following way: (P<sub>r</sub>, P<sub>a</sub>, P<sub>c</sub>)

<u>Requester chooses S:</u>  
|Asset / Computer| S | F |
|--|--|--|
| **S** | (<u>U<sub>r</sub> - (Price<sub>a</sub> + Price<sub>c</sub>)</u> , <u>Price<sub>a</sub></u> , <u>Price<sub>c</sub> - Cost<sub>c</sub></u> ) | (<u>0</u> , <u>0</u>, -(Cost<sub>c</sub> + Slash<sub>c</sub>)) |
| **F** | (<u>0</u>, 0, <u>-(Cost<sub>c</sub> + Slash<sub>c</sub>)</u>) | (<u>0</u>, <u>0</u>, <u>-(Cost<sub>c</sub> + Slash<sub>c</sub>)</u>) |

<u>Requester chooses F:</u>  
|Asset / Computer| S | F |
|--|--|--|
| **S** | (0, <u>0</u>, <u>-(Cost<sub>c</sub> + Slash<sub>c</sub>)</u>) | (<u>0</u>, <u>0</u>, <u>-(Cost<sub>c</sub> + Slash<sub>c</sub>)</u>) |
| **F** | (<u>0</u>, <u>0</u>, <u>-(Cost<sub>c</sub> + Slash<sub>c</sub>)</u>) | (<u>0</u>, <u>0</u>, <u>-(Cost<sub>c</sub> + Slash<sub>c</sub>)</u>) |

These matrices show the payoffs for the Requester and Assets Provider based on their strategies.  

After working on each matrix independently, we compare both matrices cell by cell and underline the best payoff for the requester.  

From these, we can see that the pure Nash Equilibria are:  
(S, S, S)  
(S, F, F)  
(F, S, F)  
(F, F, S)  
(F, F, F)  

This outlines a clear problem: we aim for players to adopt the successful strategy (S, S, S), but they have equally strong incentives to remain in a faulty strategy.

However, we can observe that the (S, S, S) strategy is more stable than other strategies. Once players choose this strategy, they are unlikely to abandon it, as they will not find better payoffs elsewhere. This observation holds true primarily for repeated games.

### Repeated games

In a single-play game, participants may be incentivized to act selfishly (defect). However, in repeated games, the potential for future interactions typically encourages cooperation, as participants might adopt cooperative strategies to ensure long-term benefits over short-term gains.  

Despite this, when considering cooperative strategies in the long run, we observe that participants lack substantial incentives to behave more cooperatively outside the rewards for successful task completion. The core issue is that causing a task to fail incurs no costs compared to the effort required to deliver real value.  

In a naive approach to the current system, honest actors are clearly incentivized to cooperate and earn money. However, there is little motivation to adopt a cooperative strategy quickly, and it is nearly costless for asset providers and requesters to persist in making mistakes, causing tasks to fail. Moreover, a malicious actor who never intended to cooperate has no reason to adopt a cooperative strategy, as they face no punishment. Consequently, computing providers find themselves in a precarious situation, where anyone can jeopardize their earnings without facing any repercussions.  

### More complex modelling

In an attempt to eliminate the undesired Nash equilibria, we experimented with various game-theoretic models of our system, adjusting several parameters. Unfortunately, these efforts did not yield more information than our initial model. The best results we achieved came from a more complex model that included the production costs of dApps and datasets. However, even in this scenario, some undesired Nash equilibria persisted.  

## Conclusion on game theory

By examining the behaviors and strategic interactions of various actors, we identified significant issues in the current incentive structures.

Despite the theoretical stability of the (S, S, S) strategy, where all players succeed, undesired Nash equilibria persist, allowing players to adopt faulty strategies without facing sufficient penalties. This is particularly problematic for computing providers who can be adversely affected by the actions of requesters and asset providers, as these actors face minimal repercussions for causing task failures.

In repeated games, the potential for future interactions can promote cooperation, but this is insufficient without real incentives for immediate cooperative behavior. The lack of penalties for non-cooperative actions results in a precarious situation for honest actors, undermining the integrity and success of the system.

To tackle those problems, a blind slashing model, where every actor involved in a task faces penalties upon its failure, would bring several key benefits to the decentralized marketplace. It creates a strong deterrent against non-cooperative behavior by ensuring that all actors have a stake in the success of each task. This model incentivizes participants to carefully select reliable partners and maintain high standards in their operations, as any failure would result in a direct financial loss. It also helps to mitigate the risk posed by malicious actors, who would face significant penalties for attempting to disrupt the system.

# Showing Blind Slashing feasibility under ruin theoric model

In a decentralized marketplaces for cloud computing, ensuring reliable and cooperative behavior from all participants is crucial. Blind slashing, a model where every actor involved in a task faces penalties upon its failure, offers a promising solution to enforce compliance and deter malicious activities. To evaluate the feasibility and effectiveness of this approach, we employ a ruin theory model, which allows us to predict the sustainability of participants' stakes over time and the impact of various penalties and rewards.

## Basic blind slashing model

Given:
- $S_0$: initial stake
- P: penalty per task failure
- L: user loss per task
- F: global failure rate of the system

We want to calculate the expected time to ruin (number of tasks until a participant’s stake is depleted).

### Failure Rate

1. **Individual Failure Rate ( $F_u$ )**:
   - Each user u has their own failure rate $F_u$. This rate follows a long-tailed distribution where most users have low failure rates, and a few have higher rates due to malicious intent or frequent mistakes.

2. **Overall Task Failure Rate ( F )**:
   - The failure rate for a task depends on the failure rates of all four actors involved (requester, dApp provider, data provider, and computing provider).
   - The formula for calculating the failure rate of a task considering the failure rates of all participants can be given by:
     $$
     F = 1 - (1 - F_u) \cdot (1 - \text{mean}(F_u))^3
     $$
   - This formula considers the probability that at least one of the four actors fails, causing the task to fail.

### Expected Loss Per Task

For a given participant with failure rate  $F_u$ :
$$
L = F \times P
$$

### Time to Ruin

The time to ruin,  T , is given by:
$$
T = \frac{S_0}{L} = \frac{S_0}{F \times P}
$$

### Conclusion on Basic blind slashing model

This basic model demonstrates the feasibility of creating a significant disparity in penalties between faulty and non-faulty actors. However, it also highlights that non-faulty users may still face substantial financial pressure due to the blind slashing mechanism. To mitigate this, it would be beneficial to introduce a recovery system, akin to how premiums balance claims in ruin theory.  

## Introducing a Recovery Mechanism

1. **Recovery Rate ( $R$ )**:
   - Define a recovery amount $R$ which represents the amount a user recovers per successful task.

2. **Probability of Success ( $1 - F$ )**:
   - The probability of a task being successful is $1 - F$.

3. **Net loss in Stake ( $L_{\text{net}}$ )**:
   - The net loss per task will now be the penalty incurred for a failure minus the recovery from a success.

### Formula for Time to Ruin with Recovery

Let's denote:
- $S_0$ as the initial stake.
- $P$ as the penalty per task failure.
- $R$ as the recovery per successful task.
- $F$ as the task failure rate.

The expected loss per task without recovery:
$$ L = F \times P $$

The expected recovery per task:
$$ R = (1 - F) \times R $$

The net expected loss in stake per task:
$$ L_{\text{net}} = L - R = F \times P - (1 - F) \times R $$

To ensure that the model is coherent, $L_{\text{net}}$ should be positive, implying that users are more likely to lose stake than gain it. However, in some scenarios, it might be possible for $L_{\text{net}}$ to be zero or negative, meaning the user never runs out of stake or increases their stake over time. We will assume $L_{\text{net}} > 0$ for the ruin theory to hold.

The time to ruin $T$ can be calculated as:
$$ T = \frac{S_0}{L_{\text{net}}} = \frac{S_0}{F \times P - (1 - F) \times R} $$

## Finding the parameters to ensure a given QoS

### Net Loss Per Task
The net loss per task ($L_{\text{net}}$) is given by:
$$
L_{\text{net}} = F \cdot P - (1 - F) \cdot R
$$
where:
- $F$ is the task failure rate.
- $P$ is the penalty per task failure.
- $R$ is the recovery per successful task.

### Inequality for Losing Money
A user is not losing / earning money if $L_{\text{net}} \leq 0$. Therefore, the inequality we need to solve is:
$$
F \cdot P - (1 - F) \cdot R \leq 0
$$

Solving the inequality:  
$$
F \cdot P - R + F \cdot R \leq 0
$$

$$ 
F(P + R) - R \leq 0 
$$

$$ 
F(P + R) \leq R 
$$

$$ 
F \leq \frac{R}{P + R} 
$$

This means that for a chosen treshold corresponding to $\frac{R}{P + R}$, users with a Failure Rate under that treshold will prosper whereas users above will loose money and eventually be bankrupted out of the system.

### Example: Set a targeted failure rate

$F_t$ being the targeted failure rate.  

Let's choose $F_t\leq 0.2$  

This mean we'll be able to garantee to our users that on average a task will not be failing more than 20% of the time.  

### Example: Decide of the slashing and recovery rate

The slashing and recovery rate must respect the following ratio: $ F \leq \frac{R}{P + R}  $

So if we choose an arbitrary slashing amount such as $P = 500$.  
(Choosing arbitrarly the slashing value might pose some problems later on as we might want to scale the slashing and recovery based on the task value.  
Otherwise it would be too easy to spam worthless but successful tasks to recover money.)  

We get:  
$ 0.2 \leq \frac{R}{500+R} $

$ \Rightarrow 0.2 \times (500+R) \leq R $

$ \Rightarrow 100 + 0.2 \times R \leq R $

$ \Rightarrow 100 \leq 0.8 \times R $

$ \Rightarrow 125 \leq R $

This means that we need to let the user recover at least 125 for each successful task in order for them to not loose money with a slashing of 500 at a failure rate of 0.2 or below.

### Example: Find what maximum failure rate will be tolerated amongst users
This part is only informative, it does not really matter (unless we want to base our system on the individual failure rate tolerated amongst users).  

We want:  
$F_t\leq 0.2$

So we get:  
$ 1 - (1 - F_u)^{4} \geq 0.2$

$ \Rightarrow - (1 - F_u)^{4} \geq - 0.8$

$ \Rightarrow (1 - F_u)^{4} \leq 0.8$

$ \Rightarrow \left| 1 - F_u \right| \leq 0.8^{\frac{1}{4}}$   ($ 0 \leq F_u \leq 1 $)

$ \Rightarrow - F_u \leq 0.8^{\frac{1}{4}} - 1$

$ \Rightarrow F_u \geq 1 - 0.8^{\frac{1}{4}}$ ($ \approx 0.054 $)

A user cannot have a greater failure rate than 5.4% if he wants to stay profitable.  

## Controlling the Time to Ruin

The time to ruin can be calculated using the following formula:

$$ T = \frac{S_0}{L_{net}} = \frac{S_0}{F \times P - (1 - F) \times R} $$

### Adjusting User Stake

Simply changing the user stake could allow users to reach ruin more or less quickly. However, the staked amount is a crucial factor. If set too high or too low, it might make it excessively difficult or too easy to enter the system. Therefore, it would be better to use another lever.

### Adjusting the Penalty/Recovery System

We can adjust $L_{net}$ to either decrease or increase the time to ruin.

$L_{net}$ can be seen as an affine function representing a user's loss per task as a function of their failure rate. It is negative between 0 and $F_t$ (since users shouldn't lose money if they engage in transactions with a failure rate below this threshold), and positive and increasing between $F_t$ and infinity. We want to increase the slope of this function so that a higher failure rate $x$ results in greater loss and, consequently, a shorter time to ruin:

$$ L_{net}(x) = x \times P - (1 - x) \times R $$

Expanding this gives us:

$$ L_{net}(x) = xP - (1 - x)R $$
$$ L_{net}(x) = xP - R + xR $$
$$ L_{net}(x) = xP + xR - R $$
$$ L_{net}(x) = x(P + R) - R $$

Therefore, the expanded function is:

$$ L_{net}(x) = x(P + R) - R $$

To increase the slope, we can multiply the coefficient $P + R$ by a factor $k > 1$:

$$ L_{net}(x) = x \times k(P + R) - R $$

As $x$ increases, the loss grows more rapidly, which shortens the time to ruin. However, by doing this, $L_{net}(F_t) = 0$ may no longer hold true for all $k$. We need this equality to guarantee a certain level of reliability.

Users need to maintain a failure rate below $\frac{R}{P + R}$ to stay profitable. Thus, this should equal our targeted failure rate, making it unprofitable for users to exceed this rate.

To ensure $R$ depends on $P$ such that the following always holds:

$$ F_t = \frac{R}{P + R} $$

We rearrange and solve:

$$ F_t \times (P + R) = R $$
$$ F_t \times P + F_t \times R = R $$
$$ F_t \times P = R - F_t \times R $$
$$ F_t \times P = R \times (1 - F_t) $$
$$ R = \frac{F_t \times P}{1 - F_t} $$

Inserting this into the net loss function gives us:

$$ L_{net}(x) = x \times (P + \frac{F_t \times P}{1 - F_t}) - \frac{F_t \times P}{1 - F_t} $$

Simplifying further:

$$ L_{net}(x) = x \times \frac{P}{1 - F_t} - \frac{F_t \times P}{1 - F_t} $$

Now, we can adjust $P$ to modify the slope of our function while keeping $L_{net}(F_t) = 0$ valid. However, we are limited by the maximum stake, as excessive slashing risks causing significant losses for users who are simply unlucky (cf "Estimate the minimum initial stake needed").

### Real world translation

In practice we wannot simply apply the function and compute the net loss of a user in this way. We don't know in advance the user failure rate and we need to act with a limited knowledge on each task execution.  
The challenge here if we want to modify the slashing penalty is to respect the defined ratio so that everyone that is below our targeted failure rate stays profitable.  
For that purpose if we consider a constant penalty, the recovery amount should be computed based on that penalty. But the problem might get more tricky as we move on to a changing penalty (based on repeated failed tasks or on tasks size for example...)  

## Controlling the acceleration of the slashing strategy

Previously, we used an affine function to gauge the impact of our slashing on actors based on their individual failure rates. However, it might be more effective to implement a quadratic or even exponential function. This would rapidly eliminate actors who repeatedly fail, and allow those with fewer errors more time to adjust their strategies and become profitable.

### User reliability metric

For that purpose we need to find out which slash to apply based on wether it is a repeated offense or not.  
Intuitively, I think that the state of the user stake is a good indication of wether he has been acting bad lately or not. If a lot of money has already been slashed it means the user keeps behaving in a non desirable way. We should slash him harder to deter him of continuing.  

### Exponential slashing formula

The exponential slashing formula is designed to impose increasingly severe penalties on users based on their performance, specifically targeting repeated offenses. The formula used is:
$$
y = \alpha^{x+\beta}+\omega
$$

Here’s what each parameter controls:  
$\alpha$: This parameter controls the slope of the exponential curve. A higher value of $\alpha$ makes the penalty increase more rapidly.  
$\beta$: This parameter controls the horizontal shift of the curve. Adjusting $\beta$ shifts the entire curve left or right along the x-axis.  
$\omega$: This parameter controls the vertical shift of the curve. It adjusts the starting point of the penalty on the y-axis.  

See: [Exponential and Logarithmic Functions](https://math.libretexts.org/Courses/Borough_of_Manhattan_Community_College/MAT_206.5/05%3A_Exponential_and_Logarithmic_Functions/5.03%3A_Graphs_of_Exponential_Functions)

In the context of slashing, the variable $x$ represents the unreliability of the user, which is calculated as:  

$$
Unreliability = \frac{S_0 - S_{current}}{S_0}
$$
​
where $S_0$ is the initial stake and $S_{\text{current}}$ is the current stake of the user. The unreliability reflects how much of the initial stake has been slashed.

By using this exponential formula, we can impose steeper penalties on users who continue to perform poorly, effectively deterring repeated offenses while giving users with fewer errors more time to adjust their strategies.

### Real world translation

In a real world situation, we need a formula for how mush to slash on a failed task and how much to reward on a successful task.  

In practice, we should be able to slash $ P = \alpha^{x+\beta}+\omega $ for each failed task and to reward $ R = \frac{F_t \times P}{1 - F_t} $ for each successful task. With $ x = \frac{S_0 - S_{current}}{S_0} $.

## Task size based slashing

Task size-based slashing adjusts penalties and rewards according to the size or complexity of the task. This approach ensures that larger or more complex tasks carry proportional stakes, aligning incentives and penalties with the task's importance.  

This approach also ensures that users cannot fail on very big tasks and recover their lost stake on small and cheap tasks.  

### Practical standpoint

In practice, the task size could be quantified as the total price paid for the task. However the price might be inflated using pumped up app or dataset cost. The most reliable and trustworthy way to quantify the size of a task would be to rely on the computational cost.    

The iExec marketplace already provides a tool to quantify task size through its' proof of contribution (PoC) protocol.

iExec uses a "pay-per-task" model where tasks are categorized based on their complexity and computational requirements. The categories are defined by the maximum computing time (`C`) and maximum deal time (`D`). This categorization helps to standardize task sizes, making it easier to apply our slashing and reward formulas proportionally.

| Category | Maximum Computing Time (C) | Maximum Deal Time (D)   |
|----------|-----------------------------|-------------------------|
| 0 – XS   | 5 min                       | 50 min                  |
| 1 – S    | 20 min                      | 200 min (3h20m)         |
| 2 – M    | 1 hour                      | 10h                     |
| 3 – L    | 3 hours                     | 30h (1d6h)              |
| 4 – XL   | 10 hours                    | 100h (4d4h)             |

Each worker allocates `C` minutes to compute the application. If the computation is not completed within the Maximum Computing Time, the application is stopped. From the buyer's perspective, a requester can claim a task of a deal after `D` minutes if the task is not completed.

By defining task sizes using iExec's categories, we ensure a standardized approach to slashing and rewards. Task size \( T_s \) can be mapped to these categories, making the system both scalable and fair. However there might be an interest to artificially increase a task size so as to recover more money on a successful task. The opposite is not possible, as if you artificially decrease a task size, it may not have enough time allocated to be executed.

### Theoretical standpoint

In our theoretical approach, we'll push aside those concern and consider that we have a fair and reliable way to quantify task size.

The task size could be quantified by computational cost or the total price paid for the task in a reliable and trustworthy manner. For theoretical purposes, we assume the task size $ T_s $ is known, with $ 0 \leq T_s \leq 1 $, where 0 is the smallest possible task and 1 is the largest.

The question of the referential arises, should we base our task size measurement on the global biggest and smallest possible task, or should we base it on the user biggest and smallest task achieved yet. While the latter seem easier to quantify and achieve, it also seem easier to manipulate for a user.  

### Updated slashing formula

To update our model and take into account task size, we could simply reuse the accelerated slashing strategy exponential formula and dedicate one of the parameter to task size.  

In the following function:
$$
y = \alpha^{x+\beta}+\omega
$$

$\alpha$: Provides a steep increase in penalties for low reliability.  
$\beta$: Delays the steep rise in penalties, giving users some initial leniency.  
$\omega$: Ensures there is always a minimum penalty, even when reliability is high.  

The parameters we choose is subjective to the desired effect. And a valid argument could be made for each parameter:  
$\alpha$ allows us to punish more severily for tasks, whereas $\beta$ allows us to delay higher punishment for smaller tasks and $\omega$ could allow us to set a more constant increment to base penalty based on task size.  

## Estimate the minimum Initial Stake Needed

The key factor in effectively implementing a blind slashing system is determining the appropriate initial stake. Setting the initial capital too high could deter individuals from entering the marketplace, while setting it too low increases the risk of users facing financial ruin. The challenge lies in finding the optimal balance: the initial stake should be high enough to deter attackers or careless users by making it costly for them to make the platform fault prone, but not so high that it discourages potential users from participating.

### The Classic Cramér–Lundberg Model

The Cramér-Lundberg model is a mathematical model used in risk theory and actuarial science to describe the evolution of an insurer's surplus over time. The model provides a framework for analyzing the probability of ruin, which occurs when the insurer's surplus becomes negative. What we did earlier is a simplification of this model. The main difference being the way we compute capital over time and the use of a Poisson law to set the number of claims per time period. We can use it in order to try and find the right staking amount.  

### Key Components

1. **Initial Capital ($u$)**: The initial amount of money the insurer has.
2. **Premiums ($P_i$)**: Regular income received by the insurer over time.
3. **Claims ($C_j$)**: Payments made by the insurer when insured events occur.
4. **Claim Frequency ($\lambda$)**: The rate at which claims occur, typically modeled using a Poisson process.
5. **Claim Severity**: The size of the claims, often modeled using a normal or exponential distribution.

### Surplus Process

The surplus process $ U(t) $ describes the insurer's capital at time $ t $:
$$ U(t) = u + \sum_{i=1}^{N_t} P_i - \sum_{j=1}^{M_t} C_j $$

- $ u $ is the initial capital.
- $ N_t $ is the number of premium payments received by time $ t $.
- $ M_t $ is the number of claims by time $ t $.
- $ P_i $ are the premiums.
- $ C_j $ are the claims.

### Probability of Ruin

The probability of ultimate ruin $ \Psi(u) $ is the probability that the surplus process $ U(t) $ will eventually fall below zero:
$$ \Psi(u) = \text{P}( \exists t \geq 0 \text{ such that } U(t) < 0 ) $$

We will estimate the probability of ruin by running many simulations (Monte Carlo method), then we can estimate the probability of ruin 𝜓(𝑢) by counting the fraction of simulations where the capital drops below zero.  