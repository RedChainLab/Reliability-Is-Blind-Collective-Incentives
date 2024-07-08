# Naive Game-Theoretic Model for the current system

## Actors
For our first model, we'll try to abstract the problem a bit. In theory, the Computing Provider is not one actor but several different actors (such as worker, scheduler...) working together.  
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

## Strategies and Payoffs
A very naïve setup where we consider that people would either fail on accident or successfuly complete their task would leave us with two strategies:
* **S**: Success
* **F**: Fail  

For the requester, we consider that "utility from the result" is strictly positive, hence P<sub>r</sub> > Total Cost. 

  * **S**: Successfuly completing task in honest way
    * P<sub>r</sub> = U<sub>r</sub> - (Price<sub>a</sub> + Price<sub>c</sub>)
    * P<sub>a</sub> = Price<sub>a</sub>
    * P<sub>c</sub> = Price<sub>c</sub> - Cost<sub>c</sub>
  * **F**: Failing task honestly
    * P<sub>r</sub> = 0
    * P<sub>a</sub> = 0
    * P<sub>c</sub> = -(Cost<sub>c</sub> + Slash<sub>c</sub>)

U<sub>r</sub>: Utility from the result  
P<sub>r</sub>: Requester payoff  
P<sub>a</sub>: Assets provider payoff  
P<sub>c</sub>: Computing provider payoff  
Slash<sub>c</sub>: Computing provider slash   
Price<sub>a</sub>: Asset price  
Price<sub>c</sub>: Computing price  
Cost<sub>c</sub>: Computing cost  

## Payoff Matrix and Nash Equilibria

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

## Repeated games

In a single-play game, actors may have an incentive to act selfishly (defect). However, in repeated games, the potential for future interactions typically creates an incentive to cooperate. Actors might choose cooperative strategies to ensure long-term benefits over short-term gains.   

In a repeated game setting, actors can also adopt punishment strategies. If one actor defects, the others can punish the defector in subsequent rounds, discouraging deviation from cooperative behavior.

Regarding the choice of cooperative strategies in the long run, actors may lack real incentives to adopt more cooperative behavior outside of the payment for a successful task. The issue here is that causing a task to fail is virtually costless compared to the effort required to provide real value. Therefore, for malicious actors, the endgame is not to provide value, and their strategy is unlikely to shift towards cooperation.  

Regarding the possibility of punishing bad behaviors, in our system, the worst-case scenario for requesters and assets providers is simply not earning anything. They will never be in a situation where they lose anything, unlike the computing providers who lose computing power and can get slashed. This creates a real imbalance between the different actors. Computing providers are unable to effectively punish other actors, except perhaps by ignoring their requests.


## Conclusion

In a naive approach to the current system, there is a clear incentive for honest actors to cooperate and earn money. However, an actor with malicious intent, who never planned to cooperate, will simply choose a strategy that leads to failed tasks.