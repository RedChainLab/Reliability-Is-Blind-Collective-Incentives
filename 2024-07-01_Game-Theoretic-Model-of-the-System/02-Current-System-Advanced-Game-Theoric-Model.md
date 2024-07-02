# Advanced Game-Theoretic Model for the current system

## Actors
For our first model, we'll try to abstract the problem a bit. In theory, the Computing Procider is not one actor but several different actors (such as worker, scheduler...) working together.  
We'll only consider 4 different actors: Requesters, dApp Providers, Data Providers and Computing Providers.  
We might even consider dApp Providers and Data Providers as one kind of Actor as they contribute to the marketplace in a very similar way and so we'll deal with them in a very similar way.

1. **Requesters**: Choose a dApp, choose a dataset, set a confidence level, pay fees.
   - Honest: Follow the protocol, choose appropriate dApp and data.
   - Malicious: Choose inappropriate dApp or data to disrupt the system.

2. **Assets Providers**: Upload dApps/datasets, receive fees.
   - Honest: Upload functional, correct dApps / accurate, useful datasets.
   - Malicious: Upload faulty or harmful dApps / incorrect or harmful datasets.

3. **Computing Providers**: Run tasks, validate results, receive fees.
   - Honest: Execute tasks correctly and report accurate results.
   - Malicious: Manipulate task execution or results.

## Strategies and Payoffs
I currently see 3 possible strategies that a player could want to play in the market. The third strategy is hypothetical and infer that there would be a weakness in the system. Here are for each strategy what each actor could hope to earn.  

We consider that "utility from the result" is strictly positive, hence P<sub>r</sub> > Total Cost.  

We also consider that the payoff for ruining someone else can be mapped as the maximum value that you can get someone in the system to loose.

Finally in the case of exploiting a weakness in the system, we'll consider that the malicious actors choosing this strategy for a task find a way to steal all the money at stake, so the "total cost" from the transaction. If several actor use this strategy, we'll split it between them.  
The only exception is the requester, he has no interest in stealing his own money, so his payoff will be "utility from the attack" and will be considered strictly inferior to the "total cost"

  * **S**: Successful and honest task completion (Financial Payoff)
    * P<sub>r</sub> = U<sub>r</sub> - (Price<sub>a</sub> + Price<sub>c</sub>)
    * P<sub>a</sub> = Price<sub>a</sub>
    * P<sub>c</sub> = Price<sub>c</sub> - Cost<sub>c</sub>
  * **F**: Failing task to ruin another actor (Strategic Payoff)
    * P<sub>r</sub> = |min(P<sub>a</sub>, P<sub>c</sub>)|
    * P<sub>a</sub> = |min(P<sub>r</sub>, P<sub>c</sub>)|
    * P<sub>c</sub> = |min(P<sub>r</sub>, P<sub>a</sub>)| - (Cost<sub>c</sub> + Slash<sub>c</sub>)
  * **E**: Exploiting a weakness in the system (Financial Payoff)
    * P<sub>r</sub> = 0
    * P<sub>a</sub> = Price<sub>a</sub> + Price<sub>c</sub>
    * P<sub>c</sub> = Price<sub>a</sub> + Price<sub>c</sub> - (Cost<sub>c</sub> + Slash<sub>c</sub>)

U<sub>r</sub>: Utility from the result
P<sub>r</sub>: Requester payoff  
P<sub>a</sub>: Assets provider payoff  
P<sub>c</sub>: Computing provider payoff  
Slash<sub>c</sub>: Computing provider slash   
Price<sub>a</sub>: Asset price  
Price<sub>c</sub>: Computing price  
Cost<sub>c</sub>: Computing cost  

## Payoff Matrix
For simplicity, we'll start with pairwise interactions and then expand to more complex interactions.

We'll write payoffs in the following way: (P<sub>r</sub>, P<sub>a</sub>, P<sub>c</sub>)

<u>Requester chooses S:</u>  
|Asset / Computer| S | F | E |
|--|--|--|--|
| **S** | (U<sub>r</sub> - (Price<sub>a</sub> + Price<sub>c</sub>), Price<sub>a</sub>, Price<sub>c</sub> - Cost<sub>c</sub>) | (0, 0, -(Cost<sub>c</sub> + Slash<sub>c</sub>)) | (-(Price<sub>a</sub> + Price<sub>c</sub>), 0, Price<sub>a</sub> + Price<sub>c</sub> - (Cost<sub>c</sub> + Slash<sub>c</sub>)) |
| **F** | (0, Cost<sub>c</sub> + Slash<sub>c</sub>, -(Cost<sub>c</sub> + Slash<sub>c</sub>)) | (0, Cost<sub>c</sub> + Slash<sub>c</sub>, -(Cost<sub>c</sub> + Slash<sub>c</sub>)) | (-(Price<sub>a</sub> + Price<sub>c</sub>), Price<sub>a</sub> + Price<sub>c</sub>, Price<sub>a</sub> + Price<sub>c</sub> - (Cost<sub>c</sub> + Slash<sub>c</sub>)) |
| **E** |  |  |  |

<u>Requester chooses F:</u>  
|Asset / Computer| S | F | E |
|--|--|--|--|
| **S** |  |  |  |
| **F** |  |  |  |
| **E** |  |  |  |

<u>Requester chooses E:</u>  
|Asset / Computer| S | F | E |
|--|--|--|--|
| **S** |  |  |  |
| **F** |  |  |  |
| **E** |  |  |  |

These matrix shows the payoffs for the Requester, Assets providers and Computing providers based on their strategies.

## Nash Equilibria
TODO